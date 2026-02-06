import os
import json
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from summarization.prompts import EXECUTIVE_SUMMARY_PROMPT

load_dotenv(find_dotenv())

def generate_summary(text_content: str):
    client = OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=os.getenv("GROQ_API_KEY")
    )
    
    # We use 'gpt-4o' style logic but pointing to Groq's Llama model
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a professional analyst. Output valid JSON only."},
            {"role": "user", "content": EXECUTIVE_SUMMARY_PROMPT.format(text_content=text_content)}
        ],
        response_format={"type": "json_object"}
    )
    return json.loads(response.choices[0].message.content)