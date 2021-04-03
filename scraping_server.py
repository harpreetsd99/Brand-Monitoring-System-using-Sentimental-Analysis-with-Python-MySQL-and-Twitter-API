# Import
from os import environ
from flask import Flask

# Instance Created
app = Flask(__name__)

# Used for accessing environment variables 
app.run(environ.get('PORT'))  