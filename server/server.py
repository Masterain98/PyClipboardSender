import os
import sys
import pyperclip
from flask import Flask, jsonify, request
import json

# Setting root
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_PATH)

# Initial flask
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # jsonify返回的中文正常显示


# clipboard receiver function
@app.route("/clipboardReceiver", methods=["POST"])
def clipboardReceiver():
    # Expect to receive json posts
    content = request.json.get("content").strip()
    passwd = request.json.get("passwd").strip()
    pcName = request.json.get("pcName").strip()

    # Filter the setting
    if server_passwd != "" and server_passwd == passwd or server_passwd == "":
        if server_allowedPC == "":
            pyperclip.copy(content)
            return jsonify({"code": 2000, "msg": "Clipboard content received"})
        elif server_allowedPC != "" and pcName in server_allowedPC_list:
            pyperclip.copy(content)
            return jsonify({"code": 2000, "msg": "Clipboard content received"})
        else:
            return jsonify({"code": 2001, "msg": "Client not in white list"})
    else:
        return jsonify({"code": 2002, "msg": "Wrong password"})


if __name__ == '__main__':
    with open("config.json", 'r') as config:
        configFile = json.loads(config.read())
        server_passwd = configFile["passwd"].replace(' ', '')
        server_allowedPC = configFile["allowedPC"].replace('', ' ')
        server_allowedPC_list = server_allowedPC.split(",")
        print("password: " + server_passwd)
        print("Receiving: " + server_allowedPC)
        print(type(server_allowedPC))

    app.run(host="0.0.0.0", port=5951, debug=True)
