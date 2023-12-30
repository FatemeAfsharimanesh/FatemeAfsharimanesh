x=int(input("Enter x="))
y=int(input("Enter b="))
s=x+y
print("s={0}".format(s))

####

x=int(input("Enter x="))
y=int(input("Enter y="))
if(x>y):
    print("x is bigger than y")
elif(x>y):
    print("x is bigger than y")
else:
    print(" they are equal")

####

x=int(input("Enter x="))
y=int(input("Enter y="))
z=int(input("Enter z="))
max=5
if(y>z):
    max=y
if(x>z):
   max=x
print("max{0}".format(max))


####

a=int(input("Enter your first number="))
count=1
while count<100:
    number=int(input("Enter another number="))
    count+=1
    if(number>a):
       max=number
print(max)

####

a=int(input("Enter your first number="))
max=a
min=a
count=1
while count<100:
    number=int(input("Enter your next number="))
    if(number>max):
        max=number

    elif(number<min):
        min=number
    count+=1

print(max)
print(min)

####


a=[]
for i in range(1,11):
    a.append(int(input("Enter number:")))

a.sort(reverse=True)
print(a)


####

b=[]
for i in range(1,101):
    b.append(int(input("Enter value:")))

b.sort()
print(b)


###


a=int(input("Enter a="))
if(a%2==0):
    print("even")
else:
    print("odd")


####

num=int(input("Enter your number="))
max=num
for i in range(1,10):
    a=int(input("Enter another number="))
    if(a>max):
        max=a

print(max)


####


a=int(input("Enter a="))
b=int(input("Enter b="))
for i in range(a+1,b):
    if(i%2==0):
        print(i)


####


a=int(input("Enter a="))
flag=True
for i in range(2,a):
    if(a%i==0):
        flag=False
        break

if(flag):
    print("F")

else:
    print("H")


###


a=int(input("Enter a="))
b=int(input("Enter b="))
count=0
if a>b:
    (a,b)=(b,a)

for i in range(a+1,b):
    for j in range(2,i):
        if(i%j==0):
            count+=1
            break
        if(count!=0):
           print(i)
           break


###


a=int(input("Enter a="))
b=int(input("Enter b="))
if(a>b):
    (a,b)=(b,a)

for i in range(a+1,b):
    sum=0
    for j in range(1,i):
        if(i%j==0):
            sum+=i
        if(sum==2*i):
            print(i)


###


n=int(input("Enter your number="))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i
if(sum==n):
   print('True')

else:
   print("False")

###


a=[]
for i in range(1,101):
    a.append(int(input("Enter value=")))
print(max(a))


###


lst=[]
for i in range(1,11):
    lst.append(int(input("Enter value=")))
x=int(input("Enter x="))
if x in lst:
    print("found")
else:
    print("not found")



###



lst1=[]
lst2=[]
for i in range(1,101):
    lst1.append(int(input('enter value=')))
for j in range(1,101):
    lst2.append(int(input('Enter more values=')))
c=lst1+lst2
print(c)



###


x=int(input("Enter x="))
sum=0
while x>=0:
    x=int(input('Enter x='))
    sum+=x

print(sum-x)



###



b=int(input("Enter b="))
f=1
i=1
while i<=x:
    f*=i
    i+=1
print("factorial=",f)


###22222
def findthebiggest(a,b,c):
    max=a
    if(b>max):
     max=b
    if(c>max):
     max=c
    else:
      print("They are equal")
    
    print("max={0}".format(max))
    
a=int(input("enter your first number:"))
b=int(input("enter your second number:"))
c=int(input("enter your third number:"))
findthebiggest(a,b,c)

#####


def rec(a,b):
    c=a*b
    return c

a=float(input("Enter length="))
b=float(input("Enter width="))
print("area={0}".format(rec(a,b)))


#####


def isprime(x):
    flag=True
    for i in range(2,x):
        if(x%i==0):
            flag=False
    if(flag==True):
        return 1
    else:
        return 0
    
a=int(input("Enter your number="))
print("The result is={0}".format(isprime(a)))


#####


def iscomplete(a):
    s=0
    for i in range(1,a):
        if(a%i==0):
            s+=i
    if(s==a):
        return 1
    else:
        return 0
x=int(input("Enter number="))
print("checking if complete or not ={0}".format(iscomplete(x)))


####


lst=[]
def maxlist(lst):
    return max(lst)


for i in range(1,101):
    x=int(input("Enter elements="))
    lst.append(x)
print("The biggest element is={0}".format(maxlist(lst)))


    


#####


def isprime(i):
    flag=True
    for j in range(2,i):
        if(i%j==0):
            flag=False
            break
    if(flag==True):
        return 1
    else:
        return 0
    
for i in range(1,1000000):
    if(isprime(i) and i!=1 ):
        print(i)



#####


def plus(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s

n=int(input("Enter n="))
print("The final answer is={0}".format(plus(n)))


#####


def sort_lst(lst):
    lst.sort(reverse=True)
    print(lst)
    

lst=[int(x) for x in input("Enter list elements=").split()]
sort_lst(lst)


####


def search_list(lst,x):
    if x in lst:
        return lst.index(x)
    else:
        return -1
    
lst=[i for i in range(1,101)]
print("The index of targeted number is={0}".format(search_list(lst,4)))





def num_digit(x):
    s=0
    while (x>0):
        b=x%10
        s+=b
        x//=10
    return s


x=int(input("Enter num="))
print("The sum of digits={0}".format(num_digit(x)))


####


def digit_count(x):
    count=0
    while (x>0):
        x%10
        x//=10
        count+=1
    return count

n=int(input("Enter x="))
print("The count of digit={0}".format(digit_count(x)))























