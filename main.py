
import tracker


def main():
    """Run the Study Session Tracker menu."""
    print("Welcome to Study Session Tracker!")

    while True:
        print("\n1. Add Study Session")
        print("2. View Summary")
        print("3. View All Sessions")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            tracker.add_session()
        elif choice == "2":
            tracker.view_summary()
        elif choice == "3":
            tracker.view_all()
        elif choice == "4":
            print("Goodbye! Keep up the studying.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
