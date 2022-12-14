num = input()
phrase = list(map(str, input().split()))
print(max(phrase, key=len))
print(len(max(phrase, key=len)))
