"""# Vectorizer"""

import prg_globales as glb

document = ["One Geek helps Two Geeks",
            "Two Geeks help Four Geeks",
            "Each Geek helps many other Geeks at GeeksforGeeks"]
  
# Create a Vectorizer Object
vectorizer = CountVectorizer()
  
vectorizer.fit(document)
  
# Printing the identified Unique words along with their indices
print("Vocabulary: ", vectorizer.vocabulary_)
  
# Encode the Document
vector = vectorizer.transform(document)
nombres_columnas = vectorizer.vocabulary_
  
# Summarizing the Encoded Texts
print("Encoded Document is:")
print(vector.toarray())

vectorizer = CountVectorizer()

print (glb.tweets_pd.shape)
vectorizer.fit(glb.tweets_pd["Texto_tweet"])
  
# Printing the identified Unique words along with their indices
print("Vocabulary: ", vectorizer.vocabulary_)
  
# Encode the Document
vector = vectorizer.transform(glb.tweets_pd["Texto_tweet"])
nombres_columnas = vectorizer.vocabulary_
print (glb.tweets_pd.shape)

# Summarizing the Encoded Texts
print("Vector X de palabras:")
print(vector.toarray())
print (vector.shape)
# print(vector[:4287])

from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(vector)
X_train_tfidf.shape

# TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pandas as pd

# set of documentstrain = ['The sky is blue.','The sun is bright.']
test = ['The sun in the sky is bright', 'We can see the shining sun, the bright sun.']

# instantiate the vectorizer objectcountvectorizer = CountVectorizer(analyzer= 'word', stop_words='english')

tfidfvectorizer = TfidfVectorizer(analyzer='word',stop_words= 'english')

# convert th documents into a matrixcount_wm = countvectorizer.fit_transform(train)
tfidf_wm = tfidfvectorizer.fit_transform(test)

'''#retrieve the terms found in the corpora
# if we take same parameters on both Classes(CountVectorizer and TfidfVectorizer) , it will give same output of get_feature_names() methods)#count_tokens = tfidfvectorizer.get_feature_names() # no difference
count_tokens = countvectorizer.get_feature_names()
tfidf_tokens = tfidfvectorizer.get_feature_names()
df_countvect = pd.DataFrame(data = count_wm.toarray(),index = ['Doc1','Doc2'],columns = count_tokens)
df_tfidfvect = pd.DataFrame(data = tfidf_wm.toarray(),index = ['Doc1','Doc2'],columns = tfidf_tokens)
print("Count Vectorizer\n")
print(df_countvect)
print("\nTD-IDF Vectorizer\n")
print(df_tfidfvect)'''