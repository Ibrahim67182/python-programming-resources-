import re




mytext ="ibrahim my age is 21 years old and my name is ibrahim and my father name is junaid "


x= re.findall(r"\d",mytext)
print(x)


y =re.findall(r"ibrahim | junaid",mytext)

print(y)
