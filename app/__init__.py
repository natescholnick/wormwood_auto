from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)

# ignore CORS restrictions
CORS(app)

# all variables based on this application must be instantiated after the app instance is created

bootstrap = Bootstrap(app)

# flask app instance uses from object method to laod in all configurartion variables
app.config.from_object(Config)

# setup database variables
db = SQLAlchemy(app)

# app variable for handling login functionality
login = LoginManager(app)

# when a page requires someone to be logged in, specify the route they should be sent to when accessing that page anonymously
login.login_view = 'login'


from app import routes
