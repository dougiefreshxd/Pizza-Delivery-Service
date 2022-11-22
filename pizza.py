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

#This is a temporary dictionary we will use to practice sending information into our algorithm and functions later to test capability and
#debugging
'''
orders = {
    
}
'''

