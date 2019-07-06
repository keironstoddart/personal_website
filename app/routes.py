from app import app
from flask import render_template


@app.route('/')
def about():
	return render_template('about.html')


@app.route('/content')
def content():
	return render_template('content.html')


@app.route('/content/the_data_science_stack')
def the_data_science_stack():
	return render_template('content/the_data_science_stack.html', title='The Data Science Stack')
