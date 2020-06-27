s = input("Enter a string")
diction = {}
for i in range(len(s)):
    if s[i] in diction:
        diction[s[i]] = diction[s[i]] + 1
        continue
    else:
        diction[s[i]] = 1
print(diction)