# summarization/prompts.py

EXECUTIVE_SUMMARY_PROMPT = """
You are a world-class Chief of Staff. Summarize the following document for a busy executive.
Focus on high-level strategy, key numbers, and actionable next steps.
Ignore fluff. Be direct.

DOCUMENT CONTENT:
{text_content}
"""