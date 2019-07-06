import re

text = input()
# text = "\/\/in_US$100000_in_our_Ca$h_Lo||ery!!!"

matches = re.findall(r"(_)|([A-Z])|([a-z])|([^A-Za-z_])", text)

w = u = l = s = 0

for m in matches:
    if m[0] != '':
        w += 1
    elif m[1] != '':
        u += 1
    elif m[2] != '':
        l += 1
    elif m[3] != '':
        s += 1

text_len = len(text)

print(f"{w/text_len}\n{l/text_len}\n{u/text_len}\n{s/text_len}")