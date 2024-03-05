import streamlit as st
import src.manage_data as cleaning
cleaning.load_dataframe()




st.write("Adventure time data")
st.dataframe(df)