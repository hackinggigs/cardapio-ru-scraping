from flask import Flask, jsonify
import scraping

# EB looks for an 'application' callable by default.
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'hello world! pru pru'

@application.route('/menu', methods=['GET'])
def get_tasks():
    return jsonify(scraping.get_menu())

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    # application.debug = True
    application.run()