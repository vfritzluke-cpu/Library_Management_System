from book import Book
from member import Member
from loan import Loan
from exceptions import *

books = [
    Book("B001", "The Midnight Library", "Matt Haig"),
    Book("B002", "Project Hail Mary", "Andy Weir"),
    Book("B003", "Circe", "Madeline Miller"),
    Book("B004", "Educated", "Tara Westover")
]

members = [
    Member("M001", "Fritz Villas", "fritzv@email.com")
]

loans = []


def main():
    while True:

        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Books")
        print("6. View Members")
        print("7. View Loans")
        print("8. Exit")

        try:
            choice = input("Choose an option: ")

            # Validation: Invalid Menu Input
            if choice not in [str(i) for i in range(1, 9)]:
                raise InvalidMenuInputError(f"'{choice}' is not valid. Select 1-8.")

            if choice == '1':  # Add Book
                bid = input("Enter Book ID: ")
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                books.append(Book(bid, title, author))
                print(f"Success: '{title}' added.")

            elif choice == '2':  # Register Member
                mid = input("Enter Member ID: ")
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                members.append(Member(mid, name, email))
                print(f"Success: Member '{name}' registered.")

            elif choice == '3':  # Borrow Book
                mid = input("Enter Member ID: ")
                # Validation: Member not found
                member = next((m for m in members if m._member_id == mid), None)
                if not member:
                    raise MemberNotFoundError(f"Member ID '{mid}' not found.")

                bid = input("Enter Book ID: ")
                # Validation: Book not found
                book = next((b for b in books if b._book_id == bid), None)
                if not book:
                    raise BookNotFoundError(f"Book ID '{bid}' not found.")

                # Validation: Book unavailable
                if not book._available:
                    raise BookUnavailableError(f"'{book._title}' is already borrowed.")

                # Process Loan
                new_loan = Loan(f"L{len(loans) + 1:03}", book, member)
                loans.append(new_loan)
                book._available = False
                print(f"Success: '{book._title}' lent to {member._name}.")

            elif choice == '4':  # Return Book
                bid = input("Enter Book ID to return: ")
                book = next((b for b in books if b._book_id == bid), None)
                if not book:
                    raise BookNotFoundError("Book ID not found.")

                loan = next((l for l in loans if l._book._book_id == bid and l._is_active), None)
                if not loan:
                    print("This book is not currently on loan.")
                else:
                    loan._is_active = False
                    book._available = True
                    print(f"Success: '{book._title}' returned.")

            elif choice == '5':  # View Books
                print("\n--- Books List ---")
                for b in books:
                    status = "Available" if b._available else "Borrowed"
                    print(f"[{b._book_id}] {b._title} by {b._author} - {status}")

            elif choice == '6':  # View Members
                print("\n--- Members List ---")
                for m in members:
                    print(f"[{m._member_id}] {m._name} ({m._email})")

            elif choice == '7':  # View Loans
                print("\n--- Active Loans ---")
                active = [l for l in loans if l._is_active]
                if not active:
                    print("No active loans.")
                for l in active:
                    print(f"Loan {l._loan_id}: {l._member._name} has {l._book._title}")

            elif choice == '8':  # Exit
                print("Exiting library console...")
                break

        except (LibraryError, InvalidMenuInputError, BookNotFoundError,
                MemberNotFoundError, BookUnavailableError) as e:
            # Displays the error without crashing your continuous loop
            print(f"\nCaught an exception: {e}")


if __name__ == "__main__":
    main()