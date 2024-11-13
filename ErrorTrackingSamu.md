# Error tracking while making functional tests to rasa

- Rasa can't make coverage report by "rasa test --coverage-report" like it says in the https://rasa.com/docs/rasa-pro/production/testing-your-assistant/
- Rasa doesnt know command e2e in "rasa test e2e" like it says in the https://rasa.com/docs/rasa-pro/production/testing-your-assistant/
- Custom action testing never works because the rasa version we are using is too old, and the newer ones cost money
- when making test_cases.yml file and trying run tests "rasa test" Rasa is having troubles to find any stories to evaluate.
  But somehow when i accidentally removed the test case file and ran tests it found 357 test cases. So i have no idea how to make tests work like they should.
- if it happens to find a story to evaluate, its predications are on a weird loop and the tests fail everytime except when testing only saying hi or goodbye.
