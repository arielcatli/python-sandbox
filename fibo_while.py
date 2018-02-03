#Fibonacci in a while loop
fibo = 0
prev_el = 1
next_el = 0

while fibo < 1000:
    fibo = prev_el + next_el
    print(fibo, end=" ")
    prev_el = next_el
    next_el = fibo
