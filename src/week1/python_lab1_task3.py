"""
Task 3 🟡 Function with Combined Logic
----------------------------------------
Write a function `analyze_sentence(text)` that returns:
1. total character count (len)
2. word count (split)
3. whether it contains the word "Python" (case-insensitive)
Return results as a tuple and print summary in main.
"""

def analyze_sentence(text):
    """Return length, word count, and whether 'Python' appears in text."""
    # TODO: implement function logic
    char_total = len(text)
    words_total = len(text.split())
    found_python = "python" in text.lower()
    return (char_total, words_total, found_python)

if __name__ == "__main__":
    # TODO: read sentence from input, call function, and print results
    sentence = input("Write a sentence: ")
    chars, words, contains = analyze_sentence(sentence)
    print(f"Characters: {chars}")
    print(f"Words: {words}")
    print(f"Has Python?: {'Yes' if contains else 'No'}")
