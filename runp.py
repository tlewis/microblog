#!flask/bin/python
import os
from app import app
if not os.path.isdir('tmp'):
    os.makedirs('tmp')
app.run(host = '0.0.0.0', debug = False)
