# 1. Introduction

Purpose of this website is to host the integration of the Rasa framework based Chatbot called "Essi-Bot"
The website utilizes Flask framework written in Python and uses API to interact with the quizbot.

# 2. Getting Started

<!-- This is a comment Prerequisites: List any software or tools needed to run the website (e.g., Python, Flask, MySQL).-->
<!-- Installation: Step-by-step instructions on how to install the website on a local machine.-->
<!-- Configuration: Instructions on how to configure the website, including setting up environment variables and database connections.-->

## Tools required for this website:

- Python programming language installed (Chatbot requires Python 3.9 to run)
- MySQL (In this case we used MariaDB as our Database)
- Flask (Webframework that makes the website)
- Flask-Babel & getText() (These are used for the localization of the website)

# 3. Localization

## What is getText() and what is Flask-Babel

This website utilizes Flask-Babel library's getText function that fetches marked localization phrases into a template that will be used to produce all the necessary messages, which are then written in their localized versions and then converted into binary, which allows the website to change quickly from one language to another.

## How to use it:

### Inside a python file

To use the localization library gettext you want to import it first into the file

```
from flask_babel import gettext as _
```

with this we utilize the function like this:

```
_("Inside here is the message that we want to translate")
```

The string that you put inside this function tells for the localization library to create a template which will be used later to generate all of the messages needed

### Inside an HTML file

When using Jinja in html files you can use the {%% trans %%} tag to tag strings you want to be translated

example:

```
{%% trans %%} This string will be translated {%% endtrans %%}
```

Using these tags when we run the Babel to fetch all of the translateable string, it will find what we want.

### Creating the templates

next we want to be in the terminal and locate the website folder:

```
cd Flask-Website/website
```

and run the next command

```
pybabel extract -F babel.cfg -o messages.pot .
```

this command will make the Flask-Babel to scan all of the files found in the "website" folder and extract the strings you want to translate and it will put them into messages.pot file.

This file will be created into the "website" folder and there you can find all of the translateable strings.

Example:

```
#: auth.py:46
msgid "Email is required"
msgstr ""
```

confirm that you can find all of the translateable strings that you want.

Next we will run the following command in the terminal:

```
pybabel init -i messages.pot -d translations -l en
```

This will create a new folder called "translations" and inside of it you will find the translations template made for that specific flagged language in this case it's "en".

based off how many languages you want to add to the localization you want to run the command for each of the languages.

Currently the the project has 3 languages supported and for those we use these commands:

```
pybabel init -i messages.pot -d translations -l en
pybabel init -i messages.pot -d translations -l fi
pybabel init -i messages.pot -d translations -l ar
```

After the templates have been created, then we fill in the translated messages for the website.

Example in the translations/fi/messages.pot:

```
#: auth.py:46
msgid "Email is required"
msgstr "Sähköpostiosoite on pakollinen"
```

Last thing to do is to compile the translations by using this command in the terminal:

```
pybabel compile -d translations
```

# 4. Adding Pages

<!--  Creating a New Page: Step-by-step instructions on how to add a new page to the website. -->

<!--   This is from views.py-->
<!--  Eaxmple: images/essi-bot_website.png-->

<!--  Updating Navigation: How to update the navigation menu to include the new page.-->

<!--  This is from website/templates/base.html-->
<!--  Image where to add things: images/essi-bot_navlink-->

<!--  Templates and Static Files: How to create and use templates and static files (CSS, JavaScript, images).-->

<!--  Logically speaking how it works-->
<!--  What is the purpose of base.html-->

# 5. Rasa Chatbot Integration

<!--  Where does the integration happen-->
<!--  Overview: Explanation of how the Rasa chatbot is integrated into the website.-->
<!--  Tell about Webhook-->
<!--  images/essi-bot_webhook-->
<!--  Connecting Rasa to Flask: How to connect the Rasa chatbot to the Flask application.-->

# 6. Database Management

<!--  Where does it happen-->
<!--  images/Database/authentication.py-->
<!--  Database Configuration: How to configure the database connection.-->
<!--  Creating and Updating Tables: Instructions on how to create and update database tables.-->

# 7. Testing

<!--  Where can you find them-->
<!--  What is pytest-->
<!--  How to make them-->
<!--  Running Tests: How to run the test suite.-->
<!-- Writing Tests: Guidelines for writing new tests.-->
<!--  Test Coverage: How to check test coverage.-->

# 8. Deployment

<!--  Preparing for Deployment: Steps to prepare the website for deployment.-->
<!--  Deploying to a Server: Instructions on how to deploy the website to a production server.-->
<!--  Environment Variables: How to set environment variables for production.-->

# 9. Troubleshooting

<!--  Common Issues: List of common issues and their solutions.-->
<!--  Debugging Tips: Tips for debugging and troubleshooting problems.-->
