from read_input import read_input
data = read_input("02", "2015").splitlines()
p1, p2 = 0, 0

for _, dimensions in enumerate(data):
    l,w,h = sorted(list(map(int, dimensions.split("x"))))
    p1 += 3*l*w + 2*h*(l + w)
    p2 += 2*(l+w) + l*w*h

print(p1)
print(p2)