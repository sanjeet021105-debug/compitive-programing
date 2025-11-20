def reverseString(s):
    if s=="":
        return s
    return reverseString(s[1:])+s[0]

s= input()
print(reverseString(s))