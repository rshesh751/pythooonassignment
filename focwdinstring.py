#finding number of ovals,consonents,digits and words in given string
str = input("Enter a string: ")
key = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ova = ['a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U']
words = 1
ovals = 0
space = 0
digits = 0
conso = 0
print(str)
for i in range(len(str)):
    for j in range(10):
        if key[j] == str[i]:
            digits += 1
        if ova[j] == str[i]:
            ovals += 1
    if str[i] == ' ':
        space += 1
        words += 1
conso = len(str) - (ovals + space + digits)
print("no. of words: ", words)
print("no. of ovals: ", ovals)
print("no. of consonents: ", conso)
print("no. of digits: ", digits)
