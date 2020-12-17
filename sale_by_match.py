def sockMerchant(n, ar):
    res = 0
    d = dict()
    for e in ar:
        if e in d:
            d[e] += 1
            if d[e] == 2:
                res += 1
                d[e] == 0
        else:
            d[e] = 1
    return res

l = "10 20 20 10 10 30 50 10 20".split()
print(sockMerchant(9,l))