#function that returns the sum of the squares of first n natural numbers

def squaresum(n):
    SquareSum = 0
    temp = 1
    if n<= 0:
        print("Please enter a natural number!")
    else:
        while temp <= n:
            SquareSum += temp*temp
            temp +=1
            
        print("The sum of the square of first ", n, "number(s) is/are: ", SquareSum)
