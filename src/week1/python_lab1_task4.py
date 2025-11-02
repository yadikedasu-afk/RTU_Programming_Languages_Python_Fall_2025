"""
Task 4 🟡 Text-based Arithmetic Analyzer
----------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""

def count_characters(text):
    """Count non-space characters in a string."""
    # TODO: implement
    cleaned = text.replace(" ", "")
    return len(cleaned)

def count_words(text):
    """Count number of words in a string."""
    # TODO: implement
    return len([w for w in text.split() if w != ""])

def extract_numbers(text):
    """Return list of integers found in text."""
    # TODO: implement
    nums = []
    for word in text.split():
        if word.isdigit():
            nums.append(int(word))
    return nums

def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    # TODO: call helper functions and compute total, average, etc.
    chars = count_characters(text)
    words = count_words(text)
    numbers = extract_numbers(text)
    total_sum = sum(numbers) if numbers else 0
    avg = (total_sum / len(numbers)) if numbers else 0
    return chars, words, total_sum, avg

if __name__ == "__main__":
    # TODO: read input, call analyze_text(), and print results
    txt = input("Enter your text: ")
    chars, words, total_sum, avg = analyze_text(txt)
    print(f"Characters (no spaces): {chars}")
    print(f"Words count: {words}")
    print(f"Sum of all numbers: {total_sum}")
    print(f"Average of numbers: {avg:.2f}")
