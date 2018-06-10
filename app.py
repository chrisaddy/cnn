from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flaskext.markdown import Markdown
from flask_nav import Nav
from flask_nav.elements import Navbar, View



app = Flask(__name__)
Bootstrap(app)
Markdown(app)

nav = Nav()

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/hadamard_product")
def hadamard():
	return render_template('linear_algebra/hadamard_product.html')

@nav.navigation()
def navbar():
	return Navbar(
		'Convoluted Notebook Network',
		View('Home', 'index'),
		View('About', 'about')
	)

nav.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0')