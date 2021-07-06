import string
s = list(input())
s_upper =[]
s_lower = []
s_odd_digits = []
s_even_digits = []









for i in s:
    if i in string.ascii_lowercase:
        s_lower.append(i)
    elif i in string.ascii_uppercase:
        s_upper.append(i)
    elif i.isdigit() and int(i)%2==0:
        s_even_digits.append(i)
    elif i.isdigit() and int(i)%2!=0:
        s_odd_digits.append(i)

s_lower.sort()
s_upper.sort()
s_odd_digits.sort()
s_even_digits.sort()
l = s_lower+s_upper+s_odd_digits+s_even_digits
print("".join(l),sep="")

        
    
