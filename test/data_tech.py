'''
Created on Feb 1, 2014

@author: geeth
'''

if __name__ == '__main__':
    f = open('DataTech.txt', 'r')
    fo = open('DataTechOut.txt', 'w')
    s = set()
    for line in f:
        valarr = line.split(',')
        for vala in valarr:
            val = vala.lstrip().rstrip().rstrip('\n').lower()
            s.add(val)
        #fo.write("insert into cpts (code, name) values ('{0}','{1}');\n".format(code,name))
    s = sorted(s)
    print(s)
    for item in s:
        fo.write(item+'\n')
        