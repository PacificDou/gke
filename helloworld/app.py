from flask import Flask, request, render_template
from flask_cors import CORS
import os, threading
import logging


app = Flask(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# set logging level
logging.basicConfig(level=logging.DEBUG)


@app.route("/", methods=["GET"])
def hello_world():
    message = "Hello World! <br>Version: {}<br>Pod name: {}<br>Pod IP: {}<br>Pod service account: {}<br>Process id: {}<br>Thread id: {}".format(
        os.environ.get('VERSION', 'Unknown'), 
        os.environ.get('POD_NAME', 'Unknown'), os.environ.get('POD_IP', 'Unknown'), os.environ.get('POD_SERVICE_ASCCOUNT', 'Unknown'),
        os.getpid(), threading.get_ident()
    )
    return message


if __name__ == "__main__": 
    # CAUTION: initialization of resources should be not put here (except the global variable app)
    # because when gunicorn invokes this script, the __name__ will NOT be __main__
    # ref: https://stackoverflow.com/questions/60332174/gcp-if-name-main-not-working
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 11280)), debug=False)
