num = input()
phrase = input().split()
print(max(phrase, key=len))
print(len(max(phrase, key=len)))
