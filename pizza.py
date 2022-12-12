class Rules:
    def __init__(self):
        self.route = []
        self.already_used = ['Z']

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
        self.fastest_route = fastest_routes
        continue_stmnt = False
        for x in newdict[starting_point].keys(): 
            if x == ending_point:
                tempDistance = distance_traveled + newdict[starting_point][x] 
                self.already_used.append(x) 
                if self.fastest_route == 0:
                    print(f"Current Fastest Route is {tempDistance}.")
                    print(f"The pathing it took was {self.already_used}")
                    self.fastest_route = tempDistance
                elif tempDistance < self.fastest_route:
                    print(f"Found a faster route, previous fastest was {self.fastest_route}, new fastest is {tempDistance}.")
                    print(f"The pathing it took was {self.already_used}")
                    self.fastest_route = tempDistance
                else:
                    pass
                self.already_used.pop()
            else:
                if len(self.already_used) > 2:
                        if x == self.already_used[-2]:
                            tempDict = newdict[starting_point]
                            tempList = list(tempDict.keys())
                            if x == tempList[-1]:
                                self.already_used.pop()
                            continue
                         
                for y in self.already_used:
                    tempDict = newdict[starting_point]
                    if y == x:
                        tempDict = newdict[starting_point]
                        tempList = list(tempDict.keys())
                        if len(self.already_used) < 3:    
                            if y == tempList[-1]:
                                self.already_used.pop()
                                continue_stmnt = True
                                break

                        continue_stmnt = True
                if continue_stmnt == True:
                    continue
                tempDistance = distance_traveled + newdict[starting_point][x]
                if fastest_routes != 0: 
                    if fastest_routes < tempDistance:
                        self.already_used.pop()
                        tempDistance = tempDistance - newdict[starting_point][x]
                        break 
                self.already_used.append(x) 
                Rules.fastest_route(self,ending_point,x,tempDistance,self.fastest_route)
                if len(self.already_used) > 2:
                    self.already_used.pop() 





r1 = Rules()
r1.fastest_route('A')