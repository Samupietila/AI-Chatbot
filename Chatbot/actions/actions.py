
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

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
        metadata = tracker.latest_message.get('metadata', {})
        language = metadata.get('language')
        print(tracker.latest_message)
        print("ActionSetLanguage triggered")
        print("Metadata from the message: ", metadata)
        print("Language from metadata: ", language)
        print(f"User message: {user_message}")

        # Ensure language is not None
        if language is None:
            language = ""

        # Determine the language based on the user message
        if 'english' in language or 'en' in language:
            language = 'en'
            return [SlotSet("language", language)]
        elif 'finnish' in language or 'fi' in language:
            language = 'fi'
            return [SlotSet("language", language)]
        elif 'arabic' in language or 'ar' in language:
            language = 'ar'
            return [SlotSet("language", language)]
        else:
            language = 'en'  # Default to English if no valid language is found
        print(f"Setting language to: {language}")
        return [SlotSet("language", language)]