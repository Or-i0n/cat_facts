from urllib import request
import random
import json
import sys
sys.stdout.reconfigure(encoding="utf-16")

url = "https://raw.githubusercontent.com/Or-i0n/cat_facts/master/catfacts.json"
facts = json.load(request.urlopen(url))
print(random.choice(facts))
