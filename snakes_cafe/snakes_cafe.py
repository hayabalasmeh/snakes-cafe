
print('**************************************\n**    Welcome to the Snakes Cafe!   **\n**    Please see our menu below.    **\n**\n** To quit at any time, type "quit" **\n**************************************\n')


menu_list = {
    'Appetizers': ['Wings', 'Cookies', 'Spring', 'Rolls'],
    'Entrees': ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden'],
    'Desserts': ['Ice Cream', 'Cake', 'Pie'],
    'Drinks': ['Coffee', 'Tea', 'Unicorn Tears']

}

# print(f"Appetizers\n{menu_list['Appetizers']}")


for i in menu_list:
    print(f"\n{i}\n"+'-'*10)
    for j in menu_list[i]:
        print(j)


print('\n***********************************\n** What would you like to order? **\n***********************************\n')

all_menu_items = menu_list['Appetizers'] + \
    menu_list['Desserts'] + menu_list['Drinks'] + menu_list['Entrees']

# print(all_menu_items)

order = input('> ').lower()
orders = []
orders.append(order)
while order != 'quit':
    new_list = []
    for element in all_menu_items:

        new_list.append(element.lower())

    if(order in new_list):
        print(
            f"** {orders.count(order)} order of {order} have been added to your meal **")

    else:
        print(
            f"** The item you requested is not in the menu but {orders.count(order)} order of {order} have been added to your meal **")

    order = input('> ').lower()
    orders.append(order)


# if(order)
#orders.append(input('> '))
#print(f"** {orders.count(order)} order of {order} have been added to your meal **")
