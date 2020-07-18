import re
pat = re.compile('[a-z]+')
m = pat.match('tem12po')

print(m.group())
print(m.start())
print(m.end())
print(m.span())