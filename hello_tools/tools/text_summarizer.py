"""
Text summarizer tool for condensing long text into shorter summaries.
"""

from agents import function_tool


@function_tool
def text_summarizer(text: str, max_length: int = 150) -> str:
    """
    Summarize a given text to a specified maximum length.
    
    Args:
        text: The text to be summarized.
        max_length: Maximum length of the summary in characters (default: 100).
        
    Returns:
        A summarized version of the input text.
    """
    if not text or not text.strip():
        return "Error: No text provided to summarize."
    
    # Clean the text
    text = text.strip()
    
    # If text is already shorter than max_length, return as is
    if len(text) <= max_length:
        return f"Summary: {text}"
    
    # Enhanced summarization with better sentence handling
    # In a real implementation, you might use more sophisticated NLP techniques
    sentences = text.split('. ')
    summary_sentences = []
    current_length = 0
    
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
            
        # Add period if sentence doesn't end with punctuation
        if not sentence.endswith(('.', '!', '?')):
            sentence += '.'
            
        if current_length + len(sentence) + 1 <= max_length - 3:  # -3 for "..."
            summary_sentences.append(sentence)
            current_length += len(sentence) + 1
        else:
            break
    
    summary = " ".join(summary_sentences)
    if len(summary) < len(text):
        summary = summary.rstrip('.') + "..."
    
    return f"📝 Summary ({len(summary)} chars): {summary}"
