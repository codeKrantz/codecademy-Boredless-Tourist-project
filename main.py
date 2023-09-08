#list of atractions
attractions = [[], [], [], [], []]

#printing list
print(attractions)


# list of destinations
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

#test traveler info
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# destination index function 1
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

#traveler location function 2
def get_traveler_location(traveler):
  traveler_destination  = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

#Add atraction funttion 3
def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions_for_destination = attractions[destination_index].append(attraction)

# find attraction function 4
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []

  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]

    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  
  return attractions_with_interest
    
#getting attractions for travelers function 5
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  #finding atrations
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi "+traveler[0]+"we think you'll like these places around " + traveler_destination + ": "

#this loop provides logic for the gramtical usuage of the items. the range allows you to find the final value and use an "and" and a period
  for i in range(len(traveler_attractions)):
    if traveler_attractions[-1] == traveler_attractions[i]:
      interests_string += "and the "+ traveler_attractions[i] + "."
    else:
      interests_string += "the " + traveler_attractions[i] + ", "
    
  return interests_string




  



#the aplication of the code 


#testing function 1
print(get_destination_index("Paris, France"))

#testing function 2
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

#testing function 3
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
print(attractions)

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# prints all atrations print(attractions)

#testing function 4
la_arts = find_attractions("Los Angeles, USA", ['art'])
print(la_arts)


#testing function 5
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)


