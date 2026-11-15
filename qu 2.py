class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_info(self):
        print(f"Book title: {self.title} | Author: {self.author}")
book1 = Book("The alchemist", "Paulo Coelho")
book2 = Book("To kill a mockingbird", "Harper Lee")
book3 = Book("1984", "Garoge Orwell")
book1.display_info()
book2.display_info()
book3.display_info()