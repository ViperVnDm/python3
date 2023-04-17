# while expression 
# expression passed to boolean

#Count down 5 to 1 
c = 5
while c != 0:
    print(c)
    c -= 1

#Explicit better than implicit

#Stuck in a loop
# while True:
#     pass

#break in python jumps out of the inner-most executing loop to the line immediately after it
#Below hangs at a prompt until the input is divisible by 7
while True:
    response = input()
    if int(response) % 7 == 0:
        break
