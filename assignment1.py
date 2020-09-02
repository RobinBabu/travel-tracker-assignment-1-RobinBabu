"""
Replace the contents of this module docstring with your own details
Name: Robin Babu
Date started: 1/09/2020
GitHub URL: https://github.com/RobinBabu
"""
import csv
from operator import itemgetter


def main():
    print("Welcome Travel Tracker 1.0 - by Robin Babu")
    list_of_places = load_original_file()
    choice = input("Menu: \n"
                   "L - List places \n"
                   "A - Add new place \n"
                   "M - Mark a place as visited \n"
                   "Q - Quit \n"
                   ">>>").upper()

    while choice != "Q":
        if choice == "L":
            print_list_places(list_of_places)
        elif choice == "A":
            add_new_place(list_of_places)
        elif choice == "M":
            mark_visited(list_of_places)
        elif choice == "":
            print("Input cannot be blank")
        else:
            print("Invalid menu choice")

        choice = input("Menu: \nL - List places \nA - Add new place \nM - Mark a place as visited \nQ - Quit "
                       "\n>>> ").upper()

    with open('places.csv', 'w', newline='') as resultFile:
        writer = csv.writer(resultFile)
        writer.writerows(list_of_places)
    print('{} places saved to places.csv\nHave a nice day :) '.format(len(list_of_places)))


# Function Used to Open Initial Places File.
def load_original_file():
    file_places = open("places.csv", "r")
    reader = csv.reader(file_places, delimiter=',')
    places = list(reader)
    print('{} places loaded from places.csv'.format(len(places)))
    # String to integer conversion
    for place in places:
        place[1] = int(place[1])
    file_places.close()
    places.sort(key=itemgetter(1, 0))
    return places


if __name__ == '__main__':
    main()
