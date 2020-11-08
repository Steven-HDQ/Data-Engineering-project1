from flask import Flask, request, render_template , jsonify
from redis import Redis, RedisError, StrictRedis
import json

app = Flask(__name__)

def test_text(text):
	respone = "success"
	if text=='':
		return ''
	elif 'like' in text:
		respone = "Result: Positive"
	elif 'hate' in text:
		respone = "Result: Negative"
	else:
		respone = "Result: Neutral"
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
	
	
	
	
	