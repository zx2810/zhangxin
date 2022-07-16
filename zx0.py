def staff(wo='原神芭芭拉',
          url=r'https://image.baidu.com/search/index?ct=201326592&z=9&tn=baiduimage&ipn=r&word=%E5%8E%9F%E7%A5%9E%E8%8A%AD%E8%8A%AD%E6%8B%89&pn=0&istype=2&ie=utf-8&oe=utf-8&cl=2&lm=-1&st=-1&fr=&fmq=&ic=0&se=&sme=&width=0&height=0&face=0&hd=1&latest=0&copyright=0',
          nu=90):
    from zx_h import change, gethtmlbypyppteer, downLoadjpg, gethtmlbyselenium
    # se = input_set(se)
    url = change(wo, url)
    html = gethtmlbypyppteer(url)
    # html = getHtmlbyRequests(url)
    # html = gethtmlbyselenium(url)
    downLoadjpg(wo, nu, html)


def img2(pa='img/game.png', spa='img/game2.png'):
    from PIL import Image
    im = Image.open(pa)
    # im = im.convert('RGB')
    im = im.convert('RGBA')
    im.save(spa, quality=100)


def panch():
    from pyautogui import hotkey, keyDown, keyUp, typewrite, doubleClick
    from time import sleep
    url = r'http://my.lzu.edu.cn:8080/login?service=http://my.lzu.edu.cn'
    path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    keyDown('win')
    hotkey('r')
    keyUp('win')
    typewrite(url)
    hotkey('enter')
    sleep(0.5)
    doubleClick(1346, 440)
    sleep(0.5)
    doubleClick(1346, 510)
    sleep(0.5)
    doubleClick(1346, 510)
    sleep(0.5)
    doubleClick(282, 573)
    sleep(1)
    doubleClick(1675, 687)
    sleep(0.5)
    doubleClick(1672, 1000)
    sleep(0.5)
    doubleClick(1920, 20)


def news():
    import requests
    import re
    print('国际新闻')
    url = 'https://news.china.com/international/'
    r = requests.get(url)
    r.encoding = 'utf-8'
    html = r.text
    alist = re.findall(
        r'.html" target="_blank">.+</a></h3><span class="item_info">', html)
    blist = re.findall(r'<em class="item_source">.+</em>', html)
    for i in range(20):
        print('({})'.format(i + 1), end='')
        print(blist[i][24:-42], end='于')
        print(blist[i][-15:-5], end='报道：')
        print(alist[i][23:-33])
    print('兰大新闻')
    url = 'http://jwc.lzu.edu.cn/'
    r = requests.get(url)
    r.encoding = 'GB2312'
    html = r.text
    li = re.findall(
        r'<li><a title=\'(.+?)\'\s\shref=\".*?/lzupage(.+?)\"', html)
    for i in range(-10, 0):
        print('({})'.format(i + 11), end='')
        print(li[i][0] + '...http://jwc.lzu.edu.cn/lzupage' + li[i][1])
    input('input for leave')


def getpotion():
    import pyautogui
    import time

    try:
        while True:
            x, y = pyautogui.position()
            rgb = pyautogui.screenshot().getpixel((x, y))
            posi = 'x:' + str(x).rjust(4) + ' y:' + \
                   str(y).rjust(4) + '  RGB:' + str(rgb)
            print('\r', posi, end='')
            time.sleep(0.5)

    except KeyboardInterrupt:
        print('已退出！')


