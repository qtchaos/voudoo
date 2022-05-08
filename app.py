from flask import Flask, render_template, redirect
from flask_htmlmin import HTMLMIN
from flask_minify import Minify

app = Flask(__name__)
app.config['MINIFY_HTML'] = True
htmlmin = HTMLMIN(app)
Minify(app=app, html=True, js=True, cssless=True)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.errorhandler(404)
def page_not_found(e):
    return redirect("/", 302)


if __name__ == '__main__':
    app.run()
