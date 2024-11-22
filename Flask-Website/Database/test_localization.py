from Database.authentication import get_localized_welcome_message

def test_get_localized_welcome_message():
    languages = ['EN', 'FI', 'AR']

    for lang in languages:
        print(f"Testing with language code '{lang}':")
        message = get_localized_welcome_message(lang)
        print(f"Localized Welcome Message: {message}\n")

if __name__ == '__main__':
    test_get_localized_welcome_message()