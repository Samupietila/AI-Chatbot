from website import create_app
from flask_cors import CORS
from website.views import views

app = create_app()
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
    
    