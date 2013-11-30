import os
from flask import Flask

app = Flask(__name__)
app.debug = True

import main
#import application.models
#import application.views
#import application.controllers