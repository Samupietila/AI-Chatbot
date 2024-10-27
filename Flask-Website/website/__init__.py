from flask import Flask, request
from flask_login import LoginManager, current_user
from flask_babel import Babel, gettext as _

def get_locale():
        language = request.cookies.get('language')
        if language:
            return language
        return request.accept_languages.best_match(['en', 'fi', 'ar'])

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123SecretKey321'
    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
    
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
    
    babel = Babel(app)
    
    
    
    babel.init_app(app, locale_selector=get_locale)
    
    return app