from read_input import read_input
data = read_input("04", "2015")

from hashlib import md5
p1, p2 = False, False

num = 0
while True:
    num += 1
    x = data + str(num)
    res = md5(f"{data}{num}".encode()).hexdigest()
    if res[:5] == "00000" and not p1:
        print(num)
        p1 = True
    if res[:6] == "000000" and not p2:
        print(num)
        p2 = True
    if p1 and p2:
        break
