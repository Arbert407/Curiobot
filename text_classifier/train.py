from textblob.classifiers import NaiveBayesClassifier
with open('data.json','r') as fp:
  classifier = NaiveBayesClassifier(fp, format="json") 

print(classifier.classify('Muestrame algo'))