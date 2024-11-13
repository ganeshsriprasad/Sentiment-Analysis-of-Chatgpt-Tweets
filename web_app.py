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
    ##PREDICTION USING LOGISTICREGRESSION
    # Add an image in the background
 
 #input_data_cv = cv.transform([input_data])
 input_data_cv = cv.transform([str(input_data)])


# Predict the label using the logistic regression model
 predicted_label = loaded_model.predict(input_data_cv)[0]

# Convert the predicted label back to its original string representation using the label encoder
 predicted_label_str = le.inverse_transform([predicted_label])[0]

 #print("Predicted label:", predicted_label_str)
 return predicted_label_str

def main():
    
    
    # giving a title
    st.markdown("""
    <style>
    h1 {
    color:white ;
    }
    .title {
        background-color: #ff8c00;
        color: white;
        padding: 0.5rem;
        border-radius: 0.5rem;
     }
    </style>
    """, unsafe_allow_html=True)
        
         
    st.title('Sentiment analysis of chatgpt')
    
     # Add an image
    #image = Image.open('C:/Users/Ganesh.Sri/Downloads/senti/images/1.webp')
    #st.image(image, caption='CHATGPT', use_column_width=True)
    
       # Add an image as background
   # @st.experimental_memo
    @st.cache_data()
    def get_img_as_base64(file):
     with open(file, "rb") as f:
        data = f.read()
     return base64.b64encode(data).decode()
 
    img = get_img_as_base64("images/2.png")
#https://images.nature.com/original/magazine-assets/d41586-023-00056-7/d41586-023-00056-7_23914466.jpg
#https://d1e00ek4ebabms.cloudfront.net/production/bf0b67cb-1e0e-41e9-b618-f4f6fe75f5d2.jpg
#https://www.shutterstock.com/image-photo/ai-tech-businessman-show-virtual-260nw-2253228203.jpg
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://img.freepik.com/free-photo/wide-angle-shot-single-tree-growing-clouded-sky-during-sunset-surrounded-by-grass_181624-22807.jpg");
    background-size: 98%;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: local;
    }}
    [data-testid="stSidebar"] > div:first-child {{
    background-image: url("data:image/png;base64,{img}");
    background-position: center; 
    background-repeat: no-repeat;
    background-attachment: fixed;
    }}
    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}
    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)
    #st.title("It's summer!")
    #st.sidebar.header("Configuration")

# Add a title and subtitle on top of the background images
    
    
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
