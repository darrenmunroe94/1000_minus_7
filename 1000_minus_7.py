

def main():

    x = 1000

    while(x > 0):

        print ("whats %d - 7? ") % int(x)
        userInput = input("")

        x -= 7

        if(userInput == x):
            
            pass
        
        else:

            print("Incorrect: %d.\n") % int(x)

if __name__ == "__main__":
    main()
