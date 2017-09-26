'''
Shannon Lau and Eugene Thomas
SoftDev1 Period 7
HW #05: Jinja Tuning ...
2017-09-26
'''

from flask import Flask, render_template
import random

app = Flask(__name__)

# landing page
@app.route("/")
def hello_world():
    return "<a href='/occupations'>View Occupations!</a>"

# occupation page
# render template according to occupations.csv
@app.route('/occupations')
def occupation():
    return render_template('occupations.html',
                            collection=collection(),
                            rand_occupation=rand_occupation(collection()))

# return a list of all occupations and corresponding percentages
# [occupation1, percentage1, occupation2, percentage2, ...]
def collection():
    try:
        lines = open('data/occupations.csv').read().splitlines()[1:-1]
    except:
        return []
    arr = []
    for i in lines:
        pair = i.rsplit(',',1)
        for j in pair:
            arr.append(j.strip('"'))
    return arr

# return a random occupation from occupations.csv, weighted based off percentages
def rand_occupation(arr):
    total = 0.0
    print arr
    for i in arr[1::2]:
        total += float(i)
    rand = int(random.random() * total)
    for i in range(1,len(arr),2):
        rand -= float(arr[i])
        if rand < 0:
            return arr[i - 1] + ", " + arr[i]


if __name__ == "__main__":
    app.debug = True
    app.run()
