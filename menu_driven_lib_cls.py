admin_user={"aa":"pass"}
books=[]
users={}
class Lib:
    def __init__(self):
        self.admin_login=False
    def main(self):
        while True:
            print(" Main Menu \n1.Admin\n2.User\n3.Exit")
            choice=int(input("Enter choice: "))
            if choice==1:
                self.admin_sec()
            elif choice==2:
                self.user_sec()
            elif choice==3:
                print("Exit")
                break
            else:
                print("Invalid choice")
    def admin_sec(self):
        username=input("Enter username: ")
        password=input("Enter password: ")
        if admin_user.get(username)==password:
            self.admin_login=True
            while True:
                print(" Admin Menu \n1.Add Book\n2.Update Book\n3.Delete Book\n4.Display All Books\n5.Exit")
                choice=int(input("Enter choice: "))
                if choice==1:
                    self.add_book()
                elif choice==2:
                    self.update_book()
                elif choice==3:
                    self.delete_book()
                elif choice==4:
                    self.display_all_books()
                elif choice==5:
                    break
                else:
                    print("Invalid choice")
        else:
            print("Invalid username or password")
    def add_book(self):
        book_id=input("Enter book ID: ")
        for book in books:
            if book["book_id"]==book_id:
                print("Book ID exist")
                return
        title=input("Enter book title: ")
        author=input("Enter book author: ")
        quantity=int(input("Enter book quantity: "))
        books.append({"book_id": book_id, "title": title, "author": author, "quantity": quantity})
        print("Added Successfully")
    def update_book(self):
        book_id=input("Enter book_ID for updation: ")
        for book in books:
            if book["book_id"]==book_id:
                title=input("Enter new book title: ")
                author=input("Enter new book author: ")
                quantity=int(input("Enter new book quantity: "))
                book["title"] = title
                book["author"] = author
                book["quantity"] = quantity
                print("Updated Successfully")
                return
        else:
            print("Invalid book_id")
    def delete_book(self):
        book_id = input("Enter book ID: ")
        for book in books:
            if book["book_id"] == book_id:
                books.remove(book)
                print("Book deleted successfully")
                return
        print("Invalid book_id")
    def display_all_books(self):
        for book in books:
            print("Book ID:", book["book_id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Quantity:", book["quantity"])
            print()
        else:
            print("Empty books")
    def user_sec(self):
        while True:
            print(" User Menu\n1.Registeration\n2.Login\n3.Exit")
            choice=int(input("Enter choice: "))
            if choice==1:
                self.register()
            elif choice==2:
                self.login()
            elif choice==3:
                break
            else:
                print("Invalid choice")
    def register(self):
        if not self.admin_login:
            print("first login in admin")
            return
        username=input("Enter username: ")
        if username in users:
            print("Username exist")
            return
        name=input("Enter name: ")
        age=input("Enter age: ")
        address=input("Enter address: ")
        phn_num=input("Enter phn_num: ")    
        if any(user['phn_num']==phn_num for user in users.values()):
            print("Number exist")
            return
        password=input("Enter password: ")    
        users[username]={'name':name,'age':age,'address':address,'phn_num':phn_num,'password':password}  
        print("Successsfully registered")
    def login(self):
        username=input("Enter username: ")
        password=input("Enter password: ")
        user=users.get(username)
        if user and user['password']==password:
             while True:
                print(" User menu\n1.Display all books\n2.Search book by name\n3.Exit")
                choice=int(input("Enter choice: "))
                if choice==1:
                    self.display_books()
                elif choice==2:
                    self.search_book()
                elif choice==3:
                    break
                else:
                    print("Invalid choice")
        else:
            print("Invalid")
    def display_books(self):
        for book in books:
            print("Book ID:",book["book_id"])
            print("Title:",book["title"])
            print("Author:",book["author"])
            print("Quantity:",book["quantity"])
            print()

    def search_book(self):
        title=input("Enter book title: ")
        for book in books:
            if book["title"]==title:
                print("Book ID:",book["book_id"])
                print("Title:",book["title"])
                print("Author:",book["author"])
                print("Quantity:",book["quantity"])
                print()
                return
        print("Invaild book title")

a=Lib()
a.main()