import unittest
from Database.authentication import get_localized_welcome_message

class TestLocalization(unittest.TestCase):

    def test_welcome_message_finnish(self):
        """Test that the welcome message is correctly localized for Finnish."""
        language_code = 'FI'
        expected_message = 'Tervetuloa sivustollemme!'
        actual_message = get_localized_welcome_message(language_code)
        self.assertEqual(actual_message, expected_message, f"Expected '{expected_message}' but got '{actual_message}'")

    def test_welcome_message_arabic(self):
        """Test that the welcome message is correctly localized for Arabic."""
        language_code = 'AR'
        expected_message = 'مرحبًا بكم في موقعنا!'
        actual_message = get_localized_welcome_message(language_code)
        self.assertEqual(actual_message, expected_message, f"Expected '{expected_message}' but got '{actual_message}'")

    def test_welcome_message_fallback(self):
        """Test that the fallback message is displayed for an unsupported language."""
        language_code = 'ES'
        expected_message = 'Welcome!'
        actual_message = get_localized_welcome_message(language_code)
        self.assertEqual(actual_message, expected_message, f"Expected '{expected_message}' but got '{actual_message}'")

if __name__ == '__main__':
    unittest.main()
