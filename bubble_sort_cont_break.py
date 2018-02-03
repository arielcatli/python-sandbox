#Bubble sorting demo for the break and continue statements
#bubble sorting
def sort(numbers):
    sorting_done = False
    while not sorting_done:
        sorting_done = True
        iterations += 1
        for x in range(0,len(numbers)-1):
            if numbers[x] > numbers[x+1]:
                holder = numbers[x]
                numbers[x] = numbers[x+1]
                numbers[x+1] = holder
                sorting_done = False
            else:
                continue
    print("The numbers sorted: ", numbers)
    print("Iterations: ", iterations," Elements: ", len(numbers))
