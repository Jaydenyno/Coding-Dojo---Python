for a in range(151):
    print(a)

for b in range(5, 1001, 5):
    print(b)

for c in range(1,101):
    if c % 10 == 0:
        print(c, "Coding Dojo")
    elif c % 5 == 0:
        print(c, "Coding")

sumD = 0
for d in range(0, 500000):
    if d % 2 == 1:
        sum += d
print(sum)

for e in range(2018, 0, -4):
    print(e)

lowNum = 2
highNum = 9
multi = 3
numArr = []
for f in range(lowNum, highNum + 1):
    if f % multi == 0:
        numArr.append(f)
print(numArr)
