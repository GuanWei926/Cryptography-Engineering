freq = [0] * 26
text = input()
total = 0

for i in range(len(text)):
    if text[i] == " ":
        continue
    freq[ord(text[i]) - ord("A")] += 1
    total += 1

for i in range(26):
    print("%c: %f" % (chr(i + ord("A")), freq[i] / total * 100), end="%\n")
