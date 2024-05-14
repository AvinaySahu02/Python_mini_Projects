#Define the menu of restaurant
menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
}
print(menu)
#Greet
print('Welcome to SAHU CAFE!!')
print('Pizza: Rs40\nPasta: Rs 50\nBuger: Rs60\nSalad: Rs70\nCoffee: Rs80')

order_total = 0
#80 + 70 = 150

item_1 = input('Enter the name of the item you want to order = ')
if item_1 in menu:
    order_total += menu[item_1]  #0 + 50
    print(f'Your item {item_1} has been added to your order')
else:
    print(f'Ordered item {item_1} is not availabel yet!')

another_order = input('Do you want to add another item? (Yes/No)')
if another_order == 'Yes':
    item_2 = input('Enter the name of second item =')
    if item_2 in menu:
        order_total += menu[item_2]
        print(f'Item {item_2} has been added to order')
    else:
        print(f'Ordered item {item_2} is not availabel!')

print(f'The total amount of items to pay is {order_total}')