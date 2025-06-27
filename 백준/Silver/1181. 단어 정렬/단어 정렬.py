N=int(input())
words=set()

for i in range(N):
    words.add(input())

sorted_words = sorted(words, key=lambda word: (len(word), word))

for i in sorted_words:
    print(i)
