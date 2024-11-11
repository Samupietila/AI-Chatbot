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
    
# TESTS
@pytest.fixture
def home_response_en(client):
    response = client.get('/', headers={"Accept-Language": "en"})
    return response

@pytest.fixture
def home_response_fi(client):
    response = client.get('/', headers={"Accept-Language": "fi"})
    return response

@pytest.fixture
def home_response_ar(client):
    response = client.get('/', headers={"Accept-Language": "ar"})
    return response

@pytest.fixture
def login_response_en(client):
    response = client.get('/login', headers={"Accept-Language": "en"})
    return response

@pytest.fixture
def login_response_fi(client):
    response = client.get('/login', headers={"Accept-Language": "fi"})
    return response
    
@pytest.fixture
def login_response_ar(client):
    response = client.get('/login', headers={"Accept-Language": "ar"})
    return response

@pytest.fixture
def register_response_en(client):
    response = client.get('/register', headers={"Accept-Language": "en"})
    return response

@pytest.fixture
def register_response_fi(client):
    response = client.get('/register', headers={"Accept-Language": "fi"})
    return response

@pytest.fixture
def register_response_ar(client):
    response = client.get('/register', headers={"Accept-Language": "ar"})
    return response
    
# For Context
def test_localization_home_page(home_response_en, home_response_fi, home_response_ar):
    
    # Checking status Code
    assert home_response_fi.status_code == 200
    assert home_response_ar.status_code == 200
    assert home_response_en.status_code == 200
    
    assert "مرحبًا بك في موقع الكازينو" in home_response_ar.data.decode('utf-8')
    assert "Tervetuloa" in home_response_fi.data.decode('utf-8')
    assert "Welcome" in home_response_en.data.decode('utf-8')

    
def test_localization_get_register_response_en(register_response_en):
    
    # Checking status code
    assert register_response_en.status_code == 200
    
    # Asserting the necessary context
    assert "Register" in register_response_en.data.decode('utf-8')
    assert "Username" in register_response_en.data.decode('utf-8')
    assert "Password" in register_response_en.data.decode('utf-8')

    
    
def test_localization_get_register_response_fi(register_response_fi):
    
    #Checking Status Code
    assert register_response_fi.status_code == 200
    
    #Asserting thigns
    assert "Rekisteröi" in register_response_fi.data.decode('utf-8')
    assert "Käyttäjänimi" in register_response_fi.data.decode('utf-8')
    assert "Salasana" in register_response_fi.data.decode('utf-8')
    
def test_localization_get_register_response_ar(register_response_ar):
    
    #Checking Status Code
    assert register_response_ar.status_code == 200
    
    #Asserting thigns
    assert "إنشاء حساب" in register_response_ar.data.decode('utf-8')
    assert "عنوان البريد الإلكتروني" in register_response_ar.data.decode('utf-8')
    assert "اسم المستخدم" in register_response_ar.data.decode('utf-8')
    
def test_localization_get_login_response_en(login_response_en):
    
    # Checking Status code
    assert login_response_en.status_code == 200
    
    # Asserting Things
    assert "Login" in login_response_en.data.decode('utf-8')
    assert "Username" in login_response_en.data.decode('utf-8')
    assert "Password" in login_response_en.data.decode('utf-8')
    
def test_localization_get_login_response_fi(login_response_fi):
    
    #Checking Status Code
    assert login_response_fi.status_code == 200
    
    # Asserting things
    assert "Kirjaudu Sisään" in login_response_fi.data.decode('utf-8')
    assert "Käyttäjänimi" in login_response_fi.data.decode('utf-8')
    assert "Salasana" in login_response_fi.data.decode('utf-8')
        
def test_localization_get_login_response_ar(login_response_ar):
    
    # Checking Status Code
    assert login_response_ar.status_code == 200
    
    # Asserting things
    assert "تسجيل الدخول" in login_response_ar.data.decode('utf-8')
    assert "اسم المستخدم" in login_response_ar.data.decode('utf-8')
    assert "كلمة المرور" in login_response_ar.data.decode('utf-8')

# Testing the database
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

def test_get_response_from_chatbot_en(client):
    expected_message="Hello! Welcome to the customer service, what would you like to have help with?"
    payload = {
        "message": "Hello, chatbot!",
        "metadata": {
            "language": "en"
        }
    }
    response = client.post('/webhook', json=payload)
    assert response.status_code == 200
    assert expected_message.encode() in response.data
    
    
def test_get_response_from_chatbot_fi(client):
    expected_message="Hello! Welcome to the customer service, what would you like to have help with?"
    payload = {
        "message": "Hei, chatbot!",
        "metadata": {
            "language": "fi"
        }
    }
    response = client.post('/webhook', json=payload)
    assert response.status_code == 200
    assert expected_message.encode() in response.data
    
def test_get_response_from_chatbot_ar(client):
    expected_message="Hello! Welcome to the customer service, what would you like to have help with?"
    payload = {
        "message": "Hello, chatbot!",
        "metadata": {
            "language": "en"
        }
    }
    response = client.post('/webhook', json=payload)
    assert response.status_code == 200
    assert expected_message.encode() in response.data
    