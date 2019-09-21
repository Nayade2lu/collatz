#Lucia Saura collatz

# variable number user has to insert
n = int(input('Enter a positive number:'))

#logic collatz 2 
#loop for iterating when the number is bigger than 1
while n != 1:
    # print the number to show the original number
    print(n)
    # the following line identifies an even number. % gets the rest of a division, if divided by 2 the rest is 0 then is even
    if n % 2 == 0:
        #if the number is even, the number is divided by 2
        n = n//2
    #if the number is something that is not even then
    else:
        # the number is multiplied • 3 and added 1
        n = (n*3) + 1

#printing the final result
print (n)
