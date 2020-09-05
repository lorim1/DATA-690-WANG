# Prompts a user to enter 10 integers. 

# If the user enters anything other than integers, remind her that only integers are allowed and let her retry. *Don't allow the user to enter more than 10 or less than 10 integers. Display the 10 integers back to the user at the end. Calculate the following statistics from the 10 integers entered:

# Minimum
# Maximum
# Range
# Mean
# Variance
# Standard Deviation

#this part takes in the numbers given from the user. spits an error out if not given an integer.
count = 0
num_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while count < 10:

    print("Please enter an integer: ")
    input0 = input()

    try:
        val0 = int(input0)
        num_list[count] = val0
        count = count + 1
        
    except ValueError:
        print("That is not an integer. Please try again. ")

#this is where the list assigns individual values - to make it easier to read later
num0 = num_list[0]
num1 = num_list[1]
num2 = num_list[2]
num3 = num_list[3]
num4 = num_list[4]
num5 = num_list[5]
num6 = num_list[6]
num7 = num_list[7]
num8 = num_list[8]
num9 = num_list[9]

#the program reminds you what integers you entered
print ("You gave the numbers: ")
print (num0)
print (num1)
print (num2)
print (num3)
print (num4)
print (num5)
print (num6)
print (num7)
print (num8)
print (num9)

#finds the minimum number
minimum = num0

if num1 < minimum:
    minimum = num1
    
if num2 < minimum:
    minimum = num2
        
if num3 < minimum:
    minimum = num3
    
if num4 < minimum:
    minimum = num4
    
if num5 < minimum:
    minimum = num5
    
if num6 < minimum:
    minimum = num6

if num7 < minimum:
    minimum = num7
    
if num8 < minimum:
     minimum = num8
    
if num9 < minimum:
    minimum = num9
    
print ("The minimum is ")
print (minimum)
    
#finds the maximum number
maximum = num_list[0]

if num1 > maximum:
    maximum = num1
    
if num2 > maximum:
    maximum = num2
    
if num3 > maximum:
    maximum = num3

if num4 > maximum:
    maximum = num4

if num5 > maximum:
    maximum = num5
    
if num6 > maximum:
    maximum = num6
    
if num7 > maximum:
    maximum = num7

if num8 > maximum:
    maximum = num8
    
if num9 > maximum:
    maximum = num9   

print ("The maximum is ")
print (maximum)

#calculates the range
range = maximum - minimum

print ("The range is ")
print (range)

#calculates the mean
mean = (num0 + num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9) / 10
    
print ("The mean is ")
print (mean)

#calculates the variance
variance = ( ((num0-mean)**2) + ((num1-mean)**2) + ((num2-mean)**2) + ((num3-mean)**2) + ((num4-mean)**2) + ((num5-mean)**2) + ((num6-mean)**2) + ((num7-mean)**2) + ((num8-mean)**2) + ((num9-mean)**2)) / 9

print ("The variance is ") 
print (variance)

#calculates the standard deviation

stan_dev = ((((num0-mean)**2) + ((num1-mean)**2) + ((num2-mean)**2) + ((num3-mean)**2) + ((num4-mean)**2) + ((num5-mean)**2) + ((num6-mean)**2) + ((num7-mean)**2) + ((num8-mean)**2) + ((num9-mean)**2)) / 10)**(1/2)

print ("The standard deviation is ")
print (stan_dev)

print ("All done! :)")
