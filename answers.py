# Question-1

# class Classy():
#     dct={"tophat":2,"bowtie":4,"monocle":5}
#     def __init__(self):
#         self.items=[]
#     def addItem(self,str1):
#         if str1 in list(self.dct.keys()):
#             self.items.append(self.dct[str1])
#         else:
#             self.items.append(0)
#         return self.items
#     def getClassiness(self):
#         print(sum(self.items))
# me=Classy()
# me.getClassiness()
# me.addItem("tophat")
# me.getClassiness()
# me.addItem("bowtie")
# me.addItem("jacket")
# me.addItem("monocle")
# me.getClassiness()
# me.addItem("bowtie")
# me.getClassiness()

# Question-2

# def show_excitement():
#     return "I am super excited for this course! "*5
# print(show_excitement())

# Qusetion-4

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# new_dict={}
# for i in list(sample_dict.keys()):
#     if i=="city":
#         new_dict["location"]=sample_dict[i]
#     else:
#         new_dict[i]=sample_dict[i]  
# print(new_dict)

# Question-5

# l=list(map(int,input().split(",")))
# l_n=[]
# for i in range(len(l)):
#     if i==0 and l[i+1]<l[i]:
#         l_n.append(l[i])
#     elif i==len(l)-1:
#         if l[i-1]<l[i]:
#             l_n.append(l[i])
#     else:
#         if l[i+1]<l[i] and l[i]>l[i-1]:
#             l_n.append(l[i])
# print(*l_n,sep=" or ")

# Question-6

# l=list(map(int,input().split(",")))
# ind=int(input("K= "))
# l.sort()
# print(l[ind-1])

# Question-7
# l=list(map(int,input("List: ").split(",")))
# sm=int(input("Sum: "))
# cnt=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==sm:
#             cnt+=1
# print(cnt)

# Question-8


# l=list(map(int,input().split(",")))
# arr1=[]
# arr2=[]
# for i in l:
#     if i<0:
#         arr1.append(i)
#     else:
#         arr2.append(i)
# arr1.extend(arr2)
# print(arr1)


# Question-9

# l=list(map(int,input("List: ").split(",")))
# trgt=int(input("target: "))
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==trgt:
#             print([i,j])
#             break

# Question-10

# l=list(map(int,input("List: ").split(",")))
# l.sort()
# print((l[-1]*l[-2])-(l[0]*l[1]))

# Question-11
# l=list(map(str,input().split(",")))
# cntarr=[]
# for i in l:
#     cnt=0
#     for j in i:
#         if j.isspace():
#             cnt+=1
#     cntarr.append(cnt+1)
# print(max(cntarr))

# Question-12
# s=input()
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
        
# Question-13
# n=int(input())
# l=[]
# for i in range(1,n+1):
#     if i%3==0:
#         l.append("FIzz")
#     elif i%5==0:
#         l.append("Buzz")
#     elif i%3==0 and i%5==0:
#         l.append("FizzBuzz")
#     else:
#         l.append(str(i))
# print(l)

# Question-14
# l=list(map(int,input().split(",")))
# l_n=[]
# for i in l:
#     t=(i,i**3)
#     l_n.append(t)
# print(l_n)

# Question-15
# n=int(input())
# dct={}
# for i in range(1,n+1):
#     dct[i]=i**2
# print(dct)
