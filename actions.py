from rasa_core.actions import Action
from rasa_core.events import SlotSet
from datetime import datetime
from pymongo import MongoClient

class ActionExample(Action):

    def name(self):
        # you can then use action_example in your stories
        return "action_example"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        return []


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
      query["$text"] = {
        u"$search": '"'+evento+'"'
      }
      projection["score"] = {
          u"$meta": u"textScore"
      }
      sort = [('score', {'$meta': 'textScore'}), (u"year", 1), (u"day", 1), (u"month", 1)]



      with MongoClient("mongodb://localhost:27017/") as client:
          database = client["kb"]
          collection = database["Calendarios"]
          date = str()
          doc = collection.find_one(query, projection = projection, sort = sort)
          if doc:
             date = self.dateToText(doc['day'], doc['month'], doc['year'])

      return [SlotSet("date", date)]


   def dateToText(self, day, month, year):
        mes = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
        "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        date = date = "{0} de {1}{2}".format(
            day, mes[int(month)-1],
            "" if datetime.now().year == year else "del "+str(year)
            )

        return date
