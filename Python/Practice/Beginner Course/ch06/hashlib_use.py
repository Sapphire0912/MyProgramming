import hashlib
m = hashlib.md5()
data = 'Test String'
m.update(data.encode('utf-8'))
print(m.hexdigest())

# md5 = hashlib.md5(b'Test String!').hexdigest()
# print(md5)