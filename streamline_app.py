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
    region_name=st.secrets.default.AWS_DEFAULT_REGION
)

def load_data(): 
    table = DeltaTable(
        table_uri="s3://",
        storage_options = { 
            "AWS_ACCESS_KEY_ID": st.secrets.default.AWS_ACCESS_KEY_ID,
            "AWS_SECRET_ACCESS_KEY": st.secrets.default.AWS_SECRET_ACCESS_KEY,
            "REGION" :st.secrets.default.AWS_DEFAULT_REGION
        }
    )
    versions = [str(item.get("readVersion", -1) + 1) + " - " + datetime.fromtimestamp(item.get()) for item in table]
    versions[-1] = str(table.version()) + " - Lastest"
    return table, versions


    
