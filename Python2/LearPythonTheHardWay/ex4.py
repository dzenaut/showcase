#assigns the number of cars
cars = 100
#assigns space in a car
space_in_a_car = 4.0
#assigns number of drivers
drivers = 30
#assigns number of passengers
passengers = 90
#calculates number of cars that aren't driven by subtracting the number of drivers from the number of cars
cars_not_driven = cars-drivers
#sets number of cars driven equal to number of drivers
cars_driven = drivers
#calculates carpool capacity as a product of number of cars driven and space in a car
carpool_capacity = cars_driven*space_in_a_car
#calculates average number of passengers per car by dividing the number od passengers by the number of cars driven
average_passengers_per_car = passengers/cars_driven
x = 1.5


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
print 6 * x