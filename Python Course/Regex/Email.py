import re
email_address = 'Please contact us at: support@datacamp.com'
match = re.search(r'([\w\.-]+)@([\w\.-]+)', email_address)
if match:
  print(match.group()) # The whole matched text
  print(match.group(1)) # The username (group 1)
  print(match.group(2)) # The host (group 2)
