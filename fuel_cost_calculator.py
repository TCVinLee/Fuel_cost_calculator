#1 imperial gallon = 4.54609188 litres
#per litre: 46/ 4.54609188 = 10.1185812 miles
#1 mile = 0.0988376 litre

#Set up function to check if input is float
def check_input(prompt):
  while True:
    user_input = input(prompt)
    try:
      user_input = float(user_input)
      return user_input
    except ValueError:
      print(f"It requires a number and you have entered '{user_input}'. Please enter a valid number. For example 46 or 37.85 \n\n")
    

#Print out title
print("***** Fuel Cost Calculator *****")
print("********** MPG to KMpL convertor")
print("v2.0")
print("\n\n")

#Instruction for using calculator or convertor functionality
print("* If you only want to convert MPG to Km/L, please enter 0 for the following question *\n")
#Enter MPG information
#mpg = input("Enter the number for MPG: ")
mpg = check_input("Enter the number for MPG: ")
#Enter fuel cost (in pence)
cost = check_input("Enter the cost of fuel (in pence): ")
#Enter distance in miles
distance = check_input("Enter the distance in miles :")

#Convert input to float
#mpg = float(mpg)

#Break down for miles per litre
miles_per_litre = mpg / 4.54609188
#Calculate how many KM per litre
per_litre_for_km = "{:.2f}".format(miles_per_litre * 1.60934)
#Calculate distance in km
distance_in_km = "{:.2f}".format(distance * 1.60934)
#Calculate how much litre needed for 1 mile
litres_per_mile = 1 / miles_per_litre
#Calculate how much litres needed for the distance
litres_needed = litres_per_mile * distance
#Calculate cost for the distance
cost_needed = litres_needed * cost
#cost in GBP, round to 2 decimal points
cost_in_GBP = "{:.2f}".format(cost_needed / 100)

print(f"\n\n*****Cost for the trip*****\n\nCost: £{cost_in_GBP}\n\nDistance: {distance} miles | {distance_in_km} km.\n")
print(f"* Fuel efficiency * \nMPG: {mpg} = km/l: {per_litre_for_km}.")