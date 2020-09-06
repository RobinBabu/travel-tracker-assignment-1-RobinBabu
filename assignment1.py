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
    places_file = open('places.csv', 'r')   # Loads file to read file contents.

    get_list_of_lists(place_details, places_file)
    print("Welcome to Travel Tracker 1.0 - by Robin Babu")
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
            while not valid_input:
                try:
                    mark_visited(place_details)
                    valid_input = True
                except ValueError:
                    print("please make sure the entered value is an integer")
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
    # Menu error checking.
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
        print('{}{:1}. {:20} in {:<20} priority {:>5}'.format(visited_status, i, place[0], place[1], place[2]))
    print('{} places. You still want to visit {} places. '.format(len(place_details), len(place_details) -
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
    place_details.append([place_name, place_country, place_priority, 'n'])
    print('{} in {} (priority {}) added to Travel Tracker'.format(place_name, place_country, place_priority))


def mark_visited(place_details):
    """Marks place visited and displays unvisited places in the list via '*' symbol."""
    # iterate through list of places until all places are visited.
    if not[place for place in place_details if place[3] == "n"]:
        print("{} places. No places left to visit. Why not add a new place to visit? ".format(len(place_details)))
        return

    place_visited = check_integer("Enter the number of place to mark as visited: ")
    while place_visited not in range(len(place_details)):
        print("Invalid place number")
        place_visited = check_integer("Enter the number of place to mark as visited: ")
    for i in range(len(place_details)):
        if place_visited == i:
            if place_details[place_visited][3] == "n":
                place_details[place_visited][3] = "v"
                print("{} in {} visited! ".format(place_details[place_visited][0], place_details[place_visited][1]))
            else:
                print("You already visited {}. ".format(place_details[place_visited][0]))


def save_places(place_details):
    """Saves added place into places.csv before closing file."""
    places_file = open('places.csv', 'w')
    for i in place_details:
        places_file.writelines("{},{},{},{}\n".format(i[0], i[1], i[2], i[3]))


if __name__ == '__main__':
    main()
