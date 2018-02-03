#Write a Python program to remove duplicates from a list.

import random
import bubble_sort

def main():
    #Generate random listing
    listing = []
    for number in range(0,100):
        listing.append(random.randint(1,50))

    print(listing)
    remove_duplicate(listing)
    bubble_sort.sort(listing)

def remove_duplicate(listing):
    for item in listing:
        for x in range(listing.index(item)+1, len(listing)):
            if x < len(listing) and item == listing[x]:
                listing.remove(listing[x])
        for x in range(0, listing.index(item)):
            if item == listing[x]:
                listing.remove(listing[x])

if __name__ == "__main__":
    main()
