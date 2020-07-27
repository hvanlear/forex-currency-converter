class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


# student = Student("Bob", (90, 45, 66, 88, 99, 33))
# print(student.name)
# print(student.grades)
# print(student.average())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# when you want ot turn your object into a string
    def __str__(self):
        return f"{self.age}, {self.name}"

    def __repr__(self):
        return f"<Person({self.age}, {self.name})>"


bob = Person("Bob", 35)


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        item_dic = {name: price}
        self.items.append(item_dic)

    def stock_price(self):
        total = 0
        for dic in self.items:
            for num in dic:
                total = dic[num] + total
        return total


class Book:
    TYPES = ("HardCover", "SoftCover")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight} grams"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Harry Potter Azkaban", 1500)
# print(book)
# print(light)


## Class Inheritance ##
####
##
##

class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r}({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("disconnected")


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity


############## Class Composition ################


with open("CurrencyCodes.txt") as f:
    for line in f:
        curList = line.split("|")
        curList.pop(0)
    curList = [s.replace('-', '') for s in curList]
    curList = [item.strip() for item in curList]
    curList = [item.split(" ", 1) for item in curList]
    currencyList = curList

currencyDict = {currency[0]: currency[1] for currency in currencyList}

print(currencyDict)
