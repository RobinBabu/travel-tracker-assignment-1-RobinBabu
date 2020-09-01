"""
Replace the contents of this module docstring with your own details
Name: Robin Babu
Date started: 1/09/2020
GitHub URL: https://github.com/RobinBabu
"""

places_details = []
places_file = open('places.csv')


def main():
    print("Welcome Travel Tracker 1.0 - by Robin Babu")

    choice = input("Menu: \n"
                   "L - List places \n"
                   "A - Add new place \n"
                   "M - Mark a place as visited \n"
                   "Q - Quit \n"
                   ">>>").upper()



while choice != "Q":
    if choice == "L":
        places_file = open('places.csv', 'w')




"""
while choice != "Q":
    if choice == "L":
        print()
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        display invalid input error message
    display menu
    get choice
<do final thing, if needed>

"""



if __name__ == '__main__':
    main()
