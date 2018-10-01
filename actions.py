import locale
from datetime import datetime
import pytz
from pymongo import MongoClient, collection
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

        evento = tracker.get_slot("event")
        if evento is None:
            dispatcher.utter_template(tracker, "utter_event_not_found")
            return []
        query = {"$or": [
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
        ], "$text": {u"$search": evento}}

        projection = {
            "score": {u"$meta": u"textScore"},
            "evento.nombre": 1,
            "date": 1,
        }
        sort = [('score', {'$meta': 'textScore'}), (u"date", 1)]

        with MongoClient("mongodb://localhost:27017/") as client:
            database = client["kb"]
            collection = database["Calendarios"]
            docs = collection.find(query, projection=projection, sort=sort).limit(5)
            matches = []
            date = str()
            hoy = datetime.now()
            if docs.count() > 0:
                if docs[0]['score'] >= 0.700:
                    if docs[0]['date'] >= hoy:
                        date = docs[0]['date']

                    elif docs[0]['date'] < hoy <= docs[0]['evento']['finaliza']:
                        date = docs[0]['evento']['finaliza']
                    return [SlotSet('date', date)]

                else:
                    for doc in docs:
                        event = doc['evento']['nombre']
                        matches.append(event)
                    return [SlotSet('matching_events', matches)]

            dispatcher.utter_template('utter_sorry', tracker)
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
            if date >= datetime.now(tz=pytz.timezone('America/Santo_Domingo')):
                dispatcher.utter_template("utter_ack_eventdate", tracker,
                                          event=tracker.get_slot('event'), date=date_str)

            else:
                dispatcher.utter_template("utter_ack_prsnt_eventdate", tracker,
                                          event=tracker.get_slot('event'), date=date_str)

        elif matches:
            dispatcher.utter_template("utter_suggestions", tracker)
            suggestions = [{'title': event, 'payload': "/query_event{\"event\": \"%s\""} for event in matches]
            dispatcher.utter_button_message("", suggestions)

        tracker.get_slot('event').reset()
        tracker.slots['date'].reset()
        tracker.get_slot('date').reset()

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
        # if eventdate:
        #    query = {"date": datetime.strptime(eventdate+"-"+str(datetime.now().year), '%B-%Y')}
        projection = dict()
        query["evento.asueto"] = "true"
        projection["evento.nombre"] = 1
        projection["date"] = 1
        matches = list()

        with MongoClient("mongodb://localhost:27017/") as client:
            database = client["kb"]
            collection = database["Calendarios"]
            docs = collection.find(query, projection=projection)

            if docs:
                for doc in docs:
                    dia = doc['date'].strftime('%d de %B del %Y')
                    matches.append(doc['evento']['nombre'] + " " + dia + '\n')

                dispatcher.utter_template('utter_ack_asuetos', tracker)
                dispatcher.utter_message(matches.__str__())
        return [SlotSet('asueto_count', docs.count())]


class ActionCountAsuetos(Action):
    def name(self):
        # type: () -> Text
        return "action_count_asuetos"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        counted = tracker.get_slot('asueto_count')
        if counted:
            print("the count is already done")
            return
        eventdate = tracker.get_slot('date')
        query = {
            "date": {"$gte": datetime.now(tz=pytz.timezone('America/Santo_Domingo'))}
        }
        if eventdate:
            query = {"date": datetime.strptime(eventdate + "-" + datetime.now().year, '%B-%Y')}
        projection = dict()
        query["evento.asueto"] = "true"
        projection["evento.nombre"] = 1

        with MongoClient("mongodb://localhost:27017/") as client:
            database = client["kb"]
            collection = database["Calendarios"]
            docs = collection.find(query, projection=projection)

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
        # if eventdate:
        #   query = {"date": datetime.strptime(eventdate + "-" + str(datetime.now().year), '%B-%Y')}
        projection = dict()
        query["evento.importante"] = "true"
        projection["evento.nombre"] = 1
        projection["date"] = 1
        matches = list()

        with MongoClient("mongodb://localhost:27017/") as client:
            database = client["kb"]
            collection = database["Calendarios"]
            docs = collection.find(query, projection=projection)
            if docs:
                for doc in docs:
                    # date = datetime.strptime(doc['date'], '%Y-%m-%d %H:%M:%S.%f')
                    dia = doc['date'].strftime('%d de %B del %Y')
                    matches.append(doc['evento']['nombre'] + " " + dia + '\n')

                dispatcher.utter_template('utter_ack_importantes', tracker)
                dispatcher.utter_message(matches.__str__())
        return [SlotSet('importantes_count', docs.count())]


class ActionCountImportant(Action):
    def name(self):
        # type: () -> Text
        return "action_count_important"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        counted = tracker.get_slot('importantes_count')
        if (counted):
            print("the count is already done")
            return

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

        with MongoClient("mongodb://localhost:27017/") as client:
            database = client["kb"]
            collection = database["Calendarios"]
            docs = collection.find(query, projection=projection)

        return [SlotSet('importantes_count', docs.count())]
    
    
    #Actions para procesos
class ActionlookforProcessDescription(Action):
    def name(self):
        # type: () -> Text
        return "action_process_descripcion"

    def run(self, dispatcher, tracker, domain):
        proceso = tracker.get_slot("proceso")
        with MongoClient("mongodb://localhost:27017/") as client:
            database = client["kb"]
            collection = database["Procesos"]
            query = {
            "nombre": proceso
            }
            projection = {"descripcion": 1}
            docs = collection.find_one(query, projection=projection)
            descripcion = docs["descripcion"]

            dispatcher.utter_template("utter_descripcion_proceso", tracker,
                                      proceso=tracker.get_slot('proceso'))


class ActionlookforProcessImportancia(Action):
    def name(self):
        # type: () -> Text
        return "action_process_importancia"

    def run(self, dispatcher, tracker, domain):
        pass


class ActionlookforProcessPenalidad(Action):
    def name(self):
        # type: () -> Text
        return "action_process_penalidad"

    def run(self, dispatcher, tracker, domain):
        pass

class ActionlookforProcessAdvertencia(Action):
    def name(self):
        # type: () -> Text
        return "action_process_advertencia"

    def run(self, dispatcher, tracker, domain):
        pass

class ActionlookforProcessProcedimiento(Action):
    def name(self):
        # type: () -> Text
        return "action_process_procedimiento"

    def run(self, dispatcher, tracker, domain):
        pass

