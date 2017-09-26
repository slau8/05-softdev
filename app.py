from flask import Flask, render_template #flask must be installed ( (venv)$pip install flask )

app = Flask(__name__) #create Flask object

@app.route("/") #assign following fxn to run in response to root route request
def hello_world():
    return "No hablo queso!"

def collection(): 
	try: 
		d = open(file_name).read().splitlines()[1:-1]
	except: 
		return "DNE" 
	arr = [] 
	for i in d: 
		l = i.rsplit(',') 
		for j in l: 
			arr.append(j.strip())

@app.route('/occupations') 
def occupation(): 
 
	
if __name__ == "__main__": #do not run if this file is imported as module
	app.run()
