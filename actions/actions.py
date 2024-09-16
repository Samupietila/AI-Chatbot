# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SessionStarted, ActionExecuted
from rasa_sdk.events import SlotSet
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# class ActionButtonTest(Action):
#     def name(self):
#         return "utter_button_test"

#     def run(self, dispatcher, tracker, domain):
#         dispatcher.utter_message(template="utter_button_test")
#         return []

class ActionBeforeListen(Action):
    def name(self):
        return "action_before_listen"
    async def run(self, dispatcher, tracker, domain):
        last_action_name = tracker.latest_action_name
        return [SlotSet("before_listen", last_action_name)]