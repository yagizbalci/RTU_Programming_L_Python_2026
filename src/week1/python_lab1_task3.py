def analyze_sentence(text: str) -> tuple[int, int, bool]:
    return len(text), len(text.split()), "python" in text.lower()

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    characters, words, contains_python = analyze_sentence(sentence)
    print(f"Characters: {characters}")
    print(f"Words: {words}")
    print(f"Contains 'Python': {contains_python}")
