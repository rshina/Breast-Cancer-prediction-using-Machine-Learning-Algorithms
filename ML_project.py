import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import warnings
import pickle
warnings.filterwarnings("ignore")
from scipy.stats import skew
from sklearn.preprocessing import StandardScaler

from sklearn.feature_selection import SelectKBest,f_classif
from sklearn.preprocessing import LabelEncoder



#streamlit background settings
st.set_page_config(layout='wide')
st.title(":violet[Predicting Breast Cancer in a patient]")
tab1,tab2=st.tabs(["HOME","APPLICATION (PREDICT BREAST CANCER)"])
with tab1:
    st.text_area(":rainbow[ABOUT PROJECT]:","Breast cancer represents one of the diseases that make a high number of deaths every year. It is the most common type of all cancers and the main cause of women's deaths worldwide. Classification and data mining methods are an effective way to classify data.Especially in the medical field, where those methods are widely used in diagnosis and analysis to make decisions.So this is the project to make machine Learning model and  classify whether patient has cancer or not ")

    st.text_area(":rainbow[Tools Used For this Project]","Python,VSCODE ,Streamlit")

    st.text_area(":rainbow[Project created by]","ARSHINA.P,     contact:arshizig7@gmail.com")


with tab2:
    col1,col2=st.columns(2)
    
    
    
    
    with col1:
        texture_mean=st.number_input(":blue[ENTER TEXTURE_MEAN](Min: 16.17  & max: 21.8)")
        perimeter_mean=st.number_input(":blue[ENTER PERIMETER_MEAN](Min: 75.17  & max: 104.1)")
        smoothness_mean=st.number_input(":blue[ENTER SMOOTHNESS_MEAN](Min: 0.08637  & max: 0.1053)")
        compactness_mean=st.number_input(":blue[ENTER COMPACTNESS_MEAN](Min: 0.06492  & max: 0.1304)")
        concavity_mean=st.number_input(":blue[ENTER CONCAVITY_MEAN](Min: 0.02956  & max: 0.1307)")
        fractal_dimension_mean=st.number_input(":blue[ENTER FRACTAL DIAMENSION_MEAN](Min: 0.0577  & max: 0.06612)")
        texture_se=st.number_input(":blue[ENTER TEXTURE_SE](Min: 0.8339  & max: 1.474)")

    with col2:

        perimeter_se=st.number_input(":blue[ENTER PERIMETER_SE](Min: 1.606  & max: 3.357)")
        fractal_dimension_se=st.number_input(":blue[ENTER FRACTAL_DIMENSION_SE](Min: 0.002248  & max: 0.004558)")
        texture_worst=st.number_input(":blue[ENTER TEXTURE_WORST](Min: 21.08  & max: 29.72)")
        perimeter_worst=st.number_input(":blue[ENTER PERIMETER_WORST](Min: 84.11  & max: 125.4)")
        smoothness_worst=st.number_input(":blue[ENTER SMOOTHNESS_WORST](Min: 0.1166  & max: 0.146)")
        compactness_worst=st.number_input(":blue[ENTER COMPACTNESS_WORST](Min: 0.1472  & max: 0.3391)")
        concavity_worst=st.number_input(":blue[ENTER CONCAVITY_WORST](Min: 0.1145  & max: 0.3829)")

    
    data={"texture_mean":texture_mean,"perimeter_mean":perimeter_mean,"smoothness_mean":smoothness_mean,"compactness_mean":compactness_mean,"concavity_mean":concavity_mean,"fractal_dimension_mean":fractal_dimension_mean,"texture_se":texture_se,"perimeter_se":perimeter_se,"fractal_dimension_se":fractal_dimension_se,"texture_worst":texture_worst,"perimeter_worst":perimeter_worst,"smoothness_worst":smoothness_worst,"compactness_worst":compactness_worst,"concavity_worst":concavity_worst}
    dataframe=pd.DataFrame(data,index=[1])



    
    with open("classification_model.pk1","rb") as f_:
          Classi_model=pickle.load(f_)

    with open("classification_scale.pk1","rb") as f_1:
        classi_scale=pickle.load(f_1)

    

    new_df=classi_scale.transform(dataframe)
    prediction=Classi_model.predict(new_df)

    button=st.button(":violet[PREDICT BREAST CANCER]")
    if button:
        if prediction==1:
            st.write("### :red[Malignant: Patient has cancer and the cells have a harmful effect]")
        else:
            st.balloons()
            st.write("### :green[Benign: The cells are not harmful , There is no cancer]")
        

         

