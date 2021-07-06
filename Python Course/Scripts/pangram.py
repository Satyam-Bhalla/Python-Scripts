# Enter your code here. Read input from STDIN. Print output to STDOUT
import string

l = set(string.ascii_lowercase[:])
s = input().lower().replace(' ','')
if(set(s)==l):
    print('pangram')
else:
    print('not pangram')
