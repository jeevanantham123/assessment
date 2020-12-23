from itertools import groupby
from collections import Counter as c

num2word = {1:"one", 2:"two", 3:"three",
            4:"four", 5:"five", 6:"six",
            7:"seven", 8:"eight", 9:"nine", 0:"zero"
            }

n = "1145221" #input()
nums=[]
def line_1(n):
    l = list(map(int,list(n)))
    for g,v in groupby(l):
        nums.append(dict(c(list(v))))
    l=[]
    #print(nums)
    for num in nums:
        k,v = list(num.items())[0]
        #print(k,v)
        op=""
        op+=str(num2word[v]+" "+str(k))
        if v!=1:
            op+="'s"
        l.append(op)
        #print(l)
    final = " and ".join(l)
    return final

def line_2(n):
    nums = dict(c(n))
    l=[]
    for k,v in nums.items():
        op=""
        op+=str(num2word[v]+" "+k)
        if v!=1:
            op+="'s"
        l.append(op)
    
    final = " and ".join(l)
    return final  

#print(line_1(n))
print("Total: {}".format(line_2(n)))

