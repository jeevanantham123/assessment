ip = list(map(int, input("Enter ages of different people: ").split()))
print("Ages of Different people: ", ip)
CounterList=[0]*10
numRange=["1-10","11-20","21-30","31-40","41-50","51-60","61-70","71-80","81-90","91-100"]

for i in ip:
    if i>=1 and i<=10:
        CounterList[0]+=1
    elif i>=11 and i<=20:
        CounterList[1]+=1
    elif i>=21 and i<=30:
        CounterList[2]+=1
    elif i>=31 and i<=40:
        CounterList[3]+=1
    elif i>=41 and i<=50:
        CounterList[4]+=1
    elif i>=51 and i<=60:
        CounterList[5]+=1
    elif i>=61 and i<=70:
        CounterList[6]+=1
    elif i>=71 and i<=80:
        CounterList[7]+=1
    elif i>=81 and i<=90:
        CounterList[8]+=1
    elif i>=91 and i<=100:
        CounterList[9]+=1
        
print("Age Group\t Total number of People")
for j in range(len(CounterList)):
    print(numRange[j],"\t\t",CounterList[j])
