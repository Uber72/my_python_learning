message1="Global Variable"

def myFunction():
    print("\nINSIDE THE FUNCTION")
    #Global variables are accessible inside a function
    print(message1)
    #Declaring a local variable
    message2="Local Variable"
    print(message2)

    myFunction()
    print("\nOUTSIDE THE FUNCTION")
    print(message1)
    print(message2)
    
