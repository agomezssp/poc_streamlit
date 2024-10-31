import streamlit as st
from boto3 import Session, client
from deltalake import DeltaTable
from datetime import datetime
from json import dumps, loads
from time import sleep
import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.randint(0,100, size=(100,4)))

st.line_chart(df)

aws_session = Session(
    aws_access_key_id = st.secrets.default.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=st.secrets.default.AWS_SECRET_ACCESS_KEY,
    region_name="us-west-2"
)

                  
