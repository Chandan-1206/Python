# Library management exercise 

class Library:
    def __init__(self):
        self.nobooks=0
        self.books=[]

    def addbooks(self,book):
        self.books.append(book)
        self.nobooks=len(self.books)

    def showinfo(self):
        print(f"The library has {self.nobooks} books. \nThe books are:")
        for book in self.books:
            print(book)

b1=Library()
b1.addbooks("The girl in the glass case")
b1.addbooks("atomic habits")
b1.showinfo()
