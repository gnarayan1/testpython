days = [1,2,3,4,5]
d = {'a':[1], 'b':[3,4],'c':[5],'d':[2,4]}
#d = {'a':[1], 'b':[2],'c':[5],'d':[2,5]}
#d = {'a':[1,5], 'b':[3,5],'c':[5],'d':[2,5]}
#d = {'a':[1], 'b':[2],'c':[3],'d':[4]}
d = {'a':[1,2,3,4,5], 'b':[3,4],'c':[2,5],'d':[1]}
counts = {}
res=[]


if __name__ == '__main__':
    #print(counts)
    while len(d) > 0:
    #for i in range(0, 3):
        counts = {}
        for day in days:
            if day not in counts:
                counts[day] = 0
            for key, value in d.items():
                if day in value:
                    counts[day]+=1
        
        for k, v in list(counts.items()):
            if v == 0:
                del counts[k]
                days.remove(k)
        #print('Counts:',counts)
        minday = max(counts, key=counts.get)
        #print(minday)
        res.append(minday)
        del counts[minday]
        
        
        for k, v in list(d.items()):
            if minday in v:
                #print('in v')
                del d[k]
                #print("Dict:",d)


        #print(len(counts))
                
    print('Days=',res)
    
        