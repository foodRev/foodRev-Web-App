# [START app]
import logging

# [START imports]
from flask import Flask, render_template, request
# [END imports]

# [START create_app]
app = Flask(__name__)
# [END create_app]

# [START Login]
@app.route('/')
def login():
    return render_template('login_content.html')
# [END Login]

# [START Login Success Landing]
@app.route('/login_success', methods=['POST'])
def login_success():
    name = request.form['name']
    email = request.form['email']
    return render_template(
        'login_success_landing.html',
        name=name,
        email=email)
# [END Login Success Landing]

# [START auth]
@app.route('/auth')
def auth():
    return render_template('firebase_auth.html')
# [END auth]

# [START form]
@app.route('/form')
def form():
    return render_template('form.html')
# [END form]


# [START submitted]
@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']

    # [END submitted]
    # [START render_template]
    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        site=site,
        comments=comments)
    # [END render_template]


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
