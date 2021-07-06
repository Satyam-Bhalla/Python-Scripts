import re

pattern = r"Cookie"
sequence = "Cookie"

if re.match(pattern, sequence):
  print("Match!")
else: print("Not a match!")

## A period . matches any single character except newline character.
print(re.search(r'Co.k.e', 'Cookie biscuits').group())


## \w - Lowercase w. Matches any single letter, digit or underscore.
print(re.search(r'Co\wk\we', 'Cookie').group())


##\W - Uppercase w. Matches any character not part of \w (lowercase w).
print(re.search(r'C\Wke', 'C@ke').group())


## \s - Lowercase s. Matches a single whitespace character like: space, newline, tab, return.
print(re.search(r'Eat\scake', 'Eat cake').group())

##\S - Uppercase s. Matches any character not part of \s (lowercase s).
print(re.search(r'Cook\Se', 'Cookie').group())

##\t - Lowercase t. Matches tab.
##print(re.search(r'Eat\tcake', 'Eat    cake').group())


##\n - Lowercase n. Matches newline.
##\d - Lowercase d. Matches decimal digit 0-9.
print(re.search(r'c\d\dkie', 'c00kie').group())


##^ - Caret. Matches a pattern at the start of the string.
print(re.search(r'^Eat', 'Eat cake').group())


##$ - Matches a pattern at the end of string.
print(re.search(r'cake$', 'Eat cake').group())


##[abc] - Matches a or b or c.
##
##[a-zA-Z0-9] - Matches any letter from (a to z) or (A to Z) or (0 to 9).
##Characters that are not within a range can be matched by complementing the set.
##If the first character of the set is ^, all the characters that are not in the set will be matched.
print(re.search(r'Number: [0-6]', 'Number: 5').group())
# Matches any character except 5
print(re.search(r'Number: [^5]', 'Number: 0').group())



##\A - Uppercase a. Matches only at the start of the string. Works across multiple lines as well.
print(re.search(r'\A[A-E]ookie', 'Cookie').group())


##+ - Checks for one or more characters to its left.
print(re.search(r'Co+kie', 'Cooookie').group())

##* - Checks for zero or more characters to its left.
# Checks for any occurrence of a or o or both in the given sequence
print(re.search(r'Ca*o*kie', 'Caokie').group())

##? - Checks for exactly zero or one character to its left.
# Checks for exactly zero or one occurrence of a or o or both in the given sequence
print(re.search(r'Colou?r', 'Color').group())


##{x} - Repeat exactly x number of times.
##
##{x,} - Repeat at least x times or more.
##
##{x, y} - Repeat at least x times but no more than y times.
print(re.search(r'\d{9,10}', '0987654321').group())


##When you need to use an expression several times in a single program,
pattern = re.compile(r"cookie")
sequence = "Cake and cookie"
print(pattern.search(sequence).group())
# This is equivalent to:
print(re.search(pattern, sequence).group())


str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## re.sub(pat, replacement, str) -- returns new string with all replacements,
## \1 is group(1), \2 group(2) in the replacement
print(re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str))
## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher
