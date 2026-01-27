def vowels(text: str):
    chars = "aeiou"
    if not text:
        return 0
    return (1 if text.lower()[0] in chars else 0) + vowels(text[1:])