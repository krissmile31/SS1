
def gcd(e,z):
    q = []
    while ( e != 0):
        q.append(z // e)
        temp = z % e
        z = e
        e = temp
    return q,z

def EEA(z,q):
    p = []
    p.append(0)
    p.append(1)
    for i in range(2,len(q)+1):
        y = p[i-2] -p[i-1]*q[i-2]
        y %= z
        p.append(y)
    return p[len(q)]

def root(r,b,z,d):
    x0 = r * (b/d) % (z/d)
    return int(x0)

def main():
    p = 7
    q = 11
    e = 17
    n = p * q
    z = (p - 1) * (q - 1)
    x = gcd(e, z)
    r = EEA(z, x[0])
    d = root(r,1, n, x[1])
    c1, c2, c3 = 37, 39, 29
    m1, m2, m3 = (c1**d) % n, (c2**d) % n, (c3**d) % n
    print('The decrypted message: ', end="")
    print(chr(m1), chr(m2), chr(m3))

main()

