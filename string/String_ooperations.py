A = input()
A= A+A

new_string = ""
for ch in A:
    if not ch.isupper():     
        new_string = new_string + ch   
A = new_string

words= 'aeiou'
result =''
for ch in A:
    if ch in words:
        result+= "#"
    else:
        result+=ch

print(result)