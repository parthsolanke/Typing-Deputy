from string import Template

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
OLLAMA_CONFIG = {
    "model": "mistral",
    "keep_alive": "5m",
    "stream": False,
}

PROMPT_TEMPLATE = Template(
    """Fix all typos and casing and punctuation in this text, but preserve all new line characters:

$text

Return only the corrected text, don't include a preamble.
"""
)

def generate_corrected_text(text):
    """
    Generate corrected text by fixing typos, casing, and punctuation in the given text.

    Args:
        text (str): The input text to be corrected.

    Returns:
        str: The corrected text without any typos, casing, or punctuation errors.
    """
    return PROMPT_TEMPLATE.substitute(text=text)
