#to check given string is a palindrome or not
k=input()
if k==k[::-1]:
    print(f"{k} is a palindrome")
else:
    print(f"{k} is not a palindrome")