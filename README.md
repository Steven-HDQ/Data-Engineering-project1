# <center>Sentiment Analysis</center>
<center>HAN Duqing & GAO Xin</center>

### Get Start
Note: This sentiment analysis application requires nothing but Docker installed no matter which operation system you work on.
- For  Windows user, you just need to double-click the run.bat.
- For  Linux / Mac user, you just need to run the run.sh.

Then everything is done and you can check on your web browser on localhost:5000.
Enjoy yourself !!!

### Machine Learning Model
##### Dataset: 
Twitter US Airline Sentiment
URL: https://www.kaggle.com/crowdflower/twitter-airline-sentiment

##### Model: 
Google’s strongest NLP model: BERT

BERT can be used in tasks such as question answering systems, sentiment analysis, spam filtering, named entity recognition, document clustering, etc., as the infrastructure or language model for these tasks.

Our model was trained on Google Colab.( Google Colaboratory is a research tool opened by Google, mainly used for the development and research of machine learning. Google Colab provides free GPU usage (GPU model is Tesla K80). We can easily run frameworks such as Keras, Tensorflow, Pytorch, etc. on it.)

##### Model Accuracy: 
The model has an accuracy rate of 83.5% ！

##### Save Model: 
We use joblib to save the model we have trained. The application just need to load the pre-trained model and do the sentiment analysis.

### Project Management
We use Trello to split and manage our job during this project.
URL: https://trello.com/b/Tfgcz83w/project-1