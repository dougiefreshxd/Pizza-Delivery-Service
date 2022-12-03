class Rules:
    route = []
    already_used = ['Z']
    PizzaChoices = {
        'AllMedium' : {'Medium' : 8},
        'AllLarge' : {'Large' : 6},
        '2M5L' : {'Medium' : 2, 'Large' : 5},
        '3M4L' : {'Medium' : 3, 'Large' : 4},
        '4M3L' : {'Medium' : 4, 'Large' : 3}
    }
    Distances = {
        'A' : {'B' : 9, 'C' : 3, 'D' : 11},
        'B' : {'A' : 9, 'C' : 10, 'D' : 4},
        'C' : {'A' : 3, 'B' : 10, 'D' : 7},
        'D' : {'A' : 11, 'B' : 4, 'C' : 7, 'Z' : 5},
        'Z' : {'D' : 5}
    }

    def fastest_route(self, ending_point, starting_point='Z',distance_traveled=0,fastest_routes=0):
        newdict =  self.Distances
        tempDistance = distance_traveled 
        tempFastRoute = fastest_routes 
        for x in newdict[starting_point].keys(): 
            if x == ending_point: 
                tempDistance = distance_traveled + newdict[starting_point][x] 
                self.already_used.append(x) 
                print(f"Found ending point from strting point {starting_point} and ending at {ending_point} with {tempDistance} miles.")
                print(f"Path taken was {self.already_used}.") 
                if tempFastRoute == 0:
                    print(f"Current Fastest Route is {tempDistance}.")
                    tempFastRoute = tempDistance
                elif tempDistance < tempFastRoute:
                    print(f"Found a faster route, previous fastest was {tempFastRoute}, new fastest is {tempDistance}.")
                    tempFastRoute = tempDistance
                else:
                    pass
                self.already_used.pop()
            else:
                for y in self.already_used: 
                    if y == x:
                        print(f"Found a path we already took, the path is to {x}. Breaking this loop... ")
                        break
                tempDistance = distance_traveled + newdict[starting_point][x] 
                if fastest_routes != 0: 
                    if fastest_routes < tempDistance:
                        print(f"This route is taking too long if we continue to go down path {x} coming from key {starting_point}. Breaking this loop...")
                        self.already_used.pop()
                        tempDistance = tempDistance - newdict[starting_point][x]
                        break 
                #tempDistance = distance_traveled + newdict[starting_point][x] 
                print(f"The current value we are looking at right now is {x} from key {starting_point}.")
                self.already_used.append(x) # Becomes Z,D
                Rules.fastest_route(self,ending_point,x,tempDistance,tempFastRoute) 



def comparing_lists(current_best, contender):
    return 0 

r1 = Rules()

orders = {
    'A' : {'Medium' : 2, 'Large' : 3},
    'B' : {'Medium' : 0, 'Large' : 4},
    'C' : {'Medium' : 2, 'Large' : 3},
    'D' : {'Medium' : 4, 'Large' : 1}
}


r1.fastest_route('B')