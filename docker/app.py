from flask import Flask, request, render_template
from redis import Redis, RedisError, StrictRedis
import numpy as np
import joblib

model = joblib.load('ML-Model.pkl')

app = Flask(__name__)

def test_text(text):
	if text=='':
		return ''
	result = model.predict([text])
	pos = np.where(result[1][0] == np.amax(result[1][0]))
	pos = int(pos[0])
	sentiment_dict = {0:'Positive',1:'Negative',2:'Neutral'}
	respone = "Result: "+sentiment_dict[pos]
	return respone

@app.route('/', methods=['GET', 'POST'])
def index():
	text=''
	result=''
	if request.method == 'POST':
		text = request.form['text']
		result = test_text(text)
		return render_template('index.html',text=text,result=result)
	return render_template('index.html',text=text,result=result)

if __name__ == '__main__':
	redis_client = StrictRedis(host='redis', port=6379)
	app.run(host='0.0.0.0')
	
	
	
	
	