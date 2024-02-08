class LAB:
    def __init__(self):
        self.string=""
    def get_string(self):
        self.string = input()
    def print_string(self):
        print(self.string.upper)

a = LAB()
a.get_string()
a.print_string()