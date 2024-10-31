import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randit(0,100, shape=(4,100)))

st.line_chart(df)

                  
