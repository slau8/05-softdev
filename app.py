'''
Shannon Lau and Eugene Thomas
SoftDev1 Period 7
HW #05: Jinja Tuning ...
2017-09-26
'''

from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

# landing page
@app.route("/")
def hello_world():
    # routes automatically to run occupation() for '/occupations' route
    return redirect(url_for('occupation'))

# occupation page
# render template according to occupations.csv
@app.route('/occupations')
def occupation():
    return render_template('occupations.html',
                            occupations = make_occupations(),
                            rand_occupation = rand_occupation(make_occupations()))

# return a dict of all occupations and corresponding percentages
def make_occupations():
    # convert file into an array of each line from occupations.csv
    try:
        lines = open('data/occupations.csv').read().splitlines()[1:-1]
    except:
        return {}
    # initialize dict
    # occupation : percentage
    dic = {}
    # separate occupation and percent to add to dict
    for i in lines:
        pair = i.rsplit(',',1)
        dic[pair[0].strip('"')] = pair[1]
    return dic

# return a random occupation from occupations.csv, weighted based off percentages
def rand_occupation(dic):
    # calculate total percentage
    total = 0.0
    for i in dic:
        total += float(dic[i])
    # generate random integer in [0,total)
    rand = int(random.random() * total)
    # subtract dict values from rand until less than 0
    for i in dic:
        rand -= float(dic[i])
        if rand < 0:
            return i + ", " + dic[i]

if __name__ == "__main__":
    app.debug = True
    app.run()
