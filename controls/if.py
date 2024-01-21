text = """
Conditional operators
1. Equality:
  ==: Equal to
  !=: Not equal to

2. Comparison:
  <: Less than
  >: Greater than
  <=: Less than or equal to
  >=: Greater than or equal to

3. Membership:
  in: Checks if a value exists in a sequence (e.g., list, tuple, string)
  not in: Checks if a value does not exist in a sequence

4. Identity:
  is: Checks if two variables refer to the same object
  is not: Checks if two variables do not refer to the same object

"""

print(text)

#simple if and else 

if 10 > 20 :
  print("10 is greater than 20 ")
elif 10 > 15:
  print("10 is greater than 15")
else :
  print("10 is neither greater than 20 and 15")


print("do we have ternary operator like a > b ? True : False ")
print("Answer is No. However python has implemented ternary condition expression through if ")

#Ternary expression
result = True if 0 > 1 else False
print("Ternary result: ", result)

print("Do we have === in python? ")
print("Answer is No")
# === operator
# if 10 === 10 :
#   print("true with type check")
# else:
#   print("Flase with type check")

print("What is alterate to do type check? ")

def is_number(x):
  result = 'number' if isinstance(x, (int, float, complex)) else 'Not a number'
  print(f"given {x} is {result}")

is_number(42)   # True
is_number(3.14)   # True
is_number(5 + 2j)   # True
is_number("Hello")

print("Another way to check is type(variable) == data_tyep ")

if type(10) == int:
  print("10 in integer")
else:
  print("10 is not an integer")

print("check the value is in the list, tuple, string or not")
a = 10 
item_list = [10, 20, 30]
item_tuple = (20, 10, 30)
item_string = "welcome"
b = "come"
if a in item_list:
  print(f"{a} is in the item_list")
else:
  print(f"{a} is not in the item_list")

if a in item_tuple:
  print(f"{a} is in the item_tuple")
else:
  print(f"{a} is not in the item_tuple")

if b in item_string:
  print(f"{b} is in the item_string")
else:
  print(f"{b} is not in the item_string")

print("are we able to check the dictonary since it is key value pair")
dict_item = {"suba": "Back end dev", 'venkat': "Front end dev", 'Gutti': 'ML dev'}
key = "suba"
if key in dict_item:
  print(f"{key} is in the dict_item")
key = "test"
if key not in dict_item:
  print(f"{key} is not in the dict_item")


value = "Front end dev"
if value in dict_item.values():
  print(f"{value} is in the dict_item")
value = "developer"
if value not in dict_item.values():
  print(f"{value} is not in the dict_item")

if 10 not in [1, 2, 4 ,5 ]:
  print(f"10 is not in the list")

# indendity check (is and not is )
list1 = [1, 2 , 3 ]
list2 = [1, 2, 3]
list3 = list1

def check_same_object(obj1, obj2):
  if obj1 is obj2:
    print(f"obj1 and obj2 are in the same object")
  if obj1 is not obj2:
    print(f"obj1 and obj2 are not in the same object")

check_same_object(list1, list2)
check_same_object(list1, list3)
