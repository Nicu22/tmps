# importing sys
import sys
 
# adding foctory to the system path
sys.path.insert(1, '/home/niciu/lab1/factory')
 
# importing the hello
from library_factory import LibraryFactory

def main():
    library_service = LibraryFactory.create_library_service()

    # Adding books and users
    library_service.add_book("Mr Mercedes", "Stephen King", "978-0567839021")
    library_service.add_book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
    library_service.add_book("To Kill a Mockingbird", "Harper Lee", "978-0446310789")
    

    library_service.add_user("john_doe", "john@example.com")
    library_service.add_user("jane_smith", "jane@example.com")
    library_service.add_user("smith_doe", "smith@example.com")

    # Listing books and users
    print("Books in the library:")
    for book in library_service.list_books():
        print(book)

    print("\nUsers of the library:")
    for user in library_service.list_users():
        print(user)

if __name__ == "__main__":
    main()
