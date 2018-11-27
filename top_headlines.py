from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/user/<nm>')
def user_name(nm):

	return render_template('user.html', name=nm)

def get_headlines(section):

if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)