def timer():
    from time import localtime, sleep
    from os import startfile
    while True:
        if localtime().tm_hour == 7 and localtime().tm_min == 25:
            startfile(r"D:\Programming\User\dist\panch.exe")
            sleep(50)
            startfile(
                r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\腾讯软件\QQ音乐\QQ音乐.lnk")
            sleep(5)
            startfile(r"D:\Programming\User\dist\news.exe")
            sleep(5)
            startfile(
                r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OneNote.lnk")
            sleep(60)
        sleep(40)


def fileStatisticsbyPython_zx():
    from os import listdir, path

    from pandas import DataFrame

    pa = str(input('postion(\\):'))
    li = []
    for i in listdir(pa):
        if path.isdir(pa + '\\' + i):
            li.append(i)
    lc = []
    for i in li:
        lt = list('=HYPERLINK(\"' + pa + '\\' + i + '\\' + j +
                  '\",\"' + j + '\")' for j in listdir(pa + '\\' + i))
        lt.insert(0, str(len(listdir(pa + '\\' + i))))
        lc.append(lt)
    df = DataFrame(data=lc, index=li)
    df.to_excel(pa + '\\' + 'fileStatisticsbyPython_zx.xlsx', na_rep=' ')
    print(df)
    input('input for leave')


def install():
    import os
    libs = ["pyppeteer", "pdf2docx", "numpy", "matplotlib", "pillow", "sklearn", "requests", "jieba", "pyperclip",
            "wheel", "pyautogui", "sympy", "pyinstaller", "Cpython", "selenium", "paddleocr", "opencv-python -i",
            "pandas",
            "wordcloud", "ipython", "paddlepaddle", "openpyxl"]
    # libs=['pyautogui']

    try:
        for lib in libs:
            os.system("python -m pip install " + lib)
            print("Successful")
    except BaseException:
        print("Failed Somehow")


def temtimer():
    from time import sleep
    from os import startfile
    startfile(r"D:\Programming\User\dist\panch.exe")
    sleep(50)
    startfile(
        r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\腾讯软件\QQ音乐\QQ音乐.lnk")
    sleep(5)
    startfile(r"D:\Programming\User\dist\news.exe")
    sleep(5)
    startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OneNote.lnk")


def originalMaze(n=20, m=30):
    import numpy as np
    m0 = np.random.rand(n, m)
    for i in range(n):
        for j in range(m):
            if m0[i][j] < 0.25:
                m0[i][j] = 0
            else:
                m0[i][j] = 1
    m0[n // 2][m // 2] = 1
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
        print(str(list(mn[i])).replace(".", '.').replace(
            '0', ' ').replace('1', '#').replace(',', '').replace('2', '@'))


def mazemain(m=40, n=40):
    m0 = originalMaze(m=m, n=n)
    m1 = mazeSolution(m=m, n=n)
    m2 = m0 * m1
    prin(mn=m2, m=m, n=n)
    print(
        "-------------------------------------------------------------------------------------------------------------------------------------------")
    prin(mn=m1, m=m, n=n)


def isprime(n=100):
    import numpy as np
    is_prime = np.ones((n,), dtype=bool)
    is_prime[:2] = 0
    N_max = int(np.sqrt(len(is_prime)))
    for j in range(2, N_max):
        is_prime[2 * j::j] = False
    return is_prime

    # for i in range(len(ni)):
    #     f += ni[-i]*x**(i)
    # plot((a, b), f)

    # return f


def hehe(a=[0.9460666, 0.11884469, -0.48295271, -0.93720798, -1.19210023],
         b=[-0.87466906, -1.28013417, -1.56781624, -1.79095979, -1.97328135], n=2):
    from numpy import polyfit, array
    from sympy import symbols, lambdify, ln
    import seaborn as sns
    import matplotlib.pyplot as plt
    sns.set()
    x = symbols('x')
    f = symbols('f', functions=True)
    f = lambdify(x, ln(x))
    # a = [0.2, 0.092, 0.051, 0.032, 0.022, 0.016]
    # b = linspace(76.6/2, 76.6/7, 6, endpoint=True)/100

    # print(a, b)
    # a, b = f(array(a)*10), f(array(b))
    a, b = array(a), array(b)
    ni = polyfit(a, b, n)
    # print(a, b, ni)
    f = 0
    for i in range(len(ni)):
        f += ni[-(i + 1)] * x ** (i)
    F = lambdify(x, f)
    plt.plot(a, b, 'b-o', a, F(a), 'r:d')
    plt.title('f={}'.format(f))
    plt.show()
    return F


def lineStas(x, y):
    from scipy import stats
    import matplotlib.pyplot as plt
    from seaborn import set
    set()
    plt.scatter(x, y)
    slope, intercept, rvalue, pvalue, stderr = stats.linregress(x, y)
    getmodel = list(map(slope * x + intercept, x))
    plt.plot(x, getmodel)


def Polyfit(x, y, deg):
    import matplotlib.pyplot as plt
    from seaborn import set
    import pandas as pd
    from numpy import poly1d, polyfit, corrcoef
    set()
    # 以上为预设，非必要
    plt.scatter(x, y)
    model = poly1d(polyfit(x, y, deg))
    r = pd.DataFrame(corrcoef(x, y))
    plt.plot(x, model(x))
    plt.title(str(model) +
              '\nCorrelation coefficient \n(take rows in order as new rows, first-order correlation, multi-order ignore)\n' + str(
        r))
    return model, r


# import inspect
#
# for name, obj in inspect.getmembers(inspect):
#     if inspect.isclass(obj):
#         print(name, str(obj))
#     if inspect.isfunction(obj):
# print(name, str(obj))
if __name__ == '__main__':
    import numpy as np
    # news()
    staff()
    # panch()
    # import matplotlib.pyplot as plt
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    # plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    # # 支持中文
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    # plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # from matplotlib import rc
    # font = {'family': 'SimHei', "size": 24}
    # rc('font', **font)  # 一次定义终身使用
    # from gethtml.gethtmlbypyppeteer import gethtmlbypyppteer
    # f = hehe(n=1)
    # x = np.linspace(0.5, 3.5, 7, endpoint=True)*1e-3*9.793
    # y = np.array([12.5, 25.1, 38.4, 51.5, 66.6, 79.5, 91.5])
    # deg = 1
    # print(x, y)
    # Polyfit(x, y, deg)
    # staff(wo='利兹与青鸟', nu=30, url='https://yandex.com/images/search?family=yes&rpt=imageview&cbir_page=similar&url=https%3A%2F%2Fyandex-images.clstorage.net%2FU5l21Ro55%2F5e2d48nVvkh%2Ftv4qHX8gnMkCD0xATFyjmg29CMMkKQSyaWePtHYmuaXOl-F7d5rZoEm4y4V-BD3tLx4KY6AUcIJLytsJKJA5rrinbY21b9FAVh2dR1zeY8vKMoSKbSeY-iSo1b_85eqkDNbmqbOKWi8ELFucKNygOLYAi6wrjj8JWwLayGER8S94rjNK_GiagkBJCxkCXObETvbABi3q1nzib1ywfSUh7QiXLDp6iNsjB3LVnKtd6zczhQQlrYT5wN0BG80l0XCn9-H6RXFuEQUBiQqbBBRjxYq1y8ZuZBF7pCDZsL_p62pMW-SxsklYLQ890thlUq7_soyEJenEconSyBWCqZd9ZDdh-sc-4NlIBgqD0sbbLcEHcE_C62Rc-Opq0fOxYmjrQ5mr8_BEGihNfR3UpZ3leL5AiyzlCbWD0AWUQmfX_ig6Y_2Cs-WRAUCBgR-JUOWHA7TIgCyinfVkYxfzMqhv40HfLLY1RRBpjXUUGqXRIz3xBU2tLQR_iFnFlMVsmvpuMq0wgz6p0ARPgspaTN7uyQ_3A4Sg4l18qurYcHWjLmxBnCBzv4uY7oA02JogV24_Mo5NI6CLuIqZwNwK41L8ZHLqdM37oJWBB8qGlkZY40OJMUZHLqSdOqXmH3b6oi-izN2iP7KBWKgLMNzQZ9PqObFJROJhTbMLGQ8ciGGY-ez7bHTCdSFdRkwKANZKmK5JSjTJQqvqlfzsr5h2sS_h5kDepjmyylUmz7-dkCHa5PW9D8ptK8S_yBlPX4CkmP0mN6D3xfKvUY2ODwoeQtityEV5RwBvpp3yLKYXPfWh5ysHHiE3sk1fLc73EJBhWWN9947PKuFL-oKUzVACIVq4oXkiMgA66FQMSs3L0sTYJoxJ_A5GZC6SdCFu1nj6K26uSVUm-zrFFCoCeJJVplig_3BHyCqiTXCKmcGcCqRbvmG_7bNF_eccRgjFhNuBl2lAQH2Pwuvlmzqop1c5dc&cbir_id=1495804%2FgbGpJxKlDatVo2JaWcaXdg1998&crop=0.15%3B0.15%3B0.85%3B0.85')
    # news()
    # n=1000000
    # print(isprime(1000))
    # li=isprime(n)
    # for i in range(n):
    #     if li[i] :
    #         print(i)
    # print(gethtmlbypyppteer())
    # news()
    # mazemain(n=80, m=80
    # news()
    # from matplotlib import pyplot as plt
    # import numpy as np

    # x1 = np.linspace(1, 10, 20)
    # print(x1)
    # y1 = x1 * x1 + 2
    # fig = plt.figure()
    # axes = fig.add_axes([0.1, 0.1, 0.9, 0.9])
    # axes.plot(x1, y1, 'r')
    # plt.show()
