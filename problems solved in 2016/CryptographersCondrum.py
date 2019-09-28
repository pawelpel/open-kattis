text = input()
counter = 0
for l in range(0,len(text),3):
    if text[l+1] == "E":
        counter += 1
    if text[l] == "P":
        counter += 1
    if text[l+2] == "R":
        counter += 1
print(len(text)-counter)
