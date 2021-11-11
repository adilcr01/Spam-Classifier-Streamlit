import streamlit as st
import re
from nltk.stem import PorterStemmer
import pickle
nltk.download("stopwords")
import nltk
from nltk.corpus import stopwords


ps = PorterStemmer()


def convert(sentences):
    corpus=[]
    for i in range(len(sentences)):
        review=re.sub('[^A-Za-z0-9]+',' ',sentences[i])
        review=review.lower()
        review=review.split()
        review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
        review= ' '.join(review)
        corpus.append(review)
    return corpus


tfidf=pickle.load(open('vectorizer.pkl','rb'))

model=pickle.load(open('model.pkl','rb'))


st.title("Email/SMS Spam Classifier")

# 0.Get the input from html page
input_sms = st.text_area('Enter your message')

if st.button('Predict'):


    # 1.Preprocess the input
    converted_sentence = convert([input_sms])
    # 2.Vectorize the preprocessed input
    vectorized_sms = tfidf.transform(converted_sentence).toarray()
    # 3.Model
    prediction = model.predict(vectorized_sms)[0]
    # 4.Display Result

    if prediction == 0:
        st.header("Not Spam")
    else:
        st.header("Spam")


