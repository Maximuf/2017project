h = s[0]
sv =[]
for i in range(1, len(s)):
    if s[i] >= s[i-1]:
        h += s[i]

    else:
        sv.append(h)
        h=s[i]
sv.append(h)
g = sv[0]
if len(sv) > 1:
    for j in range(0, len(sv)):
        if len(sv[j]) > len(g):
            g = sv[j]
else:
    g = sv[0]

print("Longest substring in alphabetical order is: " + g)
