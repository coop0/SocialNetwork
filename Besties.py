def friend_besties(individual, bestie_dict):
    ''' Recieves the individual and a besties dictionary, sorts the besties of 
        the individual and outputs this as a list.
    '''
    try:  # Returns if the key exists
        output = sorted(list(bestie_dict[individual]))  
        return output
    except:  # return a empty list as the individual is not in dict
        return []
def friend_second_besties(individual, bestie_dict):
    ''' Recieves the individual and bestie dict, works out the second degree 
        friends of the individual and returns this list 
    '''
    seconddeg = []  # Second degree friends including besties and self
    output = []
    individualsbesties = friend_besties(individual, bestie_dict)
    for keys in bestie_dict:  # Adds all the bestie dict names to a list
        for names in individualsbesties:
            if keys == names:
                seconddeg.append(list(bestie_dict[names]))
    # Adds only the second besties to a list                         
    for i in range(len(seconddeg)):  
        bestie = False  # Variable to check if their are a bestie or selves
        for k in range(len(seconddeg[i])):    
            if (seconddeg[i][k] in individualsbesties or 
                seconddeg[i][k] == individual):
                bestie = True 
            if not bestie:
                output.append(seconddeg[i][k])
            else:
                bestie = False  
    # Returns the second besties       
    return sorted(output)     
