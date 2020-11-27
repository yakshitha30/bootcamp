#creating a list
n = int(input("enter the size of list:"))
my_list = []
for i in range(n):
    item = int(input())
    my_list.append(item)
print(my_list)
#adding an item into list
item = int(input("enter the item to be added in the list:"))
my_list.append(item)
print("list after appending: ",my_list)
#delete
item = int(input("Enter the item to be deleted: "))
my_list.remove(item)
print("list after removing the selected item ",my_list)
#largest number in the list
largest_value = max(my_list)
print("Largest value in the list ",largest_value)
#Smallest value in the list
smallest_value = min(my_list)
print("Smallest value in the list",smallest_value)
