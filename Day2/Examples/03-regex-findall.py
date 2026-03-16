import re

s = "Python is Powerful and Great"
result = re.findall(r'\bP\w+', s)
print(result)

v = "Python is Powerful and Great"
result1 = re.findall(r'Great', v)
print(result1)