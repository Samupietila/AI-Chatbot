from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionBeforeListen(Action):
    def name(self):
        return "action_before_listen"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:

        last_action_name = tracker.latest_action_name


        bonus_info = tracker.get_slot("bonus_info")

        return [
            SlotSet("before_listen", last_action_name),

        ]
