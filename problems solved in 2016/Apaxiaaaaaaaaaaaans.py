text = input()
nowyText =''
for i in range(0,len(text)):
    if i == len(text)-1:
        nowyText += text[i]
        break
    if text[i]==text[i+1]:
        pass
    else:
        nowyText += text[i]
print(nowyText)

