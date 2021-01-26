from flask import Flask
from threading import Thread
import database as db

app = Flask('')

@app.route('/')
def main():
  return "The bot is alive!"

@app.route('/get/<word>')
def getpost(word):
  return db.get_entry(word)

@app.route('/post/<word>/<contents>')
def createpost(word, contents):
  db.make_entry(word, contents)
  return "Created entry"

@app.route('/delete/<word>')
def deletepost(word):
  db.del_entry(word)
  return "Deleted entry"

def run():
  app.run(host="0.0.0.0", port=8080)

def run_server():
  server = Thread(target=run)
  server.start()