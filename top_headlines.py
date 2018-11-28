from flask import Flask, render_template
import requests
from secrets import apikey
import json

app = Flask(__name__)

@app.route('/')
def index():
	return "<h1>Welcome!</h1>"

@app.route('/user/<nm>')
def user_name(nm):
	section = "Technology"
	headlines = get_headlines(section)
	return render_template('user.html', name=nm, headlines=headlines, section=section)

@app.route('/user/<nm>/<sec>')
def ec_1(nm, sec):
	section = sec.capitalize()
	headlines = get_headlines(section)
	return render_template('user.html', name=nm, headlines=headlines, section=section)

def get_headlines(section):
	r_format = "json"
	baseurl = "https://api.nytimes.com/svc/mostpopular/v2/mostviewed/{}/7.{}".format(section, r_format) #mostpopular API
	#baseurl = "https://api.nytimes.com/svc/topstories/v2/{}.{}".format(section, r_format) #topstories API (not working--"access denied"?)
	params = {"api-key":apikey}

	r = requests.get(baseurl, params)
	print(r.url)
	f = open('out.txt', 'w')
	f.write(r.text)
	f.close()
	json_data = json.loads(r.text)

	results = json_data["results"]

	headlines = []
	for item in results[:5]:
		headlines.append("{} ({})".format(item["title"], item["url"]))

	return headlines

if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)