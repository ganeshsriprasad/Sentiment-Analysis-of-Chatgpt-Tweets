from PIL import Image
import numpy as np
import pickle
import base64
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder

# Load the trained model and CountVectorizer object
loaded_model = pickle.load(open('C:/Users/Ganesh.Sri/Downloads/trained_model.sav', 'rb'))

cv = pickle.load(open('C:/Users/Ganesh.Sri/Downloads/senti/countvectorizer.sav', 'rb'))

# Fit the label encoder on the training labels used to train the model
le = pickle.load(open('C:/Users/Ganesh.Sri/Downloads/senti/labelencoder.sav', 'rb'))

def Sentiment_Analysis(input_data):

 #input_data_cv = cv.transform([input_data])
 input_data_cv = cv.transform([str(input_data)])


# Predict the label using the logistic regression model
 predicted_label = loaded_model.predict(input_data_cv)[0]

# Convert the predicted label back to its original string representation using the label encoder
 predicted_label_str = le.inverse_transform([predicted_label])[0]

 #print("Predicted label:", predicted_label_str)
 return predicted_label_str

def main():
    
              
    st.title('Sentiment analysis of chatgpt')   
    
    # getting the input data from the user
    data = st.text_input('Enter the text to analyze')
    
    
    
    # code for Prediction
    sentiment_analysis = ''
    
    # creating a button for Prediction
    
    if st.button('sentiment Test Result'):
        sentiment_analysis = Sentiment_Analysis([data])
        #st.write("Prediction",sentiment_analysis.predicted_label_str)
        
        
    st.success(sentiment_analysis)
   

    
    
    
    
    
if __name__ == '__main__':
    main()
