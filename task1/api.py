#!/usr/bin/python3
"""
File uses Flask to create one
endpoint that returns “Hello, World!” when called
"""


from flask import Flask

app = Flask(__name__)


@app.route('/api/hello')
def hello_world():
    return 'Hello, World!'

# Hosting this Flask app on 0.0.0.0 instead of 127.0.0.1 means
# that it is reachable outside of the current machine
# (the current machine being a Docker container which is
# running inside of your laptop/desktop)
# Host this Flask app on port 5252
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)
