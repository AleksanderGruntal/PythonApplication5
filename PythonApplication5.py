#0

text=(input("Esimene nimi: "))
i = 0
while i < len(text):
    print(text[i])
    i += 1
print("---------------------------------")
for i in text:
    print(i)

#21
while True:
    s=str(input(": "))
    L = s.split()
    
    lon = max(L, key =len)
    short = min(L, key=len)
    print(f"Longest: {lon}, shortest: {short}")

