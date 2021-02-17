class Warehouse:
    def __init__(self):
        self.all_items = []
        self.printer = []
        self.scanner = []
        self.xerox = []

    def supply(self):
        while input('Would you like to add an item? ') == 'yes':
            try:
                a = int(input(f'Which one?\n 1 -- Printer\n 2 -- Scanner\n 3 -- Xerox\n'))
                if a == 1:
                    printer_name = input("Enter printer's name: ")
                    printer_price = int(input("Enter printer's price: "))
                    printer_quantity = int(input("Enter printer's amount: "))
                    product_dict = {'Model': printer_name, 'Quantity': printer_price, 'Cost': printer_quantity}
                    self.all_items.append(product_dict)
                    self.printer.append(product_dict)
                    print(self.printer)
                elif a == 2:
                    scanner_name = input("Enter scanner's name: ")
                    scanner_price = int(input("Enter scanner's price: "))
                    scanner_quantity = int(input("Enter scanner's amount: "))
                    product_dict = {'Model': scanner_name, 'Quantity': scanner_price, 'Cost': scanner_quantity}
                    self.scanner.append(product_dict)
                    self.all_items.append(product_dict)
                    print(self.scanner)
                elif a == 3:
                    xerox_name = input("Enter xerox's name: ")
                    xerox_price = int(input("Enter xerox's price: "))
                    xerox_quantity = int(input("Enter xerox's amount: "))
                    product_dict = {'Model': xerox_name, 'Quantity': xerox_price, 'Cost': xerox_quantity}
                    self.xerox.append(product_dict)
                    self.all_items.append(product_dict)
                    print(self.xerox)

            except ValueError:
                print('Enter valid data')


class Equipment(Warehouse):
    def __str__(self):
        return 'Welcome to Hell'


class Printer(Equipment):
    def __str__(self):
        return 'I\'m Printer! I can print stuff!'


class Scanner(Equipment):
    def __str__(self):
        return 'I\'m Scanner! I can scan things.'


class Xerox(Equipment):
    def __str__(self):
        return 'I am Xerox. I can xerox documents...'


item1 = Warehouse()
printer = Printer()
scanner = Scanner()
xerox = Xerox()
print(item1.supply())
print(item1.all_items)
print(printer)

print(scanner)
print(xerox)
