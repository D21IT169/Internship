class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"


class Library:
    def __init__(self):
        self.books = []

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            print(book)

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def issue_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                print(f"Book '{book.title}' issued successfully.")
                return True
        print(f"Book '{book_title}' not available for issuing.")
        return False

    def return_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' returned successfully.")


def display_menu():
    print("\nMenu:")
    print("1. Display Books")
    print("2. Add Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")


def main():
    library_system = Library()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            library_system.display_books()
        elif choice == "2":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            year = input("Enter the publication year of the book: ")
            new_book = Book(title, author, year)
            library_system.add_book(new_book)
        elif choice == "3":
            title_to_issue = input("Enter the title of the book to issue: ")
            book_issued = library_system.issue_book(title_to_issue)
            if book_issued:
                print("Book issued successfully.")
        elif choice == "4":
            title_to_return = input("Enter the title of the book to return: ")
            book_to_return = Book(title_to_return, "", "")
            library_system.return_book(book_to_return)
            print("Book returned successfully.")
        elif choice == "5":
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()