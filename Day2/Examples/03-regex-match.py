import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)

if match:
    print("Match Found", match.group())
else:
    print("Match Not Found")



import re

text = "The quick brown fox"
pattern = r"The quick brown fox"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")