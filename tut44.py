#MINI PROJECT- LIBRARY MANAGEMENT SYSTEM
class Library:
    def __init__(self,books,name):
        self.books=books
        self.name=name
        self.lend_record={}

    def display(self):
        print(f"the following books are available in {self.name}:")
        for books in self.books:
            print(books)

    def lend_book(self):
        inp1=input("Enter the name of the book which you want to borrow\n")
        if inp1 not in self.books:
            print("The book you mentioned does not exist")
        elif inp1 not in self.lend_record:
            name = input("Enter your name : ")
            self.lend_record[inp1] = name
        elif inp1 in self.lend_record.keys():
                print(f"Book is not available in library this book taken by {self.lend_record[inp1]}")

    def add_book(self):
        inp2=input("Enter the name of the book you want to submit in the library\n")
        self.books.append(inp2)

    def return_book(self):
        inp3=input("Enter the name of the book you want to return\n")
        if inp3 in self.lend_record:
            self.lend_record.pop(inp3)
        else:
            print("Please enter valid input")

saleha= Library(['Hindi','Telugu','English','Maths','Science','Social'],"Saleha_Library")

if __name__ == '__main__':
 while True:
      print("---------------------------------------------------------------------------------")
      inp=int(input("Press 1 to know the details of the books\nPress 2 to borrow a book\nPress 3 to add a book\n"
                  "Press 4 to return a book\nPress 5 for exit"))
      if inp==1:
        saleha.display()
      elif inp==2:
        saleha.lend_book()
      elif inp==3:
         saleha.add_book()
      elif inp==4:
         saleha.return_book()
      elif inp==5:
          break
      else:
          print("Enter valid input")





