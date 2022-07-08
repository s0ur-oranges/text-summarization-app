#click on run all initially

#importing the necessary libraries

import pandas as pd
import numpy as np
import textwrap
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import time
import streamlit as st



nltk.download('punkt')
nltk.download('stopwords')

#creating a featurizer that will perform tf-idf
featurizer = TfidfVectorizer(
    stop_words=stopwords.words('english'),
    norm='l1',
)

def get_sentence_score(tfidf_row):
  # returning average of the non-zero values from the tf-idf vector representation of the sentences
  x = tfidf_row[tfidf_row != 0]
  return x.mean()

def wrap(x):
  return textwrap.fill(x, replace_whitespace=False, fix_sentence_endings=True)


# creating a summarizer function

def summarizer(text):
    sentences = nltk.sent_tokenize(text)  # sent_tokenize is being used to extract the individual sentences
    model = featurizer.fit_transform(sentences)  # performing tf-idf

    # now ,we will be computing the scores for each of the sentences and sort them later
    scores = np.zeros(len(sentences))
    for i in range(len(sentences)):
        score = get_sentence_score(model[i, :])
        scores[i] = score

    # sorting the scores obtained from above
    sort_data = np.argsort(-scores)
    sent=[]

    # printing the required summary. Note that the generated summary is just the sentences
    # which are determinded to be most important according to the scores
    for i in sort_data[:5]:
        sent.append(wrap("%.2f: %s" % (scores[i], sentences[i])))

    return sent




def progressbar():
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)


st.title('Article summarization App')
st.write('Performing article spinning')

# st.write('Enter some random tweets in the left sidebar and click on Predict Sentiment!')


# uploaded_file = st.sidebar.file_uploader("Choose a csv file", type="csv")
# st.sidebar.write("or")
st.sidebar.subheader("Enter a single paragraph : ")
text = st.sidebar.text_area("Enter in place of the default text..",
                              value="There are numerous benefits of recycling. Recycling helps recover resources that can be used to make use of them in a different way. New products can be made by recycling general Waste. Solid Wastes like wood, glass, plastic, electronic devices, clothing and leather items can be t decompose easily and can pile up as a landfill for many years, sometimes ending up in the ocean and killing animals who choke on them accidentally. The use of such products that are harmful to everyone should be Reduced. Alternative options have been developed to Reduce the use of plastic such as jute bags instead of polythene bags, paper straws and packaging to be used in place of those made of plastic are a few to name.",
                              height=500, max_chars=None, key=None)

if (st.sidebar.button('Summarize text')):
    progressbar()

    result=summarizer(text)

    for i in result:
        st.write(i)



