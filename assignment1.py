"""
Replace the contents of this module docstring with your own details
Name: Robin Babu
Date started: 1/09/2020
GitHub URL: https://github.com/RobinBabu
"""
from operator import itemgetter


def main():
    """Travel Tracker program allows a user to track places they wish to visit and places they have already visited"""
    valid_input = False
    place_details = []
    places_file = open('places.csv', 'r')   # Loads file

    get_list_of_lists(place_details, places_file)
    print("Welcome Travel Tracker 1.0 - by Robin Babu")
    print("{} places loaded from places.csv".format(len(place_details)))

    choice = get_choice()

    while choice != "Q":
        if choice == "L":
            print_list(place_details)
        elif choice == "A":
            open('places.csv', 'w')
            while not valid_input:
                try:
                    add_new_place(place_details)
                    valid_input = True
                except ValueError:
                    print("Invalid input,")

        elif choice == "M":
            print('Mark place as visited test ')
            return

        print("")
        choice = get_choice()
        valid_input = False
        print("")
    save_places(place_details)
    print("{} places saved to places.csv \nHave a nice day! :)".format(len(place_details)))
    places_file.close()


def get_list_of_lists(place_details, places_file):
    """Stores place data in list of lists and returns list when called."""
    for place in places_file:
        place = place.strip().split(',')
        place_details.append([place[0], (place[1]), place[2], place[3]])
    place_details.sort(key=itemgetter(1))


def get_choice():
    """Grabs user input from menu and navigate to selected input."""
    choice = input("Menu: \n"
                   "L - List places \n"
                   "A - Add new place \n"
                   "M - Mark a place as visited \n"
                   "Q - Quit \n"
                   ">>>").upper()

    while choice not in ("L", "A", "M", "Q"):
        print("Invalid menu choice, please enter a valid menu option.")
        choice = input("Menu: \n"
                       " L - List place \n"
                       " A - Add a new place \n"
                       " M - Mark a place as visited \n"
                       " Q - Quit \n"
                       ">>>").upper()
    return choice


def print_list(place_details):
    """Prints list contents from places.csv displaying visited or unvisited status."""
    unvisited_count = 0
    place_details.sort(key=itemgetter(1, 0))
    for i, place in enumerate(place_details):
        if place[3] == 'v':
            unvisited_count += 1
            visited_status = ' '
        else:
            visited_status = '*'
        print('{}{:2}. {:20} in {:<20} priority {:>5}'.format(visited_status, i, place[0], place[1], place[2]))
    print('{} places. You still want to visit {} places. '.format(unvisited_count, len(place_details) -
                                                                  unvisited_count))


def check_string(prompt):
    """Function to error check if string is being entered by user."""
    string_check = input(prompt)
    while string_check == '':
        print('Input cannot be blank')
        string_check = input(prompt)
    return string_check


def check_integer(prompt):
    """Function to error check if integer value is being entered by user."""
    valid_input = False
    while not valid_input:
        try:
            value = int(input(prompt))
            if int(value) >= 0:
                valid_input = True
                return value
            else:
                print('Number must be > 0')
        except ValueError:
            print('Invalid input, please enter a valid number')


def add_new_place(place_details):
    """Add new place to places.csv"""
    place_name = check_string('Name: ')
    place_country = check_string('Country: ')
    place_priority = check_integer('Priority: ')
    place_details.append([place_name, place_country, place_priority, 'u'])
    print('{} in {} (priority {}) added to Travel Tracker'.format(place_name, place_country, place_priority))


def save_places(place_details):
    """Saves added place into places.csv before closing file."""
    places_file = open('places.csv', 'w')
    for i in place_details:
        places_file.writelines("{},{},{},{}\n".format(i[0], i[1], i[2], i[3]))


if __name__ == '__main__':
    main()
