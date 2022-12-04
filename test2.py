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
        'A' : {'B' : 2, 'D' : 6, 'E' : 3},
        'B' : {'A' : 2, 'C' : 2, 'D' : 3, 'E' : 5},
        'C' : {'B' : 2, 'D' : 2, 'Z' : 7},
        'D' : {'A' : 6, 'B' : 3, 'C' : 2,'E' : 1, 'Z' : 2},
        'E' : {'A' : 3, 'D' : 1, 'Z' : 2},
        'Z' : {'C' : 7, 'D' : 2, 'E' : 2}
    }

    def fastest_route(self, ending_point, starting_point='Z',distance_traveled=0,fastest_routes=0):
        newdict =  self.Distances
        tempDistance = distance_traveled
        tempFastRoute = fastest_routes
        continue_stmnt = False
        for x in newdict[starting_point].keys(): 
            if x == ending_point:
                #print(f"The current value we are looking at right now is {x} from key {starting_point} in the if x == ending_point stmnt.") 
                tempDistance = distance_traveled + newdict[starting_point][x] 
                self.already_used.append(x) 
                print(f"Found ending point from strting point Z and ending at {ending_point} with {tempDistance} miles.")
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
                #print(f"The current value we are looking at right now is {x} from key {starting_point} in the else stmnt.")
                if len(self.already_used) > 2:
                        if x == self.already_used[-2]:
                            #print(f"already used list is {self.already_used} ")
                            #print(f"Bout to continue due to not repathing...")
                            tempDict = newdict[starting_point]
                            tempList = list(tempDict.keys())
                            if x == tempList[-1]:
                                #print(f"The value x which is {x} is equal to the previous key {starting_point}'s dictionaries last key which is {tempList}.")
                                self.already_used.pop()
                            continue
                         
                for y in self.already_used:
                    #print(f"Currently tweaking already used list which is {self.already_used} in the loop at value {y}")
                    #print(f"The key in the address dictionary that we are jumping from is {self.already_used[-1]} I believe. This is our test.") 
                    tempDict = newdict[starting_point]
                    if y == x:
                        #print(f"Found a path we already took, the path is to {x}. Breaking this loop... ")
                        tempDict = newdict[starting_point]
                        tempList = list(tempDict.keys())
                        #print(f"Our tempDict is {tempDict}")
                        #print(f"Our tempList is {tempList}")
                        #print(f"This is a test, current value printing is {tempList[-1]}")
                        if len(self.already_used) < 3:    
                            if y == tempList[-1]:
                                #print(f"Just hit the end of a dictionary of values to key {starting_point} with the last value being {y}, time to pop and go back up to the previous key.")
                                self.already_used.pop()
                                continue_stmnt = True
                                break

                        continue_stmnt = True
                if continue_stmnt == True:
                    continue
                tempDistance = distance_traveled + newdict[starting_point][x] 
                if fastest_routes != 0: 
                    if fastest_routes < tempDistance:
                        #print(f"This route is taking too long if we continue to go down path {x} coming from key {starting_point}. Breaking this loop...")
                        self.already_used.pop()
                        tempDistance = tempDistance - newdict[starting_point][x]
                        break 
                #tempDistance = distance_traveled + newdict[starting_point][x] 
                #print(f"The current value we are looking at right now is {x} from key {starting_point}
                self.already_used.append(x) # Becomes Z,D
                Rules.fastest_route(self,ending_point,x,tempDistance,tempFastRoute)
                if len(self.already_used) > 2:
                    self.already_used.pop() 



def comparing_lists(current_best, contender):
    return 0 

r1 = Rules()

orders = {
    'A' : {'Medium' : 2, 'Large' : 3},
    'B' : {'Medium' : 0, 'Large' : 4},
    'C' : {'Medium' : 2, 'Large' : 3},
    'D' : {'Medium' : 4, 'Large' : 1}
}


r1.fastest_route('E')