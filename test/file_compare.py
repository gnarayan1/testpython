'''
Created on Feb 1, 2014

@author: geeth
'''

if __name__ == '__main__':
    f = open('C:\\Users\\geeth\\Documents\\Work\\Opargo\\codes.txt', 'r')
    f1 = open('C:\\Users\\geeth\\Documents\\Work\\Opargo\\ICD9Codes.csv', 'r')
    fo = open('C:\\Users\\geeth\\Documents\\Work\\Opargo\\Compare.csv', 'w')
    for line in f:
        code = line.split(' ')[0].lstrip().rstrip()
        name = line[len(code)+1:].rstrip().rstrip('\n').lstrip()
        for line1 in f1:
            icd9code = line1.split(',')[0].lstrip().rstrip()
            icd9name = line1[len(code)+1:].rstrip().rstrip('\n').lstrip()
            # print(code, icd9code)
            if code == icd9code:
                #fo.write("{0},{1},{2}\n".format(code,name, icd9name))
                print(code, icd9code)
        #print("insert into cpts (code, name) values ('",code,"','",name,"');")
        #print(code)
        