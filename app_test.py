from flask import Flask, render_template, url_for, redirect, request, session
import pandas as pd
from scipy import sparse
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import re
import pickle



#filepath = '/content/drive/My Drive/magical/'
filepath = ''
clf_s1_pickle = filepath + 'clf_s1.pickle'
clf_s2_pickle = filepath + 'clf_s2.pickle'
clf_s3_pickle = filepath + 'clf_s3.pickle'
clf_s4_pickle = filepath + 'clf_s4.pickle'
vectorizer_pickle = filepath + 'vectorizer.pickle'

with open(clf_s1_pickle, mode="rb") as f:
    clf_s1 = pickle.load(f)
with open(clf_s2_pickle, mode="rb") as f:
    clf_s2 = pickle.load(f)
with open(clf_s3_pickle, mode="rb") as f:
    clf_s3 = pickle.load(f)
with open(clf_s4_pickle, mode="rb") as f:
    clf_s4 = pickle.load(f)
with open(vectorizer_pickle, mode="rb") as f:
    vectorizer = pickle.load(f)

app = Flask(__name__)

def make_prediction(test_season, input):
    test_review = input
    test_review = test_review.lower()
    test_review = re.sub('[^A-Za-z0-9]+', ' ', test_review)
    test_review = [test_review]
    X_test = vectorizer.transform(test_review).toarray()
    if test_season == 'Spring':
        prediction = clf_s1.predict(X_test)[0]
    elif test_season == 'Summer':
        prediction = clf_s2.predict(X_test)[0]
    elif test_season == 'Fall':
        prediction = clf_s3.predict(X_test)[0]
    else:
        prediction = clf_s4.predict(X_test)[0]
    #return df[df['hotel_name'] == prediction][['hotel_name', 'hotel_address']].head(1)
    return prediction

print('&&&&&&&&&&&&&&&&',make_prediction('Summer', 'beach resort'))

#### Initial Page ####
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title="Welcome Page")

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    error = ''
    if request.method == 'POST':
        input = request.form['input']
        print('$$$$$$$$$request', input)
        if len(input) == 0:
            # Form data failed validation; try again
            error = "Please input"
        else:
            test_season = 'Summer'
            result = make_prediction(test_season, input)
            print('@&&&&&&&&&&&&&&&&', result)
            #text = 'testtest'
            return render_template('prediction.html', text=result)
    return render_template('prediction.html', message=error)

#### Sign Up ####
@app.route('/signUp')
def signUp():
    return render_template('signUp.html', title="Sign up Page")



#### Sign In ####

@app.route('/signIn')
def signIn():
    return render_template('signIn.html', title="Sign In Page")



#### Payment Page
@app.route('/payment')
def payment():
    return render_template('payment.html', title='Payment Page')


if __name__ == '__main__':
    app.run(debug=True)


#### Sign Up ####



#### Sign In ####
