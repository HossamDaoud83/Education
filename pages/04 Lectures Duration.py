import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Lectures Duration", page_icon="16.png")
st.image("GSB Medium.png", width=120,)

st.title("Microsoft Teams Lectures Duration")
components.iframe("https://app.powerbi.com/view?r=eyJrIjoiZGI2OTc3Y2ItM2JjYS00MzZmLWI5YjUtOTY4OWIwODdkYjhiIiwidCI6ImE0NzRkYzY0LTQ1ZDEtNDNkOS05N2FjLWM4NWY0ZDMyZmUwMCIsImMiOjl9", width=800, height=600)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
