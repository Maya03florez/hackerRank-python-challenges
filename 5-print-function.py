if __name__ == '__main__':
    n = int(input())
    
    if n >= 1 and n <= 150:
        for i in range(1,n+1):
            print(i,end="")

# the code prompts the user to enter a number, checks if the number is within the 
# range of 1 to 150, and if it is, it prints the numbers from 1 to the input value 
# (inclusive) without any separation. If the input is invalid, it doesn't execute 
# the loop and exits the program.