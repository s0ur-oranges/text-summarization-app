## Introduction
The project aims to use simple techniques in order to generate an automated summary of any particular text article.  The project uses TF-IDF vectorizer in order to rank the individual sentences in a document . It is a kind of extractive method for generating the summary , rather than an abstractive one. The deployed link on streamlit can be found here.

## Motivation of the project
In day-to-day conversations ,we often paraphrase what has been said by others . In many documents and research papers , we find an abstract at the very top . We can conclude that summaries are very useful and often times necessary . So in this project , I have tried to use NLP techniques to create an extractive summary of any text article.

## How to use the web-app?

Here is a sample text article inside the input :
```
yo

```
By clicking on summarise text , the summary is generated as follows (the sentences are printed alongwith the scores) 

```
yah

```



For your own purpose , replace the default text with your own in the input , and click again on summarise text button.

## Outline of the project
1) Split the text into individual sentences (using nltk.sent_tokenize)
2) Assign a score to each sentence based on the importance of that sentence in that document
3) Sort the sentences based on the scores assigned. Then display the top percentage of sentences.

## How do we determine the importance of a sentence in a document?

Each particular sentence in the document is considered as a ‘document’ for the TF-IDF. (To learn more about tf-idf , visit this link )
After the matrix is created  , we simply take the mean of the non-zero tf-idf values in that sentence(or row) to calculate the score.
Then  after the scores are generated , we have many choices :

1)display the top N sentences 
2) display the top X percentage of the sentences 
3)display every sentence that falls above a certain threshold (of the score)
For the sake of simplicity , this project employed the first method and displayed the top 5 sentences , since setting a threshold value can be tricky.

## Limitations :
1) The generated summary is extractive in nature , which sometimes works but sometime smay fail to give a reliable summary . It merely outputs the most important sentences in the document. 

2) The sentences in the output are not inorder. This poses problems when looking forward to summarise an article where order is important , like a story . But since my goal is mostly to display most relevant sentences and display the scores , it has been left as such. 

3) Since only sentences are extracted and presented , it may leave out crucial details.

## Challenges faced :-
1) Finding out which method to follow after scoring of the sentences have been done. Considering the simplest approach that will likely work for many articles , I decided to merely output the most relevant sentences . 
2) Deciding the method to score the sentences 
I decided to use the TF-IDF approach and the sentences which have higher non-zero tf-idf values are ranked higher than others.


