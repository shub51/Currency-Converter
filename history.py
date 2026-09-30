#
def show_history():
    try:
        with open("history.txt", "r") as file:
            history = file.readlines()

        if not history:
            print("\nNo conversion history yet.")
            return

        print("\nConversion History:")
        for item in history:
            print("-", item.strip())

    except FileNotFoundError:
        print("\nNo conversion history yet.")