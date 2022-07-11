
def hehe(x1=[0.9460666, 0.11884469, -0.48295271, -0.93720798, -1.19210023],
         y1=[-8.87466906, -1.28013417, -1.56781624, -1.79095979, -1.97328135], y2=[-0.87466906, -1.28013417, -1.56781624, -1.79095979, -1.97328135], n=2):
    from numpy import polyfit, array
    from sympy import symbols, lambdify, ln
    import seaborn as sns
    import matplotlib.pyplot as plt
    sns.set()
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    x = symbols('x')
    f1 = symbols('f1', functions=True)
    f2 = symbols('f2', functions=True)
    f = lambdify(x, ln(x))
    # a = [0.2, 0.092, 0.051, 0.032, 0.022, 0.016]
    # b = linspace(76.6/2, 76.6/7, 6, endpoint=True)/100

    # print(a, b)
    # a, b = f(array(a)*10), f(array(b))
    x1, y1, y2 = array(x1), array(y1), array(y2)
    n1 = polyfit(x1, y1, n)
    n2 = polyfit(x1, y2, n)

    # print(a, b, ni)
    f1 = 0
    for i in range(len(n1)):
        f1 += n1[-(i + 1)] * x ** (i)
    F1 = lambdify(x, f1)
    f2 = 0
    for i in range(len(n2)):
        f2 += n2[-(i + 1)] * x ** (i)
    F2 = lambdify(x, f2)
    plt.plot(x1, y1, 'r:o', label='升温实验')
    plt.plot(x1, F1(x1), 'r-o', label='升温拟合')
    plt.plot(x1, y2, 'b:o', label='降温实验')
    plt.plot(x1, F2(x1), 'b-o', label='降温拟合')
    plt.title('升温拟合：f1={}\n降温拟合：f2={}'.format(f1, f2))
    plt.xlabel('温度值（C。）')
    plt.ylabel('长度值（mm-3）')
    plt.legend()
    plt.show()
    return F1, F2


if __name__ == '__main__':
    hehe()
