from collections import deque
### method 1 (removing last element and adding it to the front)
def method1(test_deque,rotate):
    for i in range(rotate):
        popped = test_deque.pop()
        test_deque.appendleft(popped)
    print("method1",list(test_deque))


# method 2 ( creating new array)
def method2(test_list,n,k):
    arr=[0]*n
    for i in range(n):
        arr[(i+k)%n] = test_list[i]
    print("method2",arr)

test_list = list(map(int, input("Enter array: ").split()))
test_deque = deque(test_list)
k = int(input("Enter k: "))
n=len(test_list)
rotate = k%n
method1(test_deque,rotate)
method2(test_list,n,k)
