from typing import List, Dict
import tiktoken

# Choose the model you will use (for token counting)
MODEL = "gpt-3.5-turbo"
MAX_TOKENS = 1000  # max tokens per chunk (adjust later)


def count_tokens(text: str) -> int:
    """Estimate tokens using tiktoken."""
    enc = tiktoken.encoding_for_model(MODEL)
    return len(enc.encode(text))


def chunk_pages(pages: List[Dict], max_tokens: int = MAX_TOKENS) -> List[Dict]:
    """
    Merge pages into token-safe chunks.
    
    pages: [
        {"page": 1, "text": "..."},
        {"page": 2, "text": "..."}
    ]
    
    Returns: [
        {"pages": [1,2], "text": "..."},
        {"pages": [3,4], "text": "..."}
    ]
    """
    chunks = []
    current_chunk = []
    current_pages = []
    current_tokens = 0

    for page in pages:
        page_tokens = count_tokens(page["text"])

        # If adding this page exceeds limit, save current chunk
        if current_tokens + page_tokens > max_tokens:
            if current_chunk:
                chunks.append({
                    "pages": current_pages,
                    "text": "\n".join(current_chunk)
                })
            # start new chunk
            current_chunk = [page["text"]]
            current_pages = [page["page"]]
            current_tokens = page_tokens
        else:
            current_chunk.append(page["text"])
            current_pages.append(page["page"])
            current_tokens += page_tokens

    # add last chunk
    if current_chunk:
        chunks.append({
            "pages": current_pages,
            "text": "\n".join(current_chunk)
        })

    return chunks