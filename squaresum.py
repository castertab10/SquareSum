#function that returns the sum of the squares of first n natural numbers

n = int(input("input a number (note: number must be a natural number): "))
squaresum = 0
temp = 1
temp1 = 1
while temp <= n:
    squaresum += temp*temp
    temp +=1

print("The sum of the square of first ", n, "number(s) is/are: ", squaresum)