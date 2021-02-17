class OwnError(Exception):
    def __init__(self):
        self.my_list = []

    def add_numbers(self):

        while True:
            try:
                numbers = int(input('Enter your numbers: '))
                numbers_1 = input('Operation completed. Stop - exit, Enter - continue:').lower()
                self.my_list.append(numbers)
                if numbers_1 == "stop":
                    print(self.my_list)
                    break
                # elif numbers < 0:
                #     raise OwnError('Don\'t use negative numbers')
            except (ValueError, OwnError):
                x = input('Please use only numbers. Stop - exit, Go - continue:').lower()
                if x == "go":
                    continue
                if x == "stop":
                    return print(self.my_list)


try_1 = OwnError()
try_1.add_numbers()
