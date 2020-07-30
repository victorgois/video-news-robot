with open('./tweets.json', encoding="utf8") as f:
    inputfile = json.load(f)
    data = inputfile[0]

def extract_time(json):
    try:
        # Also convert to int since update_time will be string.  When comparing
        # strings, "10" is smaller than "2".
        return int(data['retweets'])
    except KeyError:
        return 0

# lines.sort() is more efficient than lines = lines.sorted()
lines.sort(key=extract_time, reverse=True)
json.dump(dados, inputfile, indent=4)