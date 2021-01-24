product = []
specifications_1 = {}
specifications_2 = {}
item = 'Name:'
value = 'Price:'
amount = 'Amount:'
while input('Would you like to add an product? If you want press Q ') == 'Q':
    name_1 = input("Enter name: ")
    price_1 = input("Enter price: ")
    number_1 = int(input("Enter amount: "))
    specifications_1[item] = name_1
    specifications_1[value] = price_1
    specifications_1[amount] = number_1
    # print(features_1)
    break
while input('Would you like to add another one? If you want press Q ') == 'Q':
    specifications_2 = {}
    name_2 = input("Enter name: ")
    price_2 = input("Enter price: ")
    number_2 = int(input("Enter amount: "))
    specifications_2[item] = name_2
    specifications_2[value] = price_2
    specifications_2[amount] = number_2
    break
product.append(tuple([specifications_1, specifications_2]))
analytics = {
    item: [specifications_1[item], specifications_2[item]],
    value: [specifications_1[value], specifications_2[value]],
    amount: [specifications_1[amount], specifications_2[amount]]
}
print(analytics)
