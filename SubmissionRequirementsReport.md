## Submission Requirements Report

## User Interface Localization and Localization Resources Identification

**Front-End Localization in Flask:**

We implemented localization for the Flask web interface using Babel and gettext. These tools allowed us to manage and apply translations across the web interface dynamically.
Translations were created for all user-facing text, including form labels, buttons, messages, and navigation elements, ensuring a cohesive multilingual experience.
By integrating Babel and gettext, the interface can automatically display content in the appropriate language based on user preferences or browser settings, allowing for seamless language transitions across the application.
This approach enables flexible and scalable localization on the front end, supporting our goal of delivering a fully localized user experience.

**Rasa Chatbot Localization:**

We localized the Rasa chatbot by adding translations directly into the nlu and domain files, ensuring that the bot can respond accurately in multiple languages.
This involved creating language-specific intents, responses, and training data, allowing the chatbot to recognize and respond to queries in different languages seamlessly.
By organizing translations within Rasa’s structured files, we ensured that the bot’s interactions are consistent and easily maintainable as we continue to support additional languages.

**Database Localization:**

We added a translations table to store localized text for key fields, enabling flexible support for multiple languages directly within the database.
Using this approach, each field requiring localization (e.g., user names, messages, issue descriptions) can be stored with language-specific translations, accessible based on the user’s language preferences.
Character encoding was set to utf8mb4 across all tables to ensure compatibility with diverse character sets, including non-Latin scripts.

## Product Backlog Update

We updated the Product Backlog to align with the goals for Sprint 5 and created new tasks specifically for this sprint. Clear requirements were defined for the planned work in Sprint 5.

## Sprint Planning and Review

**Team member names**
**Assigned tasks**
**Time spent on each task**

Jukka
- Mixed tasks: 1 hour
- Sprint planning and review: 3 hours
- Database localization: 3 hours
- User interface localization (Essi-bot): 1 hour
- Submission requirements report: 1 hour

Mika
- Daily sprints: 3 hours
- Research for Project: 3 Hours
- Website Localization: 14 Hours
- Chatbot Localization: 7 Hours

Zehra
- Essi-bot translations/localization: 9 hours
- Daily sprints: 3 hours


Samuel
- Mixed tasks: 4h
- Daily sprints: 3 hours
- Research for Project: 2 Hours
