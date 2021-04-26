def FizzBuzz(x):
    
    fizzCount = []
    buzzCount = []
    fizzbuzzCount = []
    
    for i in range(x):
        
        if i == 0:
            continue
        
        elif i % 15 == 0:
            fizzbuzzCount.append(i)
            
        elif i % 5 == 0:
            buzzCount.append(i)
            
        elif i % 3 == 0:
            fizzCount.append(i)
    
    print("\nIn the given range of 0-" + str(x-1) +", there are:\n")
    
    print(str(len(fizzCount)) + " counts of Fizz!")
    print(fizzCount)
    
    print("\n" + str(len(buzzCount)) + " counts of Buzz!")
    print(buzzCount)
    
    print("\nand " + str(len(fizzbuzzCount)) + " counts of FizzBuzz!")
    print(fizzbuzzCount)


def inputFizzBuzz():
    
    while True:
        
        try:
            x = int(input("Input a number to 'FizzBuzz-ify':")) + 1
            FizzBuzz(x)
            
        except ValueError:
            print("You can't 'FizzBuzz-ify' that, try again.")
            
        
inputFizzBuzz()





    


