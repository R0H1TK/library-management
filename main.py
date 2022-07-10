class library:
    def __init__(self, listofbook):
        self.book=listofbook
    def displayavailablebook(self):
        print("book present in this library are :")
        for book in self.book:
            print (" * " + book)
    def borrowbook(self,bookname):
        if bookname in self.book:
            print(f"you have been issued{bookname} please keep it for 30 days")
            self.book.remove(bookname)
            return True
        else:
            print(f"this book of name {bookname} is not available so you can try for next")
            print(f"available book is {self.book}")
            return False
    def returnbook(self,bookname):
        self.book.append(bookname)
        print(f"thanks for returning this {bookname} book")
        print(" have a nice day")

class student:
    def requestbook(self):
        self.book=input("enter a book name for request: ")
        return self.book
    def returnbook(self):
        self.book=input("enter a book name for return: ")
        return self.book

if __name__=="__main__":
    centrallibrary=library(["algorithm","django","clrs","python"])
    

while(True):
    welcomemsg= ''' *****WElcome to central library*****
       Choose option 
    1. For books available 
    2. For requesting book
    3. For Adding/returning book
    4. exit '''
    students =student()
    print (welcomemsg)
    a =int(input("enter the choice"))

    if a==1:
       centrallibrary.displayavailablebook()
    elif a==2:
        centrallibrary.borrowbook(students.requestbook())
    elif a==3:
         centrallibrary.returnbook(students.returnbook())
    elif a==4:
        print("Thanks for visiting Central library")
        exit()
    else:
        print("you have chosen invalid input")
    

