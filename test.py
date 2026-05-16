#TO RUN USE SHORTCUT CTRL R AND THEN CTRL R
# {import pandas #learning about different packages in python
# # Learning about printing statements
# print("Hello world")
# print(4)
# # heyy
# # hello
# print("hello\nhow are you")
# """
# hey 
# hey
# hey 
# """
# print("hey",8,9,sep="-", end="yyyy\n")
# print("why")
# print("hey",8,9,sep="-")


#DATA TYPES
# a= complex(5,7)
# b= "word"
# c= True
# d= None
# e=8.9
# f= 7
# g='a'
# print("a= ", type(a))
# print("b= ", type(b))
# print("c= ", type(c))
# print("d= ", type(d))
# print("e= ", type(e))
# print("f= ", type(f))
# print("g= ", type(g))


# print(ord('a'))
# print(ord('&'))
# print(chr(65))



# '''
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Dictionary is a collection which is ordered and changeable. No duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# *Set items are unchangeable, but you can remove items and add new items.
# '''

# """LIST"""
# list1 =[8, 2.3, [-4, 5], ["apple", "banana"]]
# print(list1)
# print(list1[2][1])
# print(list1[2])
# print(list1[3][1])
# print("banana= ", type(list1[3][1]))
# print("list = ", type(list1))

# """TUPLE"""
# tuple1 = ("abc", 34, True, 40.5, "male", ('apple', 'banana'), "male") # note the double round-brackets
# print(tuple1)
# print(tuple1[5][1])
# print(tuple1[5][1][0])

# thistuple = ("apple",) #the comma makes this a turple
# print(type(thistuple))#tuple

# #NOT a tuple
# thistuple = ("apple") #not a tuple since no comma 
# print(type(thistuple)) #str


# """DICTIONARY"""
# dict1 = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", 2] #list
# }
# print(dict1)
# print(dict1["colors"][0][2])#d

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", 2],
#   "year": 1964 # total duplicate is ignored in result
# }
# print(thisdict) 

# thisdict1={
#     "brand": "ferrari",
#     "year": 1950,
#     "series": ("f1", "indy", "fe", ('cl16','lh44'), 6), #tuple
#     "colors": ["red", "white", 2],
#     "year": 1934 #new year value will takeover and 1950 will get relaced by 1934
# }
# print(thisdict1)
# print(thisdict1["series"][3][0][0])#c


# """SET"""
# set1 = {"abc", 34, True, 40, "male", 1, 0, False} #true and 1 are considered duplicates as well as false and 0 and thus one of them is ignored (whatever comes later than the other)
# print(set1) #sets are unorganised and unindexed so output is in random order 

# set2 = { "abc", 1, True, 5.8, ("f1", "indy", "fe", ('cl16','lh44'), 6)} #sets cannot contain lists but can contain tuple becuse tuple are immutable and lists arent
# print(set2)#also tuples are only allowed in sets as long as they contain only immutable elements so no lists, dicts, or sets within a tuple 


# '''ARITHMATIC OPERATORS'''
# print(5+6)    #addition
# print(5-6)    #subtraction
# print(15*6)   #multiplication
# print(15/6)   #divison (integral with fraction =2.5)
# print(15//6)  #floor division (just intergral part =2)
# print(5%2)    #modulation remainder(1)
# print(2**4)   #exponentiation (2 to the power 4)

# #calculator
# # a=30
# # b=10
# # print("the value of",a,"+",  b,"is=", a+b)
# # print("the value of",a,"-",  b,"is=", a-b)
# # print("the value of",a,"*",  b,"is=", a*b)
# # print("the value of",a,"/",  b,"is=", a/b) 
# # print("the value of",a,"//", b,"is=", a//b)
# # print("the value of",a,"%",  b,"is=", a%b)
# # print("the value of",a,"**", b,"is=", a**b)

# '''alt daba ke click karna and then click somewhere else and it will work like how shift select works
# alt shift downwards key duplicates in downward direction'''


# """TYPECASTING"""
# '''
#    int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents an integer)
#    float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
#    str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
#    list()
#    tuple()
#    dict()
#    set()
# '''

# y = int(2.8)   # y will be 2
# x = int("-3")  # x will be -3

# # m= int("you")
# # print(m) will throw an error since int() works only for base10 numbers

# z = float("3") # z will be 3.0
# y = str(2)     # y will be '2'
# z = str(3.0)   # z will be '3.0'

