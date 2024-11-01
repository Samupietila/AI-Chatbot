
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionSetLanguage(Action):

    def name(self) -> Text:
        return "action_set_language"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = tracker.latest_message.get('text').lower()
        if 'english' in user_message or 'en' in user_message:
            language = 'en'
        elif 'finnish' in user_message or 'fin' in user_message:
            language = 'fi'
        elif 'arabic' in user_message or 'ar' in user_message:
            language = 'ar'
        else:
            language = 'en'  # Default to English

        return [SlotSet("language", language)]