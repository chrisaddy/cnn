from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View
import os

app = Flask(__name__)
Bootstrap(app)

nav = Nav()

### for pages not yet built
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

### route home page
@app.route("/")
def index():
	return render_template('index.html')

### route about page

@app.route("/about")
def about():
	return render_template('about.html')

### route everything else
@app.route('/<path:path>')
def static_file(path):
	return render_template('%s.html' % path)

### navigation
@nav.navigation()
def navbar():
	return Navbar(
		'Convoluted Notebook Network',
		View('Home', 'index'),
		View('About', 'about')
	)

nav.init_app(app)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)