'''
Created on Feb 3, 2014

@author: geeth
'''

if __name__ == '__main__':
    f = open('ins2.list', 'r')
    #f1 = open('ins.list', 'r')
    i = 30
    for line in f:
        found=False
        name = line.rstrip().rstrip('\n').lstrip()
        print("insert into insurance_providers (name, description, national_health_plan_id) values ('{0}','{1}', {2});\n".format(name, name,i))
        i=i+1
