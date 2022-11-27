#This is our class where we will set Rules that will stay the same throughought any run of our algorithm. i.e. things such as the map and the
#relations between two points on this map 
class Rules:
    route = []
    already_used = ['Z']
    #This is a dictionary storing all choices our delivery boy will have for loading pizzas in the car
    PizzaChoices = {
        'AllMedium' : {'Medium' : 8},
        'AllLarge' : {'Large' : 6},
        '2M5L' : {'Medium' : 2, 'Large' : 5},
        '3M4L' : {'Medium' : 3, 'Large' : 4},
        '4M3L' : {'Medium' : 4, 'Large' : 3}
    }
    #Reference image for connections should be included in the png in the folder holding this code
    #This is basically a python dictionary of a matric of the map we are working and the connections between the houses. We have the value for 
    #each key for a certain reason. We will make our trail for the fastest route by traversing each dictionary. For example since we start at 
    #pizza shop Z, we will go to key Z in the distance dictionary, go through the value dictionary and see that our only path we can take is to
    #house D with 5 miles to take into consideration for travel distance. We will then mark this distance, then use key D in our distance 
    #dictionary and see the dictionary value it holds and from there see what options we have to traverse too, and we will follow this 
    #recursive pattern until we reach the designated house we want to reach. This idea will be further developed throughout the coding process
    Distances = {
        'A' : {'B' : 9, 'C' : 3, 'D' : 11},
        'B' : {'A' : 9, 'C' : 10, 'D' : 4},
        'C' : {'A' : 3, 'B' : 10, 'D' : 7},
        'D' : {'A' : 11, 'B' : 4, 'C' : 7, 'Z' : 5},
        'Z' : {'D' : 5}
    }
    #The point of this module is to take in 2 parameters, the starting point and ending point with the starting point being set to a default variable Z, which will represent
    #our pizza shop that we will always start from. After that we declare a new dictionary to our Distances dictionary list, as we might want to edit this without editing
    #the global dictionary. From here we are going to start a chain path, where we follow up the dictionary. Starting at Z we see what paths that has, which only is D with 5 miles
    #From here, we note that number then look at the D key within our dictionary. Here we will see a new nested dictionary with multiple keys of houses we have routes too, and their 
    #travel distance. We will later follow all these possible routes up to our ending point, and keep replacing the array/list with the fasted most updated route. Code still
    #in progress
    def fastest_route(self, ending_point, starting_point='Z',distance_traveled=0,fastest_routes=0):
        newdict =  self.Distances
        #This is where the route and distance will be calculated
        tempDistance = distance_traveled # 0 , 5
        tempFastRoute = fastest_routes # 0, 0
        for x in newdict[starting_point].keys(): # D : 5, ' A B C D'
            if x == ending_point: # skip, x = A so follow, 
                tempDistance = distance_traveled + newdict[starting_point][x] # is now 16
                self.already_used.append('->' + x) # Becomes Z,D,A
                print(f"Found ending point from strting point {starting_point} and ending at {ending_point} with {tempDistance} miles.")
                print(f"Path taken was {self.already_used}.") # Print Z D A
                tempFastRoute = distance_traveled # Becomes 16
                self.already_used.pop()
            else:
                for y in self.already_used: #Empty, so skip
                    if y == x:
                        print(f"Found a path we already took, the path is to {x}. Breaking this loop... ")
                        break
                if fastest_routes != 0: #FT = 0, skip
                    if fastest_routes > newdict[starting_point][x]:
                        print(f"This route is taking too long if we continue to go down path {x}. Breaking this loop...")
                        break 
                tempDistance = distance_traveled + newdict[starting_point][x] # tempDistance becomes 5
                print(f"The current key we are looking at right now is {x}")
                self.already_used.append('->' + x) # Becomes Z,D
                Rules.fastest_route(self,ending_point,x,tempDistance,tempFastRoute) # (self, 'A','D', 5, 0)



                
def comparing_lists(current_best, contender):
    return 0 
#This is a temporary dictionary we will use to practice sending information into our algorithm and functions later to test capability and
#debugging``
r1 = Rules()

orders = {
    'A' : {'Medium' : 2, 'Large' : 3},
    'B' : {'Medium' : 0, 'Large' : 4},
    'C' : {'Medium' : 2, 'Large' : 3},
    'D' : {'Medium' : 4, 'Large' : 1}
}


r1.fastest_route('A')