# # Convert decimal to hexadecimal
# print(hex(255))  # Output: '0xff'
# print(hex(-42))  # Output: '-0x2a'
# # Convert decimal to octal
# print(oct(10))   # Output: '0o12'
# print(oct(64))   # Output: '0o100'
# print(oct(-10))  # Output: '-0o12'

# a="1"
# b="2"
# t=a+b
# print("a+b= ",t, " and its type is: ", type(t))
# u=int(a+b)
# print("int(a+b)=",u, " and its type is: ", type(u))
# v=int(a)+int(b)
# print("int(a)+int(b)=",v, " and its type is: ", type(v))


# t5= list(("apple", "banana", "cherry")) # note the double round-brackets, it was a tuple before
# print("t5=", type(t5)) #list

# tu3 = tuple(t5) # turning t5(a list now) into a tuple
# t6= tuple(["apple", "banana", "cherry"])# turning a list into a tuple
# print("tu3=", type(tu3))#tuple
# print("t6=", type(t6)) #tuple

# dict5 = dict(name = "John", age = 36, country = "Norway")# turning a group of variables to a dict 
# print(dict5)
# print("dict5=", type(dict5))

# set5= set(("apple", "banana", "cherry")) # note the double round-brackets
# print(set5)
# set6= set(dict5)
# print(set6)# {'country', 'name', 'age'}
# set7= set(t5)
# print(set7)

# """USER INPUT"""

# print("Enter your name:")
# a = input() #asking input in the next line
# print("My name is", a)


# a=input("Enter your name:")#asking input in the same line
# print("My name is",a)


# print("My name is", input("Enter your  name :"))#asking input in the same line


# print("Enter your name:")
# a = input() #asking input in the next line
# print(f"Hello {a}")
# print("Hello {a}")

# a = input("Enter your name:") #asking input in the same line
# print(f"My name is {a}")

# x = input("Enter first number: ")#5
# y = input("Enter second number: ")#5
# print(x + y) #will give xy instead of x+y (concatination instead of addition)#55
# print(int(x)+int(y))#10

# # a =int(input("Enter first number : ")) 
# # b =int(input("Enter second number : "))

# # print(a+b)
# # print(a-b)
# # print(a*b)
# # print(a/b)

# a =input("Enter first number : ") 
# b =input("Enter second number : ")


# print("Addition: ",     int(a) + int(b))
# print("Subtraction",    int(a) - int(b))
# print("Multiplication", int(a) * int(b))
# print("Division",       int(a) / int(b))
# print("Floor Division", int(a) // int(b))
# print("Modulation",     int(a) % int(b))
# print("Exponent",       int(a) ** int(b))



# print("He said, \"I would like an apple\"")
# print('He said, "I would like an apple"')
# print("He said, 'I would like an apple'")

# a= """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla eget tellus ullamcorper, 
# eleifend risus ac, laoreet felis. Nullam congue at arcu a aliquam. Suspendisse ut congue nunc. 
# Pellentesque sed nunc lectus. Nullam pharetra, nisl non blandit porttitor, leo libero placerat nunc,
# ut convallis nisl lectus et mi. Fusce faucibus ultricies vestibulum. Nulla vulputate a mi at 
# suscipit. Nunc vel eros luctus, porttitor felis non, consectetur quam. 
# Proin aliquet dictum neque, at accumsan nulla facilisis nec.

# Vivamus volutpat augue eu ligula consequat fringilla. Nulla ultricies felis feugiat,
# mollis ipsum sit amet, vulputate justo. Vestibulum feugiat iaculis enim eu lacinia. 
# Aenean eget nulla in metus condimentum bibendum. Curabitur nec felis justo. Praesent tortor justo,
# gravida lobortis mi varius, malesuada luctus erat. Integer at ultricies purus, quis fringilla libero. 
# Ut tristique metus odio, ut tempor turpis porta a. Maecenas at metus nulla.

# Vivamus porta aliquam risus. Nunc tempus tortor non elit consequat feugiat. 
# Etiam blandit nunc in tellus accumsan, eu mattis ligula auctor. Vivamus hendrerit feugiat arcu 
# in accumsan. Vivamus sodales, justo sit amet convallis malesuada, mauris dui fermentum tellus, 
# commodo egestas risus velit et augue. Phasellus in lacinia sem. Etiam ut nisi sed mauris tempus 
# condimentum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. 
# Aenean viverra mauris ut purus sollicitudin, ac tempus orci blandit. Nunc hendrerit, risus quis 
# vulputate tincidunt, ligula nunc gravida metus, quis placerat eros dolor non libero. 
# Cras elementum elementum dignissim. Proin pharetra nec dui at eleifend. 
# Phasellus condimentum quam eget ornare vestibulum. Vivamus sodales erat id mauris suscipit tincidunt. 
# Ut id suscipit risus, vitae hendrerit augue."""
# print(a)
# print("hey hey hey\n")

