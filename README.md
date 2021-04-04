# PyClipboardSender

PyClipboardSender will send all clipboard content from client program to the server program via HTTP POST, to allow server copy the content to its local clipboard automatically. 

---

## Feature

- Send and receive Clipboard content between Windows devices
- Protected by password
- Protected by hostname (computer name)
- Works either in LAN or Internet

## Usage

- Server
  - Set password and client-whitelist in ```config.json```
    - Password is **required**
    - Multiple allowed devices can be separated by comma (```,```)
    - Leave ```allowedPC``` field empty if you want to receive clipboard from any device
  - Allow the program using ```5951``` port in Windows Defender Firewall
    - ```server.exe``` will start a web service to receive clipboard content from clients
  - Run ```server.exe``` and leave it minimized
- Client
  - Set IP/domain and password in ```config.json```
    - Both server and password field are **required**
  - Run ```client.exe``` and leave it minimized

