from rasa_core.actions import Action
from rasa_core.events import SlotSet
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
             date = "día {0} del  {1} de este año".format(doc['day'], doc['month'])
          
      return [SlotSet("date", date)]
        
