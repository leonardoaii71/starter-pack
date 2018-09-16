import locale
from datetime import datetime
import pytz
from pymongo import MongoClient
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


if __name__ == '__main__':
    locale.setlocale(locale.LC_TIME, '')


class ActionlookforEvent(Action):
    def name(self):
        # type: () -> Text
        return "action_look_event"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        print(locale.getdefaultlocale())
        locale.setlocale(locale.LC_TIME, 'esp_esp')
        print(locale.getdefaultlocale())
        projection = {}
        sort = {}
        query = {
            "$or": [
                {
                    "date": {
                        "$gte": datetime.now(tz=pytz.timezone('America/Santo_Domingo'))
                    }
                },
                {
                    "evento.finaliza": {
                        "$gte": datetime.now(tz=pytz.timezone('America/Santo_Domingo'))
                    }
                }
            ]
        }
        evento = 'Inicio de prematricula'
        query["$text"] = {
            u"$search": '"' + evento + '"'
        }
        projection["score"] = {u"$meta": u"textScore"}
        sort = [('score', {'$meta': 'textScore'}), (u"date", 1)]

        with MongoClient("mongodb://localhost:27017/") as client:
            database = client["kb"]
            collection = database["Calendarios"]
            docs = collection.find(query, projection=projection, sort=sort).limit(5)
            matches = []
            date = str()
            hoy = datetime.now()
            return [SlotSet('date', datetime.now())]
            # if docs[0]:
            #     if docs[0]['score'] >= 0.800:
            #         if docs[0]['date'] >= hoy:
            #             date = docs[0]['date']
            #         elif docs[0]['date'] < hoy <= docs[0]['evento']['finaliza']:
            #             date = docs[0]['evento']['finaliza']
            #         return "hola"#[SlotSet('date', date)]
            # else:
            #     for doc in docs:
            #         event = doc['evento']['nombre']
            #         matches.append(event)
            #     return "bye"#[SlotSet('matching_events', matches)]

        return []


class ActionShowEventResults(Action):
    def name(self):
        return 'action_suggest'

    def run(self, dispatcher, tracker, domain):
        match = tracker.get_slot("date")
        matches = tracker.get_slot("matching_events")
        date = datetime.strptime(match, '%Y-%m-%d %H:%M:%S.%f')
        date_str = date.strftime('%d de %B del %Y')

        if match:
            print(date_str)
            if date >= datetime.now(tz=pytz.timezone('America/Santo_Domingo')):
                dispatcher.utter_template("utter_ack_eventdate", tracker,
                                          event=tracker.get_slot('event'), date=date_str)

            else:
                print(date_str)
                dispatcher.utter_template("utter_ack_prsnt_eventdate", tracker,
                                          event=tracker.get_slot('event'), date=date_str)


        elif matches:
            dispatcher.utter_template("utter_suggestions", tracker)
            suggestions = [{'title': event, 'payload': "/query_event{\"event\": \"%s\""} for event in matches]
            dispatcher.utter_button_message("", suggestions)

        return []


class ActionLookForAsuetos(Action):
    def name(self):
        # type: () -> Text
        return "action_look_asuetos"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        eventdate = tracker.get_slot('date')
        query = {
            "date": {"$gte": datetime.now(tz=pytz.timezone('America/Santo_Domingo'))}
        }
        if eventdate:
            query = {"date": datetime.strptime(eventdate+"-"+datetime.now().year, '%B-%Y')}
        projection = dict()
        query["evento.asueto"] = "true"
        projection["evento.nombre"] = 1
        matches = list()

        with MongoClient("mongodb://localhost:27017/") as client:
            database = client["kb"]
            collection = database["Calendarios"]
            docs = collection.find(query, projection=projection)

            if docs:
                for doc in docs:
                    #date = datetime.strptime(doc['date'], '%Y-%m-%d %H:%M:%S.%f')
                    #dia = date.strftime('%d de %B del %Y')
                    matches.append(doc['evento']['nombre'])

                dispatcher.utter_template('utter_ack_asuetos', tracker)
                dispatcher.utter_message(matches.__str__())
                return [SlotSet('asueto_count', docs.count())]


class ActionLookForImportant(Action):
    def name(self):
        # type: () -> Text
        return "action_look_important"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        eventdate = tracker.get_slot('date')
        query = {
            "date": {
                "$gte": datetime.now(tz=pytz.timezone('America/Santo_Domingo'))
            }
        }
        if eventdate:
            query = {"date": datetime.strptime(eventdate + "-" + datetime.now().year, '%B-%Y')}
        projection = dict()
        query["evento.importante"] = "true"
        projection["evento.nombre"] = 1
        matches = list()

        with MongoClient("mongodb://localhost:27017/") as client:
            database = client["kb"]
            collection = database["Calendarios"]
            docs = collection.find(query, projection=projection)
            if docs:
                for doc in docs:
                    #date = datetime.strptime(doc['date'], '%Y-%m-%d %H:%M:%S.%f')
                    #dia = date.strftime('%d de %B del %Y')
                    matches.append(doc['evento']['nombre'])
                dispatcher.utter_template('utter_ack_importantes', tracker)
                dispatcher.utter_message(matches.__str__())
                return [SlotSet('importantes_count', docs.count())]


# todo dates
# Convertir fechas a Date Objects
# Solo devolver fechas futuras
# query dates https://stackoverflow.com/questions/2943222/find-objects-between-two-dates-mongodb
