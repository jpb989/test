import numpy as np
def fact(n):
    f=1
    for i in range(1,n+1):
       f*=i
    return f

def mean(l):
    #input type list of numbers return mean of list
    '''for joshua'''

    '''
    l=np.array(l)
    return l.sum()
        #or
    '''

    if(len(l)==1):
        return l[0]
    return l[0]+mean(l[1:])
    #pass

def print_pattern3(n):
    #print given patter
    #eg if n==3
    #*
    #**
    #***
    '''for nilesh'''

print(mean([1,2,3,4,5,5,6,7,8,9]))
