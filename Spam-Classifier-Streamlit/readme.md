# Spam Classifier Using Machine Learning
## Spam Classifier
This repository consists of files required for end to end implementation and deployment of Machine Learning Spam Classifier web application created with Streamlit and deployed on the Heroku platform.

## CountVectorizer:

The CountVectorizer provides a simple way to both tokenize a collection of text documents and build a vocabulary of known words, but also to encode new documents using that vocabulary.

## TF-IDF Vectorizer
Tf-idf is a method which gives us a numerical weightage of words which reflects how important the particular word is to a document in a corpus. A corpus is a collection of documents. Tf is Term frequency, and IDF is Inverse document frequency. This method is often used for information retrieval and text mining.

Tf(Term Frequency): Term frequency can be thought of as how often does a word ‘w’ occur in a document ‘d’. More importance is given to words frequently occurring in a document. The formula of Term frequency is:

IDF(inverse document frequency): Sometimes, words like ‘the’ occur a lot and do not give us vital information regarding the document. To minimize the weight of terms occurring very frequently by incorporating the weight of words rarely occurring in the document. In other words, idf is used to calculate rare words’ weight across all documents in corpus. Words rarely occurring in the corpus will have higher IDF values

![image](https://user-images.githubusercontent.com/93968656/141608992-a285afe1-beb0-4da1-8682-b2d7cdb1e853.png)


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
##### Machine Learning Library: Numpy, Pandas, sklearn, NLP


## Deployement on Heroku

##### Login or signup in order to create virtual app. You can either connect your github profile or download Heroku cli to manually deploy this project.
![image](https://user-images.githubusercontent.com/93968656/141474123-3dc0d678-af4b-4527-92af-17d05a5d0481.png)

##### The next step would be to follow the instruction given in the Heroku Documentation to deploy a web app.

## How to run the project on local system?
##### 1. Clone this repository in your local system.
##### 2. Open your IDE from your project directory and Install all the libraries mentioned in the requirements.txt file with the command pip install -r requirements.txt.
##### 3. Run the app.py file by clicking the run button.
##### 4. Go to your browser and type http://127.0.0.1:5000/ in the address bar.
##### Hurray! That's it.


## Link to the application
Check out the live demo: https://spam-classifier1.herokuapp.com/

##### Note: You might expect delay in loading the website as the webframework used is Streamlit.


