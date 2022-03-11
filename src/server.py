from dotenv import load_dotenv
from flask import Flask, jsonify, make_response
import subprocess
import os
load_dotenv()

app = Flask(__name__)
port = os.environ["PORT"]
host = os.environ["HOST"]

load_dotenv()


def sendErrorResponse(e):
    exceptionMessage = "Failed to initiate shutdown. Reason: " + e
    print(exceptionMessage)
    return make_response(jsonify(success=0, message=exceptionMessage), 500)


@app.route('/poweroff', methods=['POST'])
def index():
    try:
        subprocess.call(["shutdown", "/s", "/t", "20"])
    except Exception as e:
        return sendErrorResponse(str(e))

    sucessMessage = "Shutdown initiated"
    print(sucessMessage)
    return make_response(jsonify(success=1, message=sucessMessage), 200)


app.run(host=host, port=port)