# print('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla eget tellus ullamcorper, 
# eleifend risus ac, laoreet felis. Nullam congue at arcu a aliquam. Suspendisse ut congue nunc. 
# Pellentesque sed nunc lectus. Nullam pharetra, nisl non blandit porttitor, leo libero placerat nunc,
# ut convallis nisl lectus et mi. Fusce faucibus ultricies vestibulum. Nulla vulputate a mi at 
# suscipit. Nunc vel eros luctus, porttitor felis non, consectetur quam. 
# Proin aliquet dictum neque, at accumsan nulla facilisis nec.

# Vivamus volutpat augue eu ligula consequat fringilla. Nulla ultricies felis feugiat,
# mollis ipsum sit amet, vulputate justo. Vestibulum feugiat iaculis enim eu lacinia. 
# Aenean eget nulla in metus condimentum bibendum. Curabitur nec felis justo. Praesent tortor justo,
# gravida lobortis mi varius, malesuada luctus erat. Integer at ultricies purus, quis fringilla libero. 
# Ut tristique metus odio, ut tempor turpis porta a. Maecenas at metus nulla.

# Vivamus porta aliquam risus. Nunc tempus tortor non elit consequat feugiat. 
# Etiam blandit nunc in tellus accumsan, eu mattis ligula auctor. Vivamus hendrerit feugiat arcu 
# in accumsan. Vivamus sodales, justo sit amet convallis malesuada, mauris dui fermentum tellus, 
# commodo egestas risus velit et augue. Phasellus in lacinia sem. Etiam ut nisi sed mauris tempus 
# condimentum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. 
# Aenean viverra mauris ut purus sollicitudin, ac tempus orci blandit. Nunc hendrerit, risus quis 
# vulputate tincidunt, ligula nunc gravida metus, quis placerat eros dolor non libero. 
# Cras elementum elementum dignissim. Proin pharetra nec dui at eleifend. 
# Phasellus condimentum quam eget ornare vestibulum. Vivamus sodales erat id mauris suscipit tincidunt. 
# Ut id suscipit risus, vitae hendrerit augue.''') }

for x in "banana":
  print(x)

a='He said, "I would like an apple".'

for x in a:
  print(x)

fruit = "Mango"#M(0),a(1),n(2),g(3),o(4)
length = len(fruit)
print(length)#5
print(fruit[0:4])#0 to 3(4-1)  including 0 but not 4  Mang
print(fruit[1:4]) #1 to 3      including 1 but not 4  ang
print(fruit[:5]) #0 to 4                              Mango
print(fruit[0:]) #0 to length(5)-1 so 0 to 4          Mango
print(fruit[:])#0 to len-1 so                         Mango
print(fruit[0:-3]) #0 to (len-3)-1 so 0 to 1          Ma
print(fruit[:len(fruit)-3])# 0 to (5-3)-1 so          Ma
print(fruit[-1:len(fruit) - 3])# len-1 to (len-3)-1 so 4to1 which is not possible so no output just blank
print(fruit[-3:-1]) #len -3 to (len-1)-1 so 2 to 3 so ng
print(fruit[-2:])#len-2 to len-1 so                   go

a="Apple"
print(a[-4:-2])#len-4 to (len-2)-1 so from 1 to 2 so  pp

pie="applepie"
print(pie[:5]) #Slicing from Start                    apple
print(pie[5:])#Slicing till End                       pie

"""STRING METHODS"""
str1="  !!AbcDeFG!!"
print(str1.upper())

print(str1.lower())

print(str1.strip())
print(str1.strip("!"))
print(str1.rstrip())
print(str1.rstrip("!"))
print(str1.lstrip())
print(str1.lstrip("!"))

print(str1.replace("!","*"))
print(str1.replace("!","*",count=3))

str2="Silver Spoon"
print(str2.split(" "))
print(str2.split())
print(str2.split("o"))
print(str2.split("o",maxsplit=1))
print(str2.split("k"))

str3="hello welcome to my file."
print(str3.capitalize())
