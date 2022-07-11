def originalMaze(n=20, m=30):
    import numpy as np
    m0 = np.random.rand(n, m)
    for i in range(n):
        for j in range(m):
            if m0[i][j] < 0.25:
                m0[i][j] = 0
            else:
                m0[i][j] = 1
    return m0
def mazeSolution(n=20, m=30):
    import numpy as np
    import random
    m1 = np.ones((n, m))
    p = [n // 2, m // 2]
    while True:
        try:
            t = random.randint(1, 4)
            if p[0] == 1:
                return m1
            elif p[1] == 1:
                return m1
            elif t % 4 == 0:
                p[0] -= 2
                m1[p[0] + 1][p[1]] = 0
                m1[p[0]][p[1]] = 0
            elif t % 4 == 1:
                p[0] += 2
                m1[p[0] - 1][p[1]] = 0
                m1[p[0]][p[1]] = 0
            elif t % 4 == 2:
                p[1] -= 2
                m1[p[0]][p[1] + 1] = 0
                m1[p[0]][p[1]] = 0
            elif t % 4 == 3:
                p[1] += 2
                m1[p[0]][p[1] - 1] = 0
                m1[p[0]][p[1]] = 0
        except IndexError:
            m1[n // 2][m // 2] = 2
            return m1
def prin(mn, n, m):
    for i in range(n):
        print(str(list(mn[i])).replace(".",'.').replace('0', ' ').replace('1', '#').replace(',', '').replace('2', '@'))
def mazemain(m=40,n=40):
    m0 = originalMaze(m=m, n=n)
    m1 = mazeSolution(m=m, n=n)
    m2 = m0 * m1
    prin(mn=m2, m=m, n=n)
    print(
        "-------------------------------------------------------------------------------------------------------------------------------------------")
    prin(mn=m1, m=m, n=n)
if __name__ == "__main__":
    mazemain()


