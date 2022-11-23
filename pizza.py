#This is our class where we will set Rules that will stay the same throughought any run of our algorithm. i.e. things such as the map and the
#relations between two points on this map 
class Rules:
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
    def fastest_route(self, ending_point, starting_point='Z'):
        newdict =  self.Distances
        distance_traveled = 0
        #This is where the route and distance will be calculated
        start = newdict[starting_point]
        for x in start.keys():
            distance_traveled += start[x]
#What this function will do is help calculate the fastest route. When running our fastest route module within our earlier mentioned class, we will be saving the results of the 
#first fastest route in an array, with the total distance being the first variable, then after that the list will have a trail of the starting point to the ending point
#Then we will pass this array as a default variable within our comparing lists function below. And whenever we find another trail while going through all paths, we will compare
#each array with the variables to the current_best route, and will only replace the default variable for the array if we find a faster quicker route
def comparing_lists(current_best, contender):
    return 0 
#This is a temporary dictionary we will use to practice sending information into our algorithm and functions later to test capability and
#debugging
r1 = Rules()

orders = {
    'A' : {'Medium' : 2, 'Large' : 3},
    'B' : {'Medium' : 0, 'Large' : 4},
    'C' : {'Medium' : 2, 'Large' : 3},
    'D' : {'Medium' : 4, 'Large' : 1}
}

orderlist = []
r1.fastest_route(orderlist, 'A')
