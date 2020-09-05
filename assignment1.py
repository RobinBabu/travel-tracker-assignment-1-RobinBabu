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
    places_file = open('places.csv', 'r')

    get_list_of_lists(place_details, places_file)
    print("Welcome Travel Tracker 1.0 - by Robin Babu")
    print("{} places loaded from places.csv".format(len(place_details)))

    choice = get_choice()

    while choice != "Q":
        if choice == "L":
            print_list(place_details)
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
    places_file.close()


# sorts the places.csv file into a list of lists, returns the list of lists
def get_list_of_lists(place_details, places_file):
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
        print("Invalid menu choice")
        choice = input("Menu: \n"
                       " L - List place \n"
                       " A - Add a new place \n"
                       " M - Mark place as visited \n"
                       " Q - Quit \n"
                       ">>>").upper()
    return choice


#  (choice == L) prints the list of lists contents,
def print_list(place_details):
    unvisited_count = 0
    place_details.sort(key=itemgetter(1, 0))
    for i, place in enumerate(place_details):
        if place[3] == 'v':
            unvisited_count += 1
            visited_status = ' '
        else:
            visited_status = '*'
        print('{}{:2}. {:20} in {:<20} priority {:>5}'.format(visited_status, i, place[0], place[1], place[2]))
    print('{} places. You still want to visit {} places. '.format(unvisited_count, len(place_details) - unvisited_count))


if __name__ == '__main__':
    main()
