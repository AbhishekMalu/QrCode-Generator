import qrcode
import streamlit as st
import time

st.set_page_config(layout="wide")

st.markdown("""
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """,unsafe_allow_html=True)

st.markdown("""
            <p style="text-align:center;font-weight:bold;font-size:280%; text-shadow: 1px 2px #FF0000">QR Code Generator</p>
            """,unsafe_allow_html=True)
st.markdown("""
                <div style="display:flex;justify-content:center;">
                    <img src="https://golangexample.com/content/images/2019/01/demo.gif"/>
                </div>
            """,unsafe_allow_html=True)

link = st.text_input("Enter the link:- ")
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill_color="#fabb1e", back_color="#57503e")

if st.button("Generate QRcode"):
    with st.container():
        left,center, right = st.columns(3)
        with center:
                time.sleep(3)
                img.save("QrCode.png")
                st.image("QrCode.png")
                time.sleep(3)
                st.download_button(label='Download the QrCode',
                        data= open('QrCode.png', 'rb').read(),
                        file_name='imagename.png',
                        mime='image/png')