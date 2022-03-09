from dotenv import load_dotenv
import flask
import os
load_dotenv()
app = flask.Flask(__name__)
port = os.environ["PORT"]
host = os.environ["HOST"]
load_dotenv()

@app.route('/poweroff', methods=['POST'])
def home():
    os.system("C:/Users/jeth/dev/shutdowner/app/bin/Debug/net6.0/shutdowner.exe")
    print("Attempting to shutdown the PC...")
    return "HEY"


app.run(host=host, port=port)
