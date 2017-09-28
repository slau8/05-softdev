import random

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
    print dic
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

