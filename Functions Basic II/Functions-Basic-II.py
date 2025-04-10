#Countdown 
def countDown(a):
    for x in range(a,-1,-1):
        print(x)

countDown(5)
# Print and Return
def print_and_return(a,b):
    print(a)
    return b
print_and_return(5,4)
# First Plus Length
def first_plus_length(list):
    return list[0]+len(list)
print(first_plus_length([1,2,3,4,5]))
#Values Greater than Second
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    list2 = []
    second_value = list[1]
    for i in list:
        if i > second_value:
            list2.append(i)
    print(len(list2))
    return list2   
print(values_greater_than_second([5,2,3,2,1,4]))
# This Length, That Value
def length_and_value(size,value):
    for i in range (0,size,1):
        print(value)

length_and_value(5,2)