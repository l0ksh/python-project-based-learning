# class Book:
#     def __init__(self,title, quantity, author, price): # The __init__ special method, also known as a Constructor, is used to initialize the Book class with attributes such as title, quantity, author, and price.
#         self.title = title
#         self.quantity = quantity
#         self.author = author
#         self.price = price
        
# book1 = Book('Book 1', 12, 'Author 1', 120)
# book2 = Book('Book 2', 18, 'Author 2', 220)
# book3 = Book('Book 3', 28, 'Author 3', 320)


# print(book1)
# print(book2)
# print(book3)
# print(type(book1))
# '''
# In Python, built-in classes are named in lower case, but user-defined classes are named in Camel or Snake case, with the first letter capitalized.
# '''

class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}"


book1 = Book('Book 1', 12, 'Author 1', 120)
book2 = Book('Book 2', 18, 'Author 2', 220)
book3 = Book('Book 3', 28, 'Author 3', 320)

print(book1)
print(book2)
print(book3)