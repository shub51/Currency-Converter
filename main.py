      # Currency Converter
#importing the modules
from converter import convert_currency
from currencies import currencies
from history import show_history
# function to display available currencies
def show_currencies():
    print("\nAvailable currencies:")
    for code, name in currencies.items():
        print(code, "-", name)
# function to run the main program
def main():
    print("================================")
    print("      CURRENCY CONVERTER")
    print("================================")

    while True:
        print("\n1. Convert Currency")
        print("2. Show Currencies")
        print("3. Show History")
        print("4. Exit")
# taking user input for the choice of operation
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                from_currency = input("From currency (INR/USD/EUR/GBP): ").upper()
                to_currency = input("To currency (INR/USD/EUR/GBP): ").upper()

                result = convert_currency(amount, from_currency, to_currency)

                print(f"\n{amount:.2f} {from_currency} = {result:.2f} {to_currency}")

            except ValueError as error:
                print("Error:", error)

        elif choice == "2":
            show_currencies()

        elif choice == "3":
            show_history()

        elif choice == "4":
            print("Thank you for using Currency Converter!")
            break

        else:
            print("Please enter a valid choice.")

# run the main function when the script is executed
if __name__ == "__main__":
    main()
