import pytest
from main import app
from Database.authentication import delete_user, emailCheck, usernameCheck


# Creating the test client
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
    
# Get Homepage
@pytest.fixture
def home_response(client):
    response = client.get('/')
    return response

# Get Login Page
@pytest.fixture
def login_response(client):
    response = client.get('/login')
    return response
    
# Get Register Page
@pytest.fixture
def register_response(client):
    response = client.get('/register')
    return response

@pytest.fixture(scope='session', autouse=True)
def cleanup():
    yield
    # Cleanup code to delete test users
    test_users = [
        {"email": "testUser@EssiBot.fi", "username": "TestUser"},
        {"email": "testUser@EssiBot2.fi", "username": "TestUser2"},
        {"email": "testUserToDelete@EssiBot.fi", "username": "TestUserToDelete"}
    ]
    for user in test_users:
        delete_user(user['email'], user['username'])
    

# Testing that every page were retrieved
def test_home_page(home_response, login_response, register_response):
    # Verify Homepage
    assert home_response.status_code == 200
    assert b"Home.html" in home_response.data
    
    # Verify Login Page
    assert login_response.status_code == 200
    assert b"Login" in login_response.data
    
    # Verify Register Page
    assert register_response.status_code == 200
    assert b"Create a new account" in register_response.data

def test_register_page(client):
    form_data = {
        "email": "testUser@EssiBot.fi",
        "username": "TestUser",
        "password1": "password123",
        "password2": "password123"
    }
    response = client.post('/register', data=form_data)
    assert response.status_code == 302
    
    print("Response data:", response.data)
    
    client.get('/logout')
    login_response = client.post('/login', data={"username": form_data["username"], "password": form_data["password1"]})
    assert login_response.status_code == 200
    
    check = usernameCheck(form_data['username'])
    print("usernameCheck result:", check)
    
    assert check
    
    
    
# Registering password Fail Test
def test_register_password_fail(client):
    form_data = {
        "email":"testUser@EssiBot.fi",
        "username":"TestUser",
        "password1":"123",
        "password2":"password123"
    }
    response = client.post('/register', data=form_data)
    assert response.status_code == 200
    assert b'Passwords are not matching' in response.data
    
# Registering username Fail Test
def test_register_username_fail(client):
    form_data = {
        "email":"testUser@EssiBot.fi",
        "username":"Tes",
        "password1":"password123",
        "password2":"password123"
    }
    response = client.post('/register', data=form_data)
    assert response.status_code == 200
    assert b'Lenght of Username must be more than 3' in response.data    
    
# Registering email Fail Test
def test_register_email_fail(client):
    form_data = {
        "username":"TestUser",
        "password1":"password123",
        "password2":"password123"
    }
    response = client.post('/register', data=form_data)
    assert response.status_code == 200
    assert b'Email is required' in response.data    

# Login Test
def test_login(client):
    form_data = {
        "email":"testUser@EssiBot2.fi",
        "username":"TestUser2",
        "password1":"password123",
        "password2":"password123"
    }
    response = client.post('/register', data=form_data)
    assert response.status_code == 302
    
    form_data = {
        "username":"TestUser",
        "password":"password123"
    }
    response = client.post('/login', data=form_data)
    assert response.status_code == 200
    
    print(response.data)
    assert b'Logged in successfully!' in response.data

# ChatBot Test >> Chatbot has to be run for it to work >> rasa run --enable-api --cors "*"
def test_get_response_from_chatbot(client):
    expected_message="Hello! Welcome to the customer service, what would you like to have help with?"
    payload = {
        "message" : "Hello, chatbot!"
    }
    response = client.post('/webhook', json=payload)
    assert response.status_code == 200
    assert expected_message.encode() in response.data
    