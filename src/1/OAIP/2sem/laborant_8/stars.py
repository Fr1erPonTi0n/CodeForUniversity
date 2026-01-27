def stars(text: str):
    words = text.split()
    return "\n".join(list(map(lambda word: "*" * (max(map(len, words)) - len(word)) + word, words)))
