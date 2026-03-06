import streamlit as st
from emotion_model import detect_emotion
from encryption import encrypt_text, decrypt_text
from metadata import extract_metadata

st.title("Privacy Preserving Emotion AI")

st.write("Detect emotions while keeping messages encrypted")

text = st.text_area("Enter Message")

if st.button("Analyze"):

    emotion, confidence = detect_emotion(text)

    metadata = extract_metadata(text)

    encrypted = encrypt_text(text)

    st.subheader("Emotion Result")
    st.write("Emotion:", emotion)
    st.write("Confidence:", round(confidence,2))

    st.subheader("Emotion Metadata")
    st.write(metadata)

    st.subheader("Encrypted Message")
    st.code(encrypted)

    decrypted = decrypt_text(encrypted)

    st.subheader("Decrypted Message")
    st.write(decrypted)