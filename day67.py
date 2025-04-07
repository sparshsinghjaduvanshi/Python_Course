class library:
    def __init__(self):
        self.nobook = 0
        self.books = []

    def addbook(self,book):
        self.books.append(book)
        self.nobook = len(self.books)

    def showinfo(self):
        print(f"The library has {self.nobook} books. \nthe books are:- ")
        for book in self.books:
            print(book)

l = library()
l.addbook("harry poter 1")
l.addbook("harry poter 2")
l.addbook("harry poter 3")
l.addbook("harry poter 4")
l.showinfo()