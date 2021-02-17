class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def extract(cls, data):
        # d, m, y = [int(i) for i in data.split('-')]
        d, m, y = map(int, data.split('-'))
        return d, m, y

    @staticmethod
    def valid(data):
        d, m, y = map(int, data.split('-'))
        if d <= 31 and d != 0 and m <= 12 and m != 0:
            return d, m, y


try1 = '10-12-2021'
print(Data.extract(try1))
print(Data.valid(try1))
