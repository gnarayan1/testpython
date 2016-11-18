'''
Created on Feb 1, 2014

@author: geeth
'''

if __name__ == '__main__':
    f = open('C:\\Users\\geeth\\Documents\\Work\\Opargo\\icderrorsinp.txt', 'r')
    fo = open('C:\\Users\\geeth\\Documents\\Work\\Opargo\\icderrors.txt', 'w')
    for line in f:
        if not "ERROR" in line: continue
        fo.write(line)
        #print("insert into cpts (code, name) values ('",code,"','",name,"');")
        #print(code)
        