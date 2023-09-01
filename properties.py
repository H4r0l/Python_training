# This code example demonstrates the usage of properties and decorators in Python.
# The class `Library` is defined to showcase the concept of using properties to control attribute access.
# It's important to note that this code uses unconventional naming conventions for demonstration purposes.

class Library:
    def __init__(self, books):
        self.books = books

    @property
    def __books__(self):
        # Getter method for the `books` attribute
        print("You have: ", self.books)

    @__books__.setter
    def set_books(self, new_book):
        # Setter method for the `books` attribute
        print("You have added: ", new_book)
        if new_book >= 1:
            self.books += new_book
        else:
            self.books = 0
        return self.books
    
    @__books__.deleter
    def delete_books(self, del_book):
        # Deleter method for the `books` attribute
        print("You have deleted: ", del_book)
        self.books -= del_book
        return self.books
    
# Setting an attribute `value` in the class `Library` with the value 20
Library.value = 20

# Printing the value of the attribute `value` in the class `Library`
print(Library.value)
