#!/usr/bin/env python
import os
from time import asctime
from subprocess import call

# Run this script once when deploying on a new machine
basedir = os.path.abspath(os.path.dirname(__file__))
os.chdir(basedir)

# Create some directories that will be needed later
dirs = ['app/static', 'tmp']
for d in dirs:
	if not os.path.isdir(d):
		print 'creating directory %s' % d
		os.makedirs(d)

log = open('tmp/setup.log', 'a')
log.write('=== Starting setup: %s ===\n' % asctime())

# Get virtualenvy.py from github

# Set up virtualenv
if not os.path.isdir('flask'):
	venv_downloaded = False
	if not os.path.isfile('virtualenv.py'):
		print 'downloading virtualenv.py'
		venv_url = 'https://raw.github.com/pypa/virtualenv/1.9.X/virtualenv.py'
		cmd = ['curl', '-O', venv_url]
		call(cmd, stdout=log, stderr=log)
		venv_downloaded = True

	print 'setting up virtualenv for flask'
	cmd = ['python', 'virtualenv.py', 'flask']
	call(cmd, stdout=log, stderr=log)
	if venv_downloaded:
		os.remove('virtualenv.py')

	# Set up modules within virtualenv
	modules = [
		'flask==0.9',
		'flask-login',
		'flask-openid',
		'flask-mail==0.7.6',
		'sqlalchemy==0.7.9',
		'flask-sqlalchemy==0.16',
		'sqlalchemy-migrate==0.7.2',
		'flask-whooshalchemy==0.55a',
		'flask-wtf==0.8.4',
		'pytz==2013b',
		'flask-babel==0.8',
		'flup']

	for module in modules:
		print 'installing module: %s' % module
		cmd = ['flask/bin/pip', 'install', module]
		call(cmd, stdout=log, stderr=log)
else:
	print 'a "flask" directory already exists, skipping creation of virtualenv'

print 'setup complete'

log.write('=== Setup finished: %s ===\n' % asctime())
log.close()
