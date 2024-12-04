# 1. Introduction

## 1. Introduction

### Overview

The Flask-Website is a web application built using the Flask framework. It includes features such as user authentication, a Rasa chatbot integration, and more.

### Purpose

The purpose of this website is to provide a platform for users to interact with various services, including a chatbot for customer support.

# 2. Getting Started

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

After running the command to compile the messages, there should now be a .mo file. That means that the translations have been created successfully.

# 4. Adding Pages

To add a new page in to the website you need to:

## Create a new .html file:

into the templates folder found in

```
Flask-Website/website/templates
```

create a new .html file Example: "newpage.html"

## Create a function that creates the website

You need to create a decorator for the website so that Flask will redirect you to the correct place

```
@views.route('/newpage')
```

```
return render_template("newpage.html")
```

The end result of the function for the website is:

```
@views.route('/newpage')
def newPage():
    return render_template("newpage.html")
```

This will give the user the .html to show, while also applying base.html to it.

# 5. Rasa Chatbot Integration

Integration of the Rasa chatbot is handled in the views.py file, through the use of API requests. Specifically the Flask application sends a POST requests to the Rasa server's webhook endpoint with the user's message and the metadata(which includes the language the user has decide to use).

The default address for this is currently configured as:

```
http://localhost:5005/webhooks/rest/webhook
```

# 6. Database Management

For a working database connection it is important to have a config.py file created into the Flask-Website/Database folder

And inside of it you want to have the following added:

```
DB_CONFIG = {
    'user': 'usernametoaccessyourdatabase',
    'password': 'yourdatabasepassword',
    'host': 'localhost',
    'database': 'ChatAppDatabase',
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_unicode_ci',
    'raise_on_warnings': True
}

```

And the functions for database actions are found in the Flask-Website/Database/authentication.py file.

## Creating and Updating Tables

To create and update database tables, follow these steps:

### Creating Tables

1. **Use the SQL File**: The database schema is defined in the `database.sql` file located in the `Flask-Website/Database` folder. You can use this file to create the tables.

2. **Execute the SQL File**: Run the following command in your MySQL or MariaDB client to execute the SQL file and create the tables.

   ```bash
   mysql -u yourusername -p yourpassword ChatAppDatabase < /path/to/Flask-Website/Database/database.sql
   ```

### Updating Tables

1. **Modify the SQL File**: Update the `database.sql` file with the necessary changes to the table schema.

2. **Apply the Changes**: Re-run the updated `database.sql` file to apply the changes to the database.

   ```bash
   mysql -u yourusername -p yourpassword ChatAppDatabase < /path/to/Flask-Website/Database/database.sql
   ```

By following these steps, you can create and update database tables in your Flask application using the provided SQL file.

# 7. Testing

## Overview

For testing of the Flask-Website a testing library called "pytest" will be used for this.

## Where to find tests:

All test files are located in the "tests" folder found in

```
Flask-Website/tests
```

## Creating new tests:

To create new tests it is important to know that for pytest to be able to run the tests each of the test functions need to have the prefix "test\_"

Example of a test function:

```
def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Casino" in response.data
```

By following these guidelines and examples, you can ensure that your Flask-Website is thoroughly tested.

once all of the test files have been made, to actually run the tests, you need to be inside the Flask-Website folder

```
cd Flask-Website
```

and run the following command:

```
pytest
```
