item_number=int(input("What is the number of items?"))
user_item_list=[]
for i in range(item_number):
    item=int(input("item:"))
    if item not in user_item_list:
        user_item_list.append(item)
user_item_list.sort(reverse=True)
print(user_item_list)