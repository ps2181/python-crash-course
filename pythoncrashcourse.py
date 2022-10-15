
#week 1 problem1
#Question 1
#In this scenario, two friends are eating dinner at a restaurant. The bill comes in the amount of 47.28 dollars.
#The friends decide to split the bill evenly between them, after adding 15% tip for the service.
#Calculate the tip, the total amount to pay, and each friend's share, then output a message saying
#"Each person needs to pay: " followed by the resulting number.

bill = 47.28
tip = bill *0.15
total = bill + tip
share = total/2 
print("Each person needs to pay:" + str(share))



#week 2 problem 1(function)
# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
    
    km = miles * 1.6
    return km  # approximately 1.6 km in 1 mile

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(55)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(2 *my_trip_km))


#week 3 problem 3 (recursion)
#Question 3
#Fill in the blanks to make the is_power_of function return whether the number is a power of the given base
#Note: base is assumed to be a positive number
def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number==1

  # Recursive case: keep dividing number by base.
  return is_power_of(number//base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False


#week4 problem 1(final assessment)
def format_address(address_string):
  # Declare variables
  hnum=0
  sname = []

  # Separate the address string into parts
  address = address_string.split()

  # Traverse through the address parts
  for item in address:
    if item.isnumeric():
      hnum = item
    else:
      sname.append(item)

 

    # Determine if the address part is the
    # house number or part of the street name

  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(hnum, " ".join(sname))

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"







