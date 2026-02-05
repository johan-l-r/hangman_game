import requests
from random import randint

categories = [
  "countries", 
  "capitals_of_countries", 
  "sports", 
  "animals", 
  "pc_games", 
  "console_games", 
  "mobile_games"
]

def get_random_word():
  category = categories[randint(0, len(categories) - 1)]
  
  response = requests.get(
      "https://random-words-api.kushcreates.com/api",
      params = {
        "category": category,
        "language": "en",  
        "length": 10, 
        "words": 1
        }
      )

  data = response.json()
  return next(iter(data[0].values()))
