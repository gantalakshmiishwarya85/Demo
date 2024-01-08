import streamlit as st
st.set_page_config(page_title='Dogs')
st.header("Types of Dogs")
col1,col2=st.columns(2)
with col1:
  st.subheader("American")
  st.image("./American.jpeg",caption="American Dog",width=100,use_column_width=True)
  st.write("American dogs are lovely")
  with col2:
  st.subheader("Pomerian Dog")
  st.image("./Pomerian.jpeg",caption="Pomerian Dog",width=100,use_column_width=True)
  st.write("Pomerian Dogs are cute")
