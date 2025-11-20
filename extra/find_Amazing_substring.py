# you have given a string s. you have to find all amazing substring of s. An amazing substring is 1. what start with a vowals. example input -> ABEC output -> 6

s = "ABEC"
count = 0
for i in range(len(s)):
    n= len(s)
    if s[i]=='A' or 'E':
        count =  count+n-i
print(count)


# find the number of occurence of 'bob' in string A. consisting of lowercase english alphabets  