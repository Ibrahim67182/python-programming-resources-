
class Library:
    num_books=0
    bookname=""
    books=[]


    def __init__(self):
        self.bookname=""
        self.num_books=0
    
    def add_book(self,bn):
        self.books.append(bn)
        self.num_books+=1

    def remove_book(self,na):

        for i in range(0,len(self.books)-1):
            if(self.books[i]==na):
                print(f"removing the book {i+1} : {self.books[i]}")
                self.books.pop(i)
        self.num_books-=1

    def show_books(self):
        
          if(len(self.books)==self.num_books):
              print(f"Total books available are : {self.num_books}")

              for i in range(len(self.books)):
                  print(f"Book {i+1} is {self.books[i]}")




mybook=Library()

mybook.add_book("dumb ways")
mybook.add_book("harry potter")
mybook.add_book("novel")
mybook.add_book("shadows")
mybook.add_book("abc")     

mybook.remove_book("novel")

mybook.show_books()

