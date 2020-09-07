## this part takes in the numbers given from the user. spits an error out if not given an integer.
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


#the program reminds you what integers you entered
print ("You gave the numbers: ")

print(num_list)
    
    
#finds the minimum number
minimum = num_list[0]
print(minimum)
for y in range(1, 10):
    if num_list[y] < minimum:
        minimum = num_list[y]
      
print("The minimum is ")
print (minimum)
    
#finds the maximum number
maximum = num_list[0]

for count2 in range(1,10):
    if num_list[count2] > maximum:
        maximum = num_list[count2]
    count2 = count2 + 1  

print ("The maximum is ")
print (maximum)

#calculates the range
range1 = maximum - minimum

print ("The range is ")
print (range1)

#calculates the mean
sum = 0

for count3 in range(0,10):
    sum = sum + num_list[count3]
    count3 = count3 + 1

mean = sum / 10
    
print ("The mean is ")
print (mean)

#calculates the variance
sum1 = 0

for count4 in range(0,10):
    var = (num_list[count4]-mean)**2
    sum1 = sum1 + var
    count4 = count4 + 1
    
variance = sum1 / 9

print ("The variance is ") 
print (variance)

#calculates the standard deviation
sum2 = 0

for count5 in range(0,10):
    var1 = (num_list[count5]-mean)**2
    sum2 = sum2 + var1
    count5 = count5 + 1
    
stan_dev = (sum2 / 10)**(1/2)

print ("The standard deviation is ")
print (stan_dev)

print ("All done! :)")
