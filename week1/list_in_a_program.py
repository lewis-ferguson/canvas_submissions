

numbers = range(1,11)

#creating a function to display a list of even numbers only

def even_only(numbers):
    even_numbers = [] #creating an empty list to store the even numbers
    [even_numbers.append(number) for number in numbers if number % 2 ==0]
    #for every number than is divisible by 2, add it to the even_numbers list
    return even_numbers

print(even_only(numbers))

#lists can be used to store multiple values that can be added to, removed from and ordered in different ways.


