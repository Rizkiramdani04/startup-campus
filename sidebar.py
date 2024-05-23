import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


#sidebar select box
nilai=st.sidebar.selectbox('Navigasi Select',['Home','About','Contact Us'])
#sidebar multi select

#sidebar upload file
st.sidebar.file_uploader('Masukan FIle','csv')

if nilai== 'Home':
    st.header('Ini Vidio',divider='rainbow')
    st.video('https://www.youtube.com/watch?v=lVnSR3FS7h4&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=8')

if nilai=='About':
    gambar=Image.open('ipin.jpeg')
    st.image(gambar)


if nilai== 'Contact Us':
    st.header('Ini Vidie',divider='rainbow')
    st.video('https://www.youtube.com/watch?v=lVnSR3FS7h4&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=8')