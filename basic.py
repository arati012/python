print("hello world, arati here")           #printing the first code
name = "arati"                   #variable
print(name)
Name  = "ravi"
print(Name)
number  = 100
print(number)
num = 11.456
print(num)
print(5 + 5 * 10)

##################################### STRING ###################################
name = "arati"        # 01234-indexing
print(name[0:2])
print(name[4])
print(type(name))     # printing the type of sequence
num = 100.5
print(type(num))
var = True
print(type(var))
print(len(name))      #printing the length of sequence
name = "arati"               # as a string
name_upper = "ARATI"         # as a string
print(name.upper())          # Converting into upper case
print(name_upper.lower())    # Converting into lower case
print(name.swapcase())
print(name.title())          # first letter capital
print(name.replace("arati", "ravi"))

name ="arati"
last_name ="kumari"
print(name + " " + last_name)
print(name.find("r"))        #element present in string or not
print(name.capitalize())     # first letter capital

print("My name is ",name, "and my last name is ",last_name)   # proper way of printing
print(3 * name)                                               # printing name 3 times
print(f"my name is {name} and my last name is {last_name}")
print(name.replace("i", "u"))                                 #replace the first occurence of letter i
print(name.replace("i", "u", 1))

text =  " hello world "
print(text.replace("world", "python"))
print(text.index("world"))                                     # finding the first index of letter world

############################ LIST ###################################

my_list = [1,2,3,4,5,6,7,8,5,5,4,3,5,53]                          # OPERATIONS ON LIST
print(type(my_list))
my_list1 = [1,"ravi",3,5.8,True,6,55]
print(type(my_list1))
print(my_list1)
print(my_list)
print(my_list[2])


my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list[-1])               # indexing
print(my_list[-2])
print(my_list[-3])
print(my_list[-4])
print(my_list[-5])

print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])
print(my_list[5])

my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list[1:5])              #slicing
print(my_list[:5])
print(my_list[1:])
print(my_list[:])

print(len(my_list))
my_list.append(100)             # adding element at back
print(my_list)
my_list.insert(1,100)           # inserting an element
print(my_list)
my_list.remove(5)               # removing an element from specific postion/index
print(my_list)
my_list.pop()         
print(my_list)
print(my_list.index(3))         # finding index of 3
my_num = [5,4,3,2,1]
my_num.sort()                   # arranging the elements of list
my_num.clear()
print(my_num)


############################# TUPLE ###################################
tpl = (1,2,3,4,5)                                               # OPERATIONS ON TUPLE
print("tpl:-",tpl)
print("type of tpl:-",type(tpl))
print("len  of tpl:-",len(tpl))
print(" element at o postion :-",tpl[0])             # elements at different index
print(" element at 1 position:-",tpl[1])
print(" element at 2 position:-",tpl[2])
print(" element at 3 position:-",tpl[3])
print(" element at 4 position:-",tpl[4])


tpl = (1,2,3,4,5)
print("element from index 0 to 2 :-",tpl[0:2])        # slicing
print("reversing:-",tpl[::-1])  
print(tpl[1:-1])

print(2 in tpl)                   # elements are present in tuple or not                      
print(10  in tpl)

print("maximum of tpl:-",max(tpl))               # finding maximum element from list
print("minimum of tpl:-",min(tpl))               # minimum value
print("sum of all elements in tuple:-",sum(tpl)) # sum of all elements in a list

tpl2 = 1,2,3
print(type(tpl2))
print(tpl2)

arati = 1,2,3        # tuple unpacking
a,b,c = arati
print("a:-",a)
print("b:-",b)
print("c:-",c)

######################################## DICTIONARY ######################################

dct = {
    "name" : "arati",
    "last_name" : "kumari",
    "age" : 19
}                                                     # operaions on dictionary
print("dict type:-",type(dct))                        # type    
print("dictionary :-",dct)
print(dct["name"])
print("name :-",dct["name"])                          # arati
print("last_name :-",dct["last_name"])                # kumari
print("age :-",dct["age"])                            # 19
print("dct keys:-",dct.keys())                        # printing all keys
print("dct values:-",dct.values())                    # printing all values
print("dct items:-",dct.items())                      # printing all items

dct['Gender'] = "Male"                             # Add new key-value pair
print(dct)

dct['age'] = 22                                    # updating the value of age
print(dct)


#del dct['last_name']                               # deleting key using del keyword
print(dct) 
dct.pop("last_name")                             # deleting key using pop
print(dct)

#dct.clear()
print(dct)
print('name' in dct)                             # key or value is present or not
print('arati' in dct)

dct1 = dct.copy()                                # copying the items of dct into dct1
print(dct1)
copy_dct=dct.copy()
print("copy dict ",copy_dct)
print("original dict ",dct)

dct2 = {                                         # merging dictionaries
    "ravi_name" : "ravi",
    "ravi_age" : 21
 } 

dct3 = {
    "sonu_name" : "sonu",
    "last_name" : "kumar",
    "sonu_age" : 21
 } 

dct2.update(dct3)
print(dct2)

key = ["a","b","c"]                          # siiting all values to specific single value
default_dict=dict.fromkeys(key, 0)
print(default_dict)

########################################## SET ######################################

my_set = {1,2,3,4,5,"ravi"}                           # operations on set
print(type(my_set))
print(my_set)
my_set.add(100)                                       # adding elements
my_set.add("kumari")
my_set.add("vinay")
print(my_set)
my_set.remove("ravi")                                 # removing elements
print("remove element:-",my_set)
my_set.discard(5)
print("discard element:-",my_set)
my_set.pop()
print("pop element:-",my_set)
my_set.clear()
print("clear element:-",my_set)

####################### OPERATORS ##########################  
#arithmatic :
a = 10
b = 5
print(a+b)   
print(a-b)   
print(a*b)   
print(a/b)   
print(a//b) 
print(a%b)  
print(a**b)

#Comparison:
a = 10
b = 5
print(a==b)  
print(a!=b)  
print(a>b)   
print(a<b)   
print(a>=b)  
print(a<=b)

#Assignment:
a=1
a += 6
print(a) 
a -= 4
print(a)   
a *= 3
print(a)  

#logical:
a=5
print(a>2 and a<10)  
print(a<2 or a>3)    
print(not(a>3))

# bitwise:
a = 5   
b = 4      
print(a & b)   
print(a | b)   
print(a ^ b)

# membership:
name="arati"
print('r'in name)
print('k' not in name)

# identity:
a=[1,2,3]
b=[1,3,2]
c=[4,5,6]
print(a is b)
print(a is not c)


#updating the key in dictionary
mydict = {
    "name":"arati",
    "last_name":"kumari",
    "age ": 19
}
print(mydict)
mydict["full_name"] = mydict["name"]
del mydict["name"]
print(mydict)