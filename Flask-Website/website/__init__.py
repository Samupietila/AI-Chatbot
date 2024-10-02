from flask import Flask
from flask_login import LoginManager, current_user


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123SecretKey321'
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    from Database import authentication
    
    @login_manager.user_loader
    def load_user(id):
        return authentication.load_user(id)
    
    @app.context_processor
    def inject_user():
        return dict(user=current_user)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    

    
    return app
    