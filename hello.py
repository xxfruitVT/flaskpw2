# import Flask module
from flask import Flask, render_template
# create Flask app intance
app = Flask(__name__, template_folder='views')
#define route for the root URL
@app.route('/')
def hello_world():
    return 'Hello,World!'
#define route for a template rendering
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/main')
def main():
    return render_template('main.html')
# run the app
if __name__ == '__main__':
    app.run(debug=True)
    