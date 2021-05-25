def find_item(list, item):
    if item in list:
        return True
    else:
        return False

list = ["Item","History","Science","Hi","Find"]    
item = input("Enter item to search: ")

print(find_item(list,item))