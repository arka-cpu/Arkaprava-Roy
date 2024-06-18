from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My First Webpage",page_icon=":cityscape_at_dusk:",layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
def local_css(style.css):
    with open(style.css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")
lottie_coding=load_lottieurl("https://lottie.host/2b0613fd-45e5-44c3-997b-803825927a32/OzbOsRiVZh.json")
img_a = Image.open("images/swami-vivekanand-1024x768.png")
img_b = Image.open("images/New-Doc-09-19-2023-11.34_47-1-scaled.png")
img_c = Image.open("images/unnamed.png")
with st.container():
    st.subheader("Developed by Arkaprava Roy")
    st.title("Swami Vivekananda")
    st.write("Vivekananda (born January 12, 1863, Calcutta [now Kolkata]—died July 4, 1902, near Calcutta) was a Hindu spiritual leader and reformer in India who attempted to combine Indian spirituality with Western material progress, maintaining that the two supplemented and complemented one another. His Absolute was a person’s own higher self; to labour for the benefit of humanity was the noblest endeavour.")
    st.write("[Learn More>](https://www.britannica.com/biography/Vivekananda)")
with st.container():
    st.title("Sri Ramakrishna")
    st.write("Ramakrishna was born on 18 February 1836, in the village of Kamarpukur, in the Hooghly district of West Bengal, India, in a very poor and pious Bengali Brahmin family. He was the fourth and the youngest child of his parents, father Khudiram Chattopadhyaya, born in 1775, and mother Chandramani Devi, born in 1791. The couples first son Ramkumar is said to have born in 1805, a daughter Katyayani five years later, and a second son Rameswar in 1826.")
    st.write("[Learn More>](https://en.wikipedia.org/wiki/Ramakrishna)")
with st.container():
    st.title("Srimati Sarada Devi")
    st.write("Sri Sarada Devi was born in Jayrambati, a village in present-day Bankura District in the state of West Bengal, India. She was married to Ramakrishna in 1859[citation needed] when she was only six years old and Ramakrishna was 23 years old, but remained with her family until she was 18, when she joined Ramakrishna at Dakshineswar Kali temple.")
    st.write("[Learn More>](https://en.wikipedia.org/wiki/Sarada_Devi)")
with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)
    with left_column:
        st.header("Famous Quotes by Swami Vivekananda")
        st.write("##")
        st.write(
            
            "Take up one idea. Make that one idea your life – think of it, dream of it, live on"
            "that idea. Let the brain, muscles, nerves, every part of your body, be full of that"
            "idea, and just leave every other idea alone. This is the way to success."
                        
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


with st.container():
    st.write("---")
    st.header("Some life Histories")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_a) 

    with text_column:
        st.subheader("Swami Vivekananda: The Power and the Glory")
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=qnybonnOBv0)")
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_b) 

    with text_column:
        st.subheader("Life History of Sri Ramakrishna")
        st.markdown("[PART-1 Watch Video...](https://www.youtube.com/watch?v=e5bG-X1yTgU)")
        st.markdown("[PART-2 Watch Video...](https://www.youtube.com/watch?v=YraziymNAzM)")
        st.markdown("[PART-3 Watch Video...](https://www.youtube.com/watch?v=eLaqnrFtaX0)")
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_c) 

    with text_column:
        st.subheader("Life and Teachings of Holy Mother Sarada Devi")
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=WSnwWLfDAzE)")
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        contact_form="""
        <form action="https://formsubmit.co/antaraduttaroy11@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="Your name" required>
             <input type="email" name="email" placeholder="Your email" required>
             <textarea name="message" placeholder="You message here" required></textarea>
             <button type="submit">Send</button>
        </form>
        """
        left_column, right_column=st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()

            

      
