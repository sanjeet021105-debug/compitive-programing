def stringPalin(s):
    if len(s) <= 1:
        return True
    if s[0]== s[-1]:
        return stringPalin(s[1:-1])
    else:
        return False
    
s= input()
 
if stringPalin(s):
    print("Palindrome")
else:
    print("Not Palindrome.")    