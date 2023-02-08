import streamlit as st
import pandas


data = {
    'Series_1': [1, 3, 4, 5, 7],
    'Series_2': [10, 30, 40, 100, 250]
}

df = pandas.DataFrame(data)

st.title("Our First Streamlit App")
st.subheader("Introducing Streamlit in automate Everythin with Python")
st.write("""This is our fisrt web app.
Enjoy it!
""")

st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider('Celsius')
st.write(myslider, 'in Farenheit is', myslider * 9/5 + 32)

#To run this program run this in the terminal: 
# streamlit run Automate_Everything_with_PY\s8_ModernPythonTools\s8e67_CreateAndPublishWebAppsAndDataDashboardsWithStreamlit.py