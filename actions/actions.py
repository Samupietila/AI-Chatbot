from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SessionStarted, ActionExecuted

class ActionBeforeListen(Action):
    def name(self):
        return "action_before_listen"
    async def run(self, dispatcher, tracker, domain):
        last_action_name = tracker.latest_action_name
        return [SlotSet("before_listen", last_action_name)]