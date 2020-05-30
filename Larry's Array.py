t = int(input())


#function to rotate the array
def rotate(a):
    t = []
    for i in range(len(a)-1):
        temp = a[0]
        t.insert(i,a[i+1])

    t.append(temp)

    return t


for t_itr in range(t):

    n = int(input())
    a = list(map(int, input().rstrip().split()))
    i = 1
    s = 1
    for i in range(n):

        if i+1==a[i]: #checking whether the element is in coorect position or not
            continue
        elif i+1 == n-1 and i+1>1:#In the given array if we check till n-2 elements the remaining two elements will get sorted automatically  
            break
        else:
            t = a[i:n]#Reducing the array to search efficiently 
            while t[0]!=(i+1):
                #Untill the correct element gets to the first position we will follow the process which is mentioned in the problem
                q = t.index(i+1)
                if q==1:
                    z = t[0:3]
                    z = rotate(z)
                    t[0:3] = z #Assigning back the rotated array to the original array
                else:
                    z = t[q-2:q+1]
                    e = z.index(i+1)
                    for _ in range(e):
                        z = rotate(z) 
                    t[q-2:q+1] = z #Same thing is done here..

            a[i:n] = t #After the element comes to the first position we are assigning back the array "t" to the original array "a" (If you want clear picture of the process write print(a) here..)
                
    if a[-1] == n:
        print("YES")
    else:
        print("NO")
            




