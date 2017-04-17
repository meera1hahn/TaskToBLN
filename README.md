# Steps to use!!!

## Download my code
```
git clone https://github.com/meera1hahn/.git
```

## Install NLTK
Install NLTK: ```sudo pip install -U nltk```   
Install Numpy (optional): ```sudo pip install -U numpy```   
Test installation: run python then type import nltk   

## Download Standford parser jars
``` 
wget http://nlp.stanford.edu/software/stanford-corenlp-full-2016-10-31.zip
```
Then you need to change line 4 and 5 of extract_queries.py to refect the path to where you downloaded the jars 

## Run

Simply run the extract_queries.py and send the sentence as a command line argument. For example: 
```
python extract_queries.py "where is the red cup"
```

