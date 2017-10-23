#@app.route('/')
#def index():
#   return render_template("index.html")

from flask import Flask, render_template
from string import Template
app = Flask(__name__)

HTML_TEMPLATE = Template("""
<h1>Hello ${name}!</h1>
""")

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/<int:user_id>')
def view_user(user_id):
	if user_id < 11:
		return render_template('base.html', user=user_id)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)