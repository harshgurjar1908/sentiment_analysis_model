# This code is importing various libraries and modules that are required for the Flask web
# application.
from flask import Flask, jsonify, request, render_template, flash, url_for
import re 
import h5py
import numpy as np
import pandas as pd
import re
import tensorflow as tf
from numpy import array
from keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model



# `app=Flask(__name__)` creates an instance of the Flask class and assigns it to the variable `app`.
# The `__name__` argument is a special Python variable that represents the name of the current module.
# By passing `__name__` as an argument, Flask knows where to find the resources (templates, static
# files, etc.) associated with the application.
app=Flask(__name__)

def init():
    # The code `global model,graph` is declaring the variables `model` and `graph` as global
    # variables. This means that these variables can be accessed and modified from anywhere in the
    # code.
    global model,graph
    model=load_model('model.h5')
    graph=tf.compat.v1.reset_default_graph()

# The `stop_word` list contains common words that are often considered insignificant or irrelevant in
# natural language processing tasks, such as sentiment analysis. These words are typically removed
# from the text before analysis to improve the accuracy and efficiency of the analysis. In this code,
# the `stop_word` list is used to filter out these words from the input text before performing
# sentiment analysis.
stop_word=["i","me","my","myself","we","our","ours","ourselves","you","yours","your","yourselves","yourself","he","him","his","himself","she","her","hers","herself","it","its","itself","they","them","their","theirs","themselves","what","which","who","whome","this","that","these","those","am","is","are","was","were","be","been","being","have","has","had","having","do","does","did","doing","an","a","the","and","but","if","or","because","as","until","while","of","at","by","for","with","about","against","between","into","through","during","before","after","above","below","to","from","up","down","on","off","in","out","over","under","again","further","then","once","here","there","when","where","why","how","all","any","both","each","few","more","most","other","some","such","no","nor","not","only"  ,"own"   ,"same"  ,"so"  ,"than" ,"too", "very","yes","t","can","will","just","don","should","now"]

# `@app.route('/', methods=['GET','POST'])` is a decorator in Flask that associates a URL route with a
# function. In this case, it associates the root URL ("/") with the `home()` function.

# The line `return render_template('home.html')` is returning the rendered HTML template called
# "home.html" to the client. This template is used to display the home page of the web application.

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html')

def clean(text):
    # This code snippet is a function called `clean()` that takes in a text as input and performs
    # several cleaning operations on it.
    text1=text+"" 
    sentiment=''
    strip_special_chars=re.compile("[^A-Za-z0-9]+")
    text=text.lower().replace("<br/>"," ")
    text=re.sub(strip_special_chars, " ", text.lower())
    text=text.strip()
    words1=text.split(" ")
    words=[]
    for word in words1:
        if word not in stop_word:
            words.append(word)
    return words

def analyze_text(text):
    # The code snippet is a function called `analyze_text()` that takes in a text as input and
    # performs sentiment analysis on it.
    words=clean(text)
    max_review_length=500
    word_to_id=imdb.get_word_index()
    x_text=[[word_to_id[word] if (word in word_to_id and word_to_id[word]<=200000) else 0 for word in words]]
    print(x_text)
    x_text=sequence.pad_sequences(x_text,max_review_length)
    vector=np.array([x_text.flatten()])
    probability=model.predict(array([vector[0]]))[0][0]
    class1=(model.predict(array([vector[0]]))>0.5).astype("int32")[0][0]
    if class1==0:
        sentiment='Negative'
    else:
        sentiment='Positive'
    
    return (sentiment,probability)

@app.route('/result',methods=['POST'])
def result():
# This code snippet is a function called `result()` that is executed when a POST request is made to
# the '/result' URL route.
    text=""
    if request.method=='POST':
        text=request.form["s"]
    sentiment,probability=analyze_text(text)
    probability=round(probability*100,2)
    return render_template('result.html',x='{}'.format(text),y='{}'.format(sentiment),z='{}'.format(probability))

# The code `if (__name__=="__main__"): init() app.run(debug=True)` is used to start the Flask web
# application.

if (__name__=="__main__"):
    init()
    app.run(debug=True)