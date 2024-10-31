import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0,100, size=(100,4)))

st.line_chart(df)

                  
