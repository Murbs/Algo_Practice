# FizzBuzz

There comes a time in every persons life where they need to either fizz or buzz.

```Python
def FizzBuzz(x): # It begins..
```

Rather than copy/paste the first google result I could find, I opted to try something a bit different. Instead of replacing multiples of '3' with fizz or '5' with buzz, I've created an array for each outcome.

```Python
fizzCount = [] # All your 'Fizz' go here
buzzCount = [] # All your 'buzz' go here
fizzbuzzCount = [] # And all your 'FizzBuzz' go here
```

When the program loops through a given range, it appends the result to an array if the requirements are met. However, the python range function starts at 0 and adds a false-positive to our first loop result. We can account for this by instructing the loop to continue, essentially ignoring the first result. You could also do something fancier to check for 'FizzBuzz' using the AND operator if you're a stickler but this is my FizzBuzz.

```Python
# Loops through range of numbers, given at runtime
for i in range(x):
    
    # Ignore 0 as a result
    if i == 0:
      continue
    
    # If number is divisble by 15, FizzBuzz value appends to its array
    elif i % 15 == 0:
      fizzbuzzCount.append(i)
    
    # If number is divisble by 5, Buzz value appends to its array
    elif i % 5 == 0:
      buzzCount.append(i)
    
    # If number is divisble by 3, Fizz value appends to its array
    elif i % 3 == 0:
      fizzCount.append(i)
```

Lastly, I wanted to know exactly how many 'Fizz', 'Buzz', and 'FizzBuzz' were pushed to these arrays. Insert a bunch of print() functions to make it look nice and display which numbers are in which array.

```Python
print("\nIn the given range of 0-" + str(x-1) +", there are:\n")
    
print(str(len(fizzCount)) + " counts of Fizz!")
print(fizzCount)
    
print("\n" + str(len(buzzCount)) + " counts of Buzz!")
print(buzzCount)
    
print("\nand " + str(len(fizzbuzzCount)) + " counts of FizzBuzz!")
print(fizzbuzzCount)
```

Second lastly... I figured I might as well make this a bit more interactive. The 'inputFizzBuzz' function takes a user input and attempts to 'FizzBuzz-ify' it. If the input cannot be cast to an integer, a ValueError exception is thrown and some boilerplate text is returned. You could also add a break in either the try or except clauses if you wanted the program to terminate afterwards but I chose not to.

```Python
def inputFizzBuzz():
    
    while True:
        
        # Attempts to run on user input
        try:
            x = int(input("Input a number to 'FizzBuzz-ify':")) + 1
            FizzBuzz(x)
        
        # Boilerplate text if user input is not an integer
        except ValueError:
            print("You can't 'FizzBuzz-ify' that, try again.")
```

![FizzBuzz](https://cdn.discordapp.com/attachments/826109384093859879/828723670893068358/FzBz.PNG)
