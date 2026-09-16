text = input()
words = text.lower().split()
counts = {}

for w in words:
    counts[w] = counts.get(w, 0) + 1

for word, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
    print(f"{word}: {count}")


print(f"Distinct words: {len(counts)}")