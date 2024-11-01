## Submission Requirements Report

Submit a report outlining the team's activities in each area of focus within the sprint, covering:

**User Interface Localization**

**Database Localization**

We implemented field-level localizaiton in our database to support multiple languages—Finnish, English, and Arabic—by adding a dedicated translations table. This approach enables specific fields, such as usernames, message content, and issue descriptions, to store translations directly in the database, without duplicating entire records for each language.

**Product Backlog Update**

We updated the Product Backlog to align with the goals for Sprint 5 and created new tasks specifically for this sprint. Clear requirements were defined for the planned work in Sprint 5.

**Localization Resources Identification**

**Database Localization:**

We added a translations table to store localized text for key fields, enabling flexible support for multiple languages directly within the database.
Using this approach, each field requiring localization (e.g., user names, messages, issue descriptions) can be stored with language-specific translations, accessible based on the user’s language preferences.
Character encoding was set to utf8mb4 across all tables to ensure compatibility with diverse character sets, including non-Latin scripts.

**Front-End Localization in Flask:**

We implemented localization for the Flask web interface using Babel and gettext. These tools allowed us to manage and apply translations across the web interface dynamically.
Translations were created for all user-facing text, including form labels, buttons, messages, and navigation elements, ensuring a cohesive multilingual experience.
By integrating Babel and gettext, the interface can automatically display content in the appropriate language based on user preferences or browser settings, allowing for seamless language transitions across the application.
This approach enables flexible and scalable localization on the front end, supporting our goal of delivering a fully localized user experience.

**Rasa Chatbot Localization:**

We localized the Rasa chatbot by adding translations directly into the nlu and domain files, ensuring that the bot can respond accurately in multiple languages.
This involved creating language-specific intents, responses, and training data, allowing the chatbot to recognize and respond to queries in different languages seamlessly.
By organizing translations within Rasa’s structured files, we ensured that the bot’s interactions are consistent and easily maintainable as we continue to support additional languages.

**Sprint Planning and Review**

Additional Requirement:
Include a table within the report that specifies individual contributions. This table should detail:

**Team member names**
**Assigned tasks**
**Time spent on each task**

Jukka
- Sprint planning and review: 3 hours
- Database localization: 3 hours
- User interface localization (Essi-bot): 1 hour
