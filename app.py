import streamlit as st
from soap_chain import generate_soap_note


st.set_page_config(page_title="SOAP Note Generator", page_icon="🩺", layout="wide")

st.title("🩺 SOAP Note Generator")
st.write("Turn raw clinical encounter notes into a structured SOAP note.")

with st.sidebar:
    st.header("About")
    st.write(
        "Generates **S**ubjective, **O**bjective, **A**ssessment, and **P**lan "
        "sections from free-text notes."
    )
    temperature = st.slider("Creativity", 0.0, 1.0, 0.3, 0.1)
    st.caption("Draft for clinician review — not medical advice.")


input_col, output_col = st.columns(2)

with input_col:
    st.subheader("Encounter notes")
    encounter = st.text_area(
        "Notes",
        height=300,
        label_visibility="collapsed",
        placeholder="e.g. 45 y/o male, chest pain 2 days, BP 150/95...",
    )
    generate = st.button("Generate SOAP Note", type="primary")

with output_col:
    st.subheader("Generated note")
    if generate and encounter.strip():
        with st.spinner("Generating..."):
            note = generate_soap_note(encounter,temperature)
        st.markdown(note)
        st.download_button("Download", note, file_name="soap_note.txt")
    elif generate:
        st.warning("Please enter some notes first.")
    else:
        st.info("Your SOAP note will appear here.")
