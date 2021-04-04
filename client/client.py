import pyperclip
import json
import requests
import socket
import time
import os
import sys


if __name__ == '__main__':
    # Setting root
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, BASE_PATH)

    # Read Config
    with open("config.json", "r") as config:
        configFile = json.loads(config.read())
        server = configFile["server"]
        passwd = configFile["passwd"]
        print("server: http://" + server + ":5951")
        print("password: " + passwd)
    targetURL = "http://" + server + ":5951/clipboardReceiver"
    headers = {'Content-Type': 'application/json'}

    # Get hostname
    hostname = socket.gethostname()
    print(hostname)
    lastRecord = ""
    while True:
        # Read current clipboard content
        clipboard_content = pyperclip.paste()

        if clipboard_content != lastRecord:
            payload = {"content": clipboard_content, "passwd": passwd, "pcName": hostname}
            lastRecord = clipboard_content
            # Send clipboard content via HTTP POST
            response = requests.post(targetURL, data=json.dumps(payload), headers=headers).text
            returnInfoJson = json.loads(response)
            responseCode = returnInfoJson.get("code")
            print("Return Code " + str(responseCode))
        time.sleep(0.5)
