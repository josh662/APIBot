from flask import Flask, request
from flask_cors import CORS
from src.chat import *
import flask

def create_app():
    app = Flask(__name__)
    return app

app = create_app()
bot = IZZO()

cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

app.config['JSON_AS_ASCII'] = False

@app.route("/", methods=["POST"])
def root():
    code = 200
    response = flask.jsonify({"message": "Hello, world!"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, code

@app.route("/talk", methods=["POST"])
def talk():
    code = 200
    req = request.json
    res = {"code": code, "message": "ok"}

    try:
        message = req["message"]
        if type(message) != str:
            res = {"ok": False, "message": "The message must be a text!"}
            code = 400

        if code == 200:
            message = message.lower().capitalize().strip()
            msg = bot.chat(message)
            print(msg)
            if "chatterbot.conversation.Statement" in str(type(msg)):
                res = {"ok": True, "message": str(msg)}
            else:
                res = msg
    except KeyError:
        res = {"ok": False, "message": "One or more required information was not sent!"}
        code = 400
        

    finally:
        response = flask.jsonify(res)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, code


if __name__ == "__main__":
    app.run(debug=True, port=8087)
