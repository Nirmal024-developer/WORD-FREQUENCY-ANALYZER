from collections import Counter
import re

def analyze_text(text):
    # Treat words consistently and ignore most punctuation
    words = re.findall(r"\b[a-z0-9']+\b", text.lower())
    counts = Counter(words)
    return words, counts

def display_report(words, counts, top_n=4):
    total_words = len(words)
    unique_words = len(counts)
    most_frequent = counts.most_common(1)

    rows = counts.most_common(top_n)
    word_width = max(19, max((len(word) for word, _ in rows), default=4) + 2)
    count_width = 11
    inner_width = 33

    print("+" + "-" * inner_width + "+")
    print("|" + "TEXT ANALYZER".center(inner_width) + "|")
    print("+" + "-" * inner_width + "+")
    print(f"| {'Total Words:':<17}{total_words:>14} |")
    print(f"| {'Unique Words:':<17}{unique_words:>14} |")

    if most_frequent:
        print(f"| {'Most Frequent:':<17}{most_frequent[0][0]:>14} |")
        print(f"| {'Frequency:':<17}{most_frequent[0][1]:>14} |")
    else:
        print(f"| {'Most Frequent:':<17}{'N/A':>14} |")
        print(f"| {'Frequency:':<17}{0:>14} |")

    print("+" + "-" * inner_width + "+")
    print(f"| {'WORD':<{word_width}} {'FREQUENCY':>11} |")
    print("+" + "-" * inner_width + "+")

    for word, count in rows:
        print(f"| {word:<{word_width}} {count:>11} |")

    print("+" + "-" * inner_width + "+")

def main():
    print("Enter or paste your text below.")
    text = input("> ")

    words, counts = analyze_text(text)
    display_report(words, counts)

if __name__ == "__main__":
    main()
