import numpy as np
import pickle 
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.preprocessing import LabelEncoder

# Load the trained model and CountVectorizer object
loaded_model = pickle.load(open('C:/Users/Ganesh.Sri/Downloads/trained_model.sav', 'rb'))
cv = pickle.load(open('C:/Users/Ganesh.Sri/Downloads/countvectorizer.sav', 'rb'))

# Fit the label encoder on the training labels used to train the model
le = pickle.load(open('C:/Users/Ganesh.Sri/Downloads/labelencoder.sav', 'rb'))

#le.fit(['Positive', 'Neutral', 'Negative'])

# Define a new sentence
new_sentence = "i love chatgpt"

# Transform the new sentence using the CountVectorizer object
new_sentence_cv = cv.transform([new_sentence])

# Predict the label using the logistic regression model
predicted_label = loaded_model.predict(new_sentence_cv)[0]

# Convert the predicted label back to its original string representation using the label encoder
predicted_label_str = le.inverse_transform([predicted_label])[0]

print("Predicted label:", predicted_label_str)
