from replit import db

allwords = []
with open('wordlist') as f:
  allwords = [line.strip() for line in f]

wordstamps = []
if 'wordstamps' in db.keys():
  wordstamps = db["wordstamps"]

def make_entry(word, contents):
  db[word] = contents

def get_entry(word):
  return db[word]

def del_entry(word):
  del db[word]

def update_wordstamps():
  db["wordstamps"] = wordstamps