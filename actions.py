from rasa_core.actions import Action
from rasa_core.events import SlotSet
from datetime import datetime
from pymongo import MongoClient


class ActionlookforEvent(Action):
    def name(self):
        # type: () -> Text
        return "action_look_event"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        query = {}
        projection = {}
        sort = {}
        evento = tracker.get_slot('event')
        query["$text"] = {u"$search": '"' + evento + '"'}
        projection["score"] = {u"$meta": u"textScore"}
        sort = [('score', {'$meta': 'textScore'}), (u"year", 1), (u"day", 1), (u"month", 1)]

        with MongoClient("mongodb://localhost:27017/") as client:
            database = client["kb"]
            collection = database["Calendarios"]
            docs = collection.find(query, projection=projection, sort=sort)
            matches = []

            if docs[0]['score'] >= 0.800:
                doc = docs[0]
                #print(doc['evento']['nombre'])

                date = "día {0} ".format(self.date_to_text(doc['day'], doc['month'], doc['year']))
                return [SlotSet('date', date)]
            else:
                #dispatcher.utter_template("utter_suggestions", tracker)
               # print (docs)
                for doc in docs:
                    event = doc['evento']['nombre']
                    matches.append(event)
                    return [SlotSet('matching_events', matches)]

        return []

    def date_to_text(self,day, month, year):
            mes = [
                "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
                "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
            ]
            date = "{0} de {1}{2}".format(
                day, mes[int(month) - 1],
                "" if datetime.now().year == year else "del " + str(year)
            )

            return date


class ActionShowEventResults(Action):
    def name(self):
        return 'action_suggest'

    def run(self, dispatcher, tracker, domain):
        match = tracker.get_slot("date")
        matches = tracker.get_slot("matching_events")

        if match:
            #dispatcher.utter_template("utter_ack_eventdate", tracker)
            dispatcher.utter_message("El evento será "+match)
        elif matches:
            suggestions = [{'title': event, 'payload': "/query_event{\"event\": \"%s\""} for event in matches]
            dispatcher.utter_button_message("Quizas quisiste decir: ", suggestions)

        return []