from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SessionStarted, ActionExecuted
import logging
print("Imported logging")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
print("Set logging level to DEBUG")

from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class ActionSetLanguage(Action):
    def name(self):
        return "action_set_language"

    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.get('text')

        if "English" in user_message:
            return [SlotSet("language", "en")]
        elif "Finnish" in user_message:
            return [SlotSet("language", "fi")]
        elif "عربي" in user_message or "العربية" in user_message:
            return [SlotSet("language", "ar")]
        return []


class ActionBeforeListen(Action):
    def name(self):
        return "action_before_listen"
    async def run(self, dispatcher, tracker, domain):
        last_action_name = tracker.latest_action_name
        logger.debug(f"Last action name: {last_action_name}")
        logger.debug(f"Tracker: {tracker}")
        return [SlotSet("before_listen", last_action_name)]