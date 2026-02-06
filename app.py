import streamlit as st
import json
from pdf.extractor import extract_content
from summarization.summarizer import generate_summary

st.set_page_config(page_title="AI PDF Reader", layout="wide")
st.title("📄 Executive PDF Reader")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    # 1. Save & Extract
    with st.spinner("Reading PDF..."):
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        text = extract_content("temp.pdf")

    # 2. Summarize
    if st.button("Generate Executive Summary"):
        with st.spinner("AI is analyzing..."):
            summary_data = generate_summary(text)
            
            # Displaying Results
            st.header(summary_data['title'])
            st.info(summary_data['elevator_pitch'])
            
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("💡 Key Insights")
                for point in summary_data['key_insights']:
                    st.write(f"• {point}")
            with col2:
                st.subheader("🚀 Next Steps")
                for step in summary_data['next_steps']:
                    st.write(f"✅ {step}")
            
            # 3. Download Button
            json_string = json.dumps(summary_data, indent=2)
            st.download_button(
                label="📥 Download Summary (JSON)",
                data=json_string,
                file_name="summary.json",
                mime="application/json"
            )