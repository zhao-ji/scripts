dict = {}

for i in range(0,10):
    dict[i] = str(i)

for i in range(0,26):
    dict[i+10] = chr(i+65)


def redix(a, n):
    S = ''
    while a >= n:
        S += dict[a % n]
        a = a/n
    S += dict[a % n]
    print S[::-1]

redix(255,16)
