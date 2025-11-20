t = int(input())
s = [input().strip() for _ in range(t)]

vowels = 'aeiou'
results = []

for i in s:
    v = c = 0
    for ch in i.lower():
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    results.append(f"{v} {c}")   

print("\n".join(results))

