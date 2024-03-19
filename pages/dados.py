import streamlit as st
import pandas as pd
import numpy as np
import cadastro as cd

df = pd.DataFrame(columns=(cd.nomes))

st.dataframe(df)  