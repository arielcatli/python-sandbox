#Demo of FOR loops using Fibonacci

fibo = 0
next_elem = 0
prev_elem = 1

print("Fibonacci sequence with 20 elements:")

#Gives 20 items in the sequence
for x in range(1, 20, 1):
    fibo = next_elem + prev_elem
    print(fibo, end=" ")
    prev_elem = next_elem
    next_elem = fibo
    
