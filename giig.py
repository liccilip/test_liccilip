import hashlib
file = open('cok.txt', 'rb').read()
x = hashlib.md5(file).hexdigest()
x
оооо
