import numpy as np
import pandas as pd
import yaml

import streamlit as st

st.title('Lunge Cancer Detection And Prediction ')
st.markdown('by Aparna Muratkar')
st.write("Cancer is a disease in which cells in the body grow out of control. When cancer starts in the lungs,"
         " it is called lung cancer. Lung cancer begins in the lungs and may spread to lymph nodes or other organs "
         "in the body, such as the brain. Cancer from other organs also may spread to the lungs. When cancer cells "
         "spread from one organ to another, they are called metastases.")
st.markdown('<img width="500" src="../images/lung.jpg">',unsafe_allow_html=True)

with open('../params.yaml') as file:
	config = yaml.safe_load(file)
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:images/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

st.write("")
st.markdown('''Lung''')



name = st.text_input("Enter your Name?")
age = st.text_input("Enter your Age")
