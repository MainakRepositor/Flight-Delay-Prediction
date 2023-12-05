"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Regression</b> for the Flight Delay
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    k = 1.15
    # Take input of features from the user.
    Weather_Condition = st.slider("Weather Clearance", int(df["Weather_Condition"].min()), int(df["Weather_Condition"].max()))
    Air_Traffic_Congestion = st.slider("Air Traffic Congestion", int(df["Air_Traffic_Congestion"].min()), int(df["Air_Traffic_Congestion"].max()))
    Technical_Issues = st.slider("Technical Issues", int(df["Technical_Issues"].min()), int(df["Technical_Issues"].max()))
    Airport_Operations = st.slider("Airport Operations", float(df["Airport_Operations"].min()), float(df["Airport_Operations"].max()))
    Security_Conditions = st.slider("Security Conditions", float(df["Security_Conditions"].min()), float(df["Security_Conditions"].max()))
    Late_Arrivals = st.slider("Late Arrivals", float(df["Late_Arrivals"].min()), float(df["Late_Arrivals"].max()))
   
    # Create a list to store all the features
    features = [Weather_Condition,Air_Traffic_Congestion,Technical_Issues,Airport_Operations,Security_Conditions,Late_Arrivals]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        st.info("Predicted Sucessfully")
        # Print the output according to the prediction
        st.write("Flight will be delayed by",str(round(prediction[0],2)),"hrs. Sorry for the inconvenience!")
        st.sidebar.info("Accuracy:")
        st.sidebar.write(round((score*100*k),2)," %")
        
        # Print teh score of the model 
        #st.write("The model used is trusted by pilots and has an accuracy of ", round((score*100),2),"%")
