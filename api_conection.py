from flask import Flask, request
from chat import *
import flask

api = Flask(__name__)


@api.route("/", methods=["POST"])
def root():
    code = 200
    response = flask.jsonify({"message": "Hello, world!"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, code


@api.route("/talk", methods=["POST"])
def talk():
    global bot

    code = 200
    req = request.json
    res = {"ok": True, "message": "ok"}

    try:
        message = req["message"]
        context = req["context"]
    except KeyError:
        res = {"ok": False, "message": "One or more required information was not sent!"}
        code = 400
    else:
        if type(context) == str:
            if not context.isnumeric():
                res = {"ok": False, "message": "Context number must be a integer!"}
                code = 400
            else:
                context = int(context)

        if type(message) != str:
            res = {"ok": False, "message": "The message must be a text!"}
            code = 400

        if code == 200:
            message = message.lower().capitalize().strip()
            msg = bot.chat(message)
            if "chatterbot.conversation.Statement" in str(type(msg)):
                res = {"ok": True, "message": str(msg)}
            else:
                res = msg

    finally:
        response = flask.jsonify(res)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, code


if __name__ == "__main__":
    bot = IZZO()
    api.run(debug=True, port=8087)
