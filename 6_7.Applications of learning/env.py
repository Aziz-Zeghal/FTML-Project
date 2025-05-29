"""Env file for common environment variables and functions."""

import re

DATA = "../data/"
SEED = 42
LABEL_MAPPING = {
    "0": "Safe Email",
    "1": "Phishing Email",
}


def preprocess(text: str) -> str:
    """Preprocess the input text. Some models do not require this step."""
    text = text.lower()
    text = re.sub(r"[\d\W_]+", " ", text)
    tokens = text.split()
    return " ".join(tokens)
