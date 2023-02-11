# Spam Classifier Using Machine Learning
## Spam Classifier
This repository consists of files required for end to end implementation and deployment of Machine Learning Spam Classifier web application created with Streamlit and deployed on the Heroku platform.

## CountVectorizer:

The CountVectorizer provides a simple way to both tokenize a collection of text documents and build a vocabulary of known words, but also to encode new documents using that vocabulary.

## TF-IDF Vectorizer
Tf-idf is a method which gives us a numerical weightage of words which reflects how important the particular word is to a document in a corpus. A corpus is a collection of documents. Tf is Term frequency, and IDF is Inverse document frequency. This method is often used for information retrieval and text mining.

#### Term Frequency:

Term frequency is defined as the number of times a word (i) appears in a document (j) divided by the total number of words in the document.


![image](https://user-images.githubusercontent.com/93968656/141609082-c3dd68c0-5860-422d-a602-149d816cef66.png)


#### Inverse Document Frequency:

Inverse document frequency refers to the log of the total number of documents divided by the number of documents that contain the word. The logarithm is added to dampen the importance of a very high value of IDF.
log of idf

![image](https://user-images.githubusercontent.com/93968656/141609074-128b69bc-3e78-4b5c-b1e1-d57605c54350.png)


TFIDF is computed by multiplying the term frequency with the inverse document frequency.


![image](https://user-images.githubusercontent.com/93968656/141609069-1054a80d-1c3b-4514-9bf5-f1c7a1165eb4.png)



## Project Explanation
The Spam Classifier is a Streamlit web application which predicts if a message E-mail/SMS is a spam message or not. The dataset is available at Kaggle, and it's provided by UCI Machine Learning.

## Dataset used
Spam Classifier Dataset https://www.kaggle.com/uciml/sms-spam-collection-dataset

## Screenshot
##### Homepage
![homepage spam stream 1](https://user-images.githubusercontent.com/93968656/141608695-51413ac1-98d4-48c4-8b02-369789bd0fd7.png)

##### Spam Message
![spam message stream 3](https://user-images.githubusercontent.com/93968656/141608710-ba1bb844-66bb-49ef-998f-5f01faa88760.png)



##### ham Message (not spam)

![not spam message stream 2](https://user-images.githubusercontent.com/93968656/141608705-95d97de5-1dd8-4177-a513-925091c10b68.png)


## Tech Stacks
##### Programming Language : Python
##### WebFramework: Steamlit
##### Machine Learning Library: Numpy, Pandas, sklearn
##### NLP library: NLTK, CountVectorizer, TF-IDF Vectorizer

## Deployement on Amazon AWS

##### Login or signup in order to create virtual app. You can either connect your github profile to clone it or download any cli to manually deploy this project from local.
![image](https://user-images.githubusercontent.com/93968656/218245881-48d1ba34-6dcb-474d-9c9c-c3d75c338edf.png)


##### The next step would be to follow the instruction given in the AWS Documentation to deploy a web app.

## How to run the project on local system?
##### 1. Clone this repository in your local system.
##### 2. Open your IDE from your project directory and Install all the libraries mentioned in the requirements.txt file with the command pip install -r requirements.txt.
##### 3. Type command "streamlit run app.py" in the terminal to run the app.
##### 4. Go to your browser and type http://127.0.0.1:5000/ in the address bar.
##### Hurray! That's it.


## Link to the application
Check out the live demo: [Link](http://100.24.244.179:8501/)

## Also deployed using Streamlit
[Link](https://adilcr01-spam-classifier-streamlit-app-jgcodn.streamlit.app/)
