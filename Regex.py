import re,pyperclip
text = str(pyperclip.paste())
pno = re.compile(r'(\+8801\d{9}|01\d{9})')
emal = re.compile(r'[a-zA-Z0-9.-_%+]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{,3}')
mo = pno.findall(text)

for i in range(len(mo)):
    print(mo[i])
eo = emal.findall(text)

for i in range(len(eo)):
    print(eo[i])
