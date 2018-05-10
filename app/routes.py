from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Hector'}
	events = [
		{
			'name': 'Workshop Python',
			'date': 'May 10'
		},
		{
			'name': 'Captura la bandera',
			'date': 'May 10, 11'
		}
	]

	return render_template('index.html', user=user, title='UPSLP', events=events)