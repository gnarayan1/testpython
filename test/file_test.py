'''
Created on Feb 1, 2014

@author: geeth
'''

if __name__ == '__main__':
    f = open('C:\\Users\\geeth\\Documents\\Work\\Opargo\\Codes070515.csv', 'r')
    fo = open('C:\\Users\\geeth\\Documents\\Work\\Opargo\\Codes070515.dml', 'w')
    for line in f:
        code = line.split(',')[0].replace( "\"", '').replace( "'", '').lstrip().rstrip()
        name = line[len(code)+1:].rstrip().rstrip('\n').lstrip()
        name = name.replace( "\"", '').replace( "'", '').rstrip()
        fo.write("insert into cpts (code, name) values ('{0}','{1}');\n".format(code,name))
        #print("insert into cpts (code, name) values ('",code,"','",name,"');")
        #print(code)
        