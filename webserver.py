from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "The bot is alive!"

def run():
  app.run(host="0.0.0.0", port=8080)

def run_server():
  server = Thread(target=run)
  server.start()