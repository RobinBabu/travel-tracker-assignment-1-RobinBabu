"""
Replace the contents of this module docstring with your own details
Name: Robin Babu
Date started: 1/09/2020
GitHub URL: https://github.com/RobinBabu
"""

places_file = open('places.csv', 'r')
valid_input = False
place_details = []


def main():
    """Travel Tracker program allows a user to track places they wish to visit and places they have already visited"""
    print("Welcome Travel Tracker 1.0 - by Robin Babu")
    choice = get_choice()

    while choice != "Q":
        if choice == "L":
            print('List test')
            return
        elif choice == "A":
            open('places.csv', 'w')
            print('Add new place test')
            return

        elif choice == "M":
            print('Mark place as visited test ')
            return
        print("")
        choice = get_choice()

    print("{} places saved to places.csv \nHave a nice day! :)".format(len(place_details)))


def get_choice():
    """Grabs user input from menu and navigate to selected input."""
    choice = input("Menu: \n"
                   "L - List places \n"
                   "A - Add new place \n"
                   "M - Mark a place as visited \n"
                   "Q - Quit \n"
                   ">>>").upper()
    while choice not in ("L", "A", "M", "Q"):
        print("Invalid menu choice")
        choice = input("Menu: \n"
                       " L - List place \n"
                       " A - Add a new place \n"
                       " M - Mark place as visited \n"
                       " Q - Quit \n"
                       ">>>").upper()
    return choice


if __name__ == '__main__':
    main()
