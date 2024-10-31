import streamlit as st
from boto3 import Session, client
from deltalake import DeltaTable
from datetime import datetime
from json import dumps, loads
from time import sleep
import pandas as pd
import numpy as np


# df = pd.DataFrame(np.random.randint(0,100, size=(100,4)))
# st.line_chart(df)


def load_data(): 
    table = DeltaTable(
        table_uri="s3://cuponlub-ods-us-west-2-bucket-891377106068-dev/02_staging/tables/contacto/",
        storage_options = { 
            "AWS_ACCESS_KEY_ID": st.secrets.default.AWS_ACCESS_KEY_ID,
            "AWS_SECRET_ACCESS_KEY": st.secrets.default.AWS_SECRET_ACCESS_KEY,
            "REGION" :st.secrets.default.AWS_DEFAULT_REGION
        }
    )

    # versions = [str(item.get("readVersion", -1) + 1) + " - " + datetime.fromtimestamp(item.get()) for item in table.version()]
    # versions[-1] = str(table.version()) + " - Lastest"
    versions = []
    return table, versions



st.title("AWS Delta Lake Data")

delta_table_data, versions = load_data()

with st.sidebar:
      version = st.selectbox("Seleccione versión:", versions, len(versions) -1)

df = delta_table_data.to_pandas()
st.table(data= df)
    
