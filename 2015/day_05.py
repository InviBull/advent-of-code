from read_input import read_input
data = read_input("05", "2015").splitlines()

p1, p2 = 0, 0
for word in data:
    nice = True
    numVowels = 0
    for x in "aeiou":
        numVowels += word.count(x)
    
    if numVowels < 3:
        nice = False
    else:
        for x in {"ab","cd", "pq", "xy"}:
            if x in word:
                nice = False
                break
        if nice:
            flag = False
            for x in "abcdefghijklmnopqrstuvwxyz":
                if x*2 in word:
                    flag = True
                    break
            if not flag:
                nice = False
    
    if nice:
        p1 += 1
print(p1)
        