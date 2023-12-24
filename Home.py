import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="GSB", page_icon="16.png")

st.image("GSB Medium.png", width=120,)
st.title("Educational Dashboard System")
st.image("Power-Bi-Service.jpg", width=600,)


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


# Create a button that links to an external website
external_link = "https://laila-ai-gsb.streamlit.app/"  # Replace with the actual URL
if st.button("Chat with Laila AI"):
    st.image("Picture1.png", width=120,)       
    st.markdown(f"Redirecting to [{external_link}]({external_link})")
    # You can also use st.markdown to create a clickable link to the external website:
    # st.markdown(f"[Visit External Website]({external_link})")
