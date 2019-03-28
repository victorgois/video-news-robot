import requests

r = r.json
url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2019-03-11&'
       'sortBy=popularity&'
       'apiKey=2de5d157d448424db4574be570b492d4')

response = requests.get(url)

print r.json

