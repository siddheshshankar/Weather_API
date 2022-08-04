import streamlit as st


class WebApp:

    def title(self):
        ln_url = "https://www.linkedin.com/in/siddheshshankar94/"

        st.markdown(f"""<style>
                             .stApp {{
                                         background-image: url("https://wallpaperaccess.com/full/5227230.png");
                                         background-attachment: fixed;
                                         background-size: cover
                                    }}
                        </style>""", unsafe_allow_html=True)

        st.markdown("""<h1 style='text-align: center; margin-bottom: -35px;'>Weather Tracker</h1>""",
                    unsafe_allow_html=True)

        st.caption(f"""<p style='text-align: center'>by <a href={ln_url}>Siddhesh Shankar</a></p>""",
                   unsafe_allow_html=True)

        city = st.text_input('City')

        if city:
            return city
