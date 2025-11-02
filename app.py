import streamlit as st
import requests

# Page setup
st.set_page_config(page_title="HMRC Hello World", page_icon="👋")
st.title("👋 HMRC Sandbox API Test")
st.write("Calling `hello/world` endpoint (no authentication required).")

API_URL = "https://test-api.service.hmrc.gov.uk/hello/world"

if st.button("Call HMRC Hello World API"):
    try:
        response = requests.get(API_URL, headers={
            "Accept": "application/vnd.hmrc.1.0+json"
        })

        if response.status_code == 200:
            st.success("✅ Success!")
            st.json(response.json())
        else:
            st.error(f"Error {response.status_code}: {response.text}")

    except Exception as e:
        st.error(f"An error occurred: {e}")
