def filetree(pa=r"./", de=0, spa=r"./"):
    def fi(pa, de):
        from os.path import isdir
        from os import listdir
        if de == 0:
            f.write('文件夹:' + pa + '\n')
        for i in listdir(pa):
            f.write('|    ' * de + '+--' + i + '\n')
            di = pa + '/' + i
            if isdir(di):
                fi(di, de + 1)

    f = open(spa + '\\' + '_'.join(pa.replace(':', '').split(sep='\\')) + '_filetree2.xlsx', 'w')
    fi(pa, de)
    f.close()
# filetree()
def fileTree(pa=r"./", de=0):
    from os.path import isdir
    from os import listdir
    if de == 0:
        print('文件夹:' + pa)
    for i in listdir(pa):
        print('|    ' * de + '+--' + i)
        di = pa + '/' + i
        if isdir(di):
            fileTree(di, de + 1)
print(filetree())