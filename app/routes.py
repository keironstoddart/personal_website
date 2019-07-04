from app import app
from flask import render_template


@app.route('/')
def cover():
	return render_template('cover.html')


@app.route('/content')
def content():
	return render_template('content.html')
