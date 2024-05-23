import streamlit as st
import pandas as pd
import numpy as np
st.markdown("""
# markdown 1
## markdown 2
""",True)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.scatter_chart(chart_data)
st.file_uploader('masukan file',type='csv')

