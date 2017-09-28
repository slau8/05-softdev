'''
Shannon Lau and Eugene Thomas
SoftDev1 Period 7
HW #05: Jinja Tuning ...
2017-09-26
'''

from util import occupations
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
                            collections = occupations.make_occupations(),
                            rand_occupation = occupations.rand_occupation(occupations.make_occupations()))

if __name__ == "__main__":
    app.debug = True
    app.run()
