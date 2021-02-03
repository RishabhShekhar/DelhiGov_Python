# print("Day 2")

# n1 = 1
# while n1<10:
# 	print(n1)
# 	n1 += 1

# name = "Rishabh Shekhar"

# n = 8

# while n!= len(name):
# 	print(name[n])
# 	n += 1

#Nested Loops
# a = "abc"
# for i in range(5):
# 	for j in a:
# 		print(i,j)

'''
* * * *
* * * *
* * * *
* * * *
'''
# for i in range(4):
# 	print("* "*4)

# a = "ab "
# print(a*8)

'''
* 
* * 
* * *
* * * *
'''

# for i in range(1,5):
# 	print("* "*i)

# for i in range(1,5):
# 	for j in range(i):
# 		print("*", end=" ")
# 	print()

'''
1 
1 2 
1 2 3
1 2 3 4
1 2 3 4 5
'''
# for i in range(2,7):
# 	for j in range(1,i):
# 		print(j, end=" ")
# 	print()

# for i in range(1,6):
#     for j in range(i):
#     	print(j+1,end=" ")
#     print()

# LIST

# l = [1,2,True,8.9,"Rishabh"]
# print(l[-1][-1])

#Nested Lists

# nl = [[1,2,3],4]
# print(nl[0][1])

# ll = [[1,2,3,4],
# 	 [6,7,[8,9,[10,11]],[12,13,[14,15]],[16,[17]]],
# 	 [18]]

# print(ll[0][1])
# print(ll[1][1])
# print(ll[1][2][0])
# print(ll[1][2][2][0])
# print(ll[-1][0])
# print(ll[1][3][2][1])

# l = [1,2,3,4,5]
# print(l)

# a = 6
# b = [10,20]
# l.append(b)
# l.extend(b)
# print(l)

l = [2,1,43,1,5,23,1]
# count = 0
# for i in l:
# 	if i == 1:
# 		count += 1
# print(count)
# print(l.count(1))

# print(l.index(1))

# l.sort()
# l.sort(reverse = True)
# print(l)
# a = sorted(l)
# print(l)
# # print(a)

# l.reverse()
# print(l)

# print(l)
# print(l.pop())
# print(l)
# l.pop(2)
# print(l)

# print(l)
# l.remove(1)
# print(l)

# print(l)
# l.insert(2,29)
# print(l)

#mutable immutable

# name = "Rishabh Shekhar"
# name = name.replace("R","r")
# print(name) 

# l = [1,3,2]
# l[0]= 43
# print(l)


# print(name.title())
# print(name.capitalize())


# a = "hello  world"
# print(a.title()) # First letter of every word
# print(a.capitalize()) #First letter of first word




# Fetching all indexes of one value and explore atleast 10 methods of strings

#Tuple
# t = (1,2,3,4,5,1)
# print(t[2])
# print(t.count(1))
# print(t.index(4))

# l =[1,2,3]
# print(type(l))
# l = tuple(l)
# print(type(l))

#SET
# l = [1,2,3,1]
# l = set(l)
# print(l)

# s1 = {222,4452,722,45,89}
# s2 = {23,4452,722,67,92}

# print(s1.intersection(s2))
# print(s1.union(s2))



# a = 10
# print(id(a))
# b = 10
# print(id(b))

#Dictionary


Wagonr = {
	"Company":["Maruti","Suzuki"],
	"Year": 1990,
	"Finance": True
}

# print(Wagonr)
# print(Wagonr["Company"])
# print(Wagonr["Company"][-1])

# print(len(Wagonr))
# print(Wagonr.keys())
# print(Wagonr.values())
# print(Wagonr.items())

# print(Wagonr)
# Wagonr.update({"Year":2000})
# Wagonr.update({"Colour":"Blue"})
# print(Wagonr)

# for i in Wagonr.keys():
# 	print(i)

# Nested Dictionary

# Car = {
# 	"Alto":{
# 	"Colour": "Red",
# 	"Year": 1994,
# 	"Company": "Maruti"
# 	},
# 	"Fortuner":{
# 	"Colour": "White",
# 	"Year": 1994,
# 	"Company": "Toyota"
# 	}
# }

# print(Car["Fortuner"]["Year"])
# print(Car["Alto"]["Company"])

#Functions

# def helloworld():
# 	print("hello world")

# helloworld()

# def add_num(n,a):
# 	return n+a

# a = add_num(10,20)
# print(a)

#Default Parameters --> Default Parameters must come in last
# def add_num(n,a=5): 
# 	return n+a

# a = add_num(10,3)
# print(a)

# def table(n):
# 	for i in range(1,11):
# 		print(str(n)+" X "+ str(i)+" = "+str(i*n))


# table(13)
# table(17)
# table(23)

# def sort1(a):
# 	a.sort()
# 	return a

# l = [12,14,6,22,231]
# print(sort1(l))


# def count_vowels1(s):
# 	s = s.lower()
# 	a = 0
# 	e = 0
# 	i = 0
# 	o = 0
# 	u = 0
# 	vow = "aeiou"
# 	for j in s:
# 		if j in vow:
# 			if j == "a": a+=1
# 			elif j == "e": e+=1
# 			elif j == "i": i+=1
# 			elif j == "o": o+=1
# 			elif j == "u": u+=1

# 	print("a :",a)
# 	print("e :",e)
# 	print("i :",i)
# 	print("o :",o)
# 	print("u :",u)

# count_vowels1("sdOpiugdfsghsdcdscedsccghasfhaqwertyuioplkjhbvbnmnbvcxzawe")


# def count_vowels2(s):
# 	s = s.lower()
# 	l = [0, 0, 0, 0, 0]
# 	vow = "aeiou"
# 	for j in s:
# 		if j in vow:
# 			if j == "a": l[0]+=1
# 			elif j == "e": l[1]+=1
# 			elif j == "i": l[2]+=1
# 			elif j == "o": l[3]+=1
# 			elif j == "u": l[4]+=1

# 	print("a :",l[0])
# 	print("e :",l[1])
# 	print("i :",l[2])
# 	print("o :",l[3])
# 	print("u :",l[4])

# count_vowels2("sdOpiugdfsghsdcdscedsccghasfhaqwertyuioplkjhbvbnmnbvcxzawe")


# def count_vowels3(s):
# 	s = s.lower()
# 	d = {
# 		"a": 0,
# 		"e": 0,
# 		"i": 0,
# 		"o": 0,
# 		"u": 0
# 	}
# 	vow = "aeiou"
# 	for j in s:
# 		if j in vow:
# 			if j == "a": d["a"]+=1
# 			elif j == "e": d["e"]+=1
# 			elif j == "i": d["i"]+=1
# 			elif j == "o": d["o"]+=1
# 			elif j == "u": d["u"]+=1

# 	print(d)

# count_vowels3("sdOpiugdfsghsdcdscedsccghasfhaqwertyuioplkjhbvbnmnbvcxzawe")

def count_vowels4(s):
	s = s.lower()
	d = {
		"a": 0,
		"e": 0,
		"i": 0,
		"o": 0,
		"u": 0
	}
	vow = "aeiou"
	for j in s:
		if j in vow:
			d[j]+=1
	print(d)

count_vowels4("sdOpiugdfsghsdcdscedsccghasfhaqwertyuioplkjhbvbnmnbvcxzawe")
