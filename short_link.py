import streamlit as st
import requests

st.title("🔗 Short Link Generator")

url = st.text_input("Enter the URL to shorten:")

if st.button("Shorten URL", type="primary"):

    if url:

        try:
            api_url = f"https://tinyurl.com/api-create.php?url={url}"

            response = requests.get(api_url)

            if response.status_code == 200:
                short_url = response.text

                st.success("Short URL generated successfully!")

                st.code(short_url)

            else:
                st.error("Failed to generate short URL")

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter URL first")

# Run Program
# streamlit run short_link.py
