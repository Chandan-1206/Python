# News App exercise

# requests is explicit module hence need to be installed first
import requests
import json
# json is javascript object notation (a format for human readable text)

query=input("What type of news are you interested in ? : ")
date=input("from which date(YYYY-MM-DD) within last month ? : ")
# we will use link from News Api by generating Apikey
url=f"https://newsapi.org/v2/everything?q={query}&from={date}&sortBy=publishedAt&apiKey=8eef7e9491674b87bb77cb91a428bf81"
r=requests.get(url)
news = json.loads(r.text) # changes format to dictionaries
# print(news,type(news))  # to make it more representable we can use for loop
for article in news["articles"]:
  print("Title :\n",article["title"],"\n")
  print("Description :\n",article["description"])
  print("___________________")
