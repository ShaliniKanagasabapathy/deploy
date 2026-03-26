import streamlit as st
st.title("Nallathu nadakum. i will getinto AI/ML Project in Accenture")

st.title("My First Streamlit App")
st.write("Hello Shalini 👋")
st.header("header")
st.subheader("sub header")
st.text("text")
st.markdown("markdown")
st.caption("caption")
import pandas as pd
df=pd.DataFrame({"name":["a","b","c"],"mark":[12,14,16]})
st.write(df)
name=st.text_input("enter your name")
age=st.number_input("enter age",min_value=10,max_value=60)
rating=st.slider("Enter your rating",0,50,5)
colour=st.selectbox("select colour",["red","blue","green"])
st.write(colour)
if st.checkbox("show message"):
    st.write("hi how are you i like",colour)

ch=st.radio("pick one",["idly","dosa"])
