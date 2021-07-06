import re
from collections import Counter
words = re.findall(r'\w+', "Hello hello how are you?".lower())
print(Counter(words))
print(Counter(words).most_common())
