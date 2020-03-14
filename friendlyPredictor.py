import operator
from collections import defaultdict
from Besties import *
def spaceswap(swaplist):
    ''' Removes spaces from the input replacing them with underscores
    '''
    for word in range(len(swaplist)):
        string = ''
        a = list(swaplist[word])
        # Calculate the new string for the word using _'s
        for i in range(len(a)):
            if a[i] == '' or a[i] == ' ':
                string += '_'
            else:
                string += a[i]
        swaplist[word] = string
    return swaplist
def returner(unknown_user, features, bestie_dict, feat_dict, function):
    ''' Takes in all the variables and returns a dictionary containing the
    relevent features of the friends
    '''
    besties = function  # Gets the list of relevent people
    bestiefeatslist = []  # list of dictionaries of features
    dictionary = {}  # Holds all the information about the besties features
    dictionarya = {}  # output dictionary holding relevent feats
    # Append dictionarys to the list
    for i in range(len(besties)):
        if besties[i] in feat_dict:
            bestiefeatslist.append(feat_dict[besties[i]])
    # Add items to the dictionary from the bestie list
    for items in features:
        holdinglist = [] 
        for k in range(len(bestiefeatslist)):
            try:
                holdinglist.append(bestiefeatslist[k][items])
            except:
                continue
        dictionary[items] = spaceswap(holdinglist)
    # calculate the quantity of the feats repeating amongst friends
    for keys in dictionary:
        newdictionary = defaultdict(int)
        dickeys = sorted(dictionary[keys])
        for i in range(len(dickeys)):
            newdictionary[dickeys[i]]+= 1
        dictionarya[keys] = newdictionary
    return dictionarya
def getorder(bestieinfo):
    ''' Sorts the input and returns a list with the underscores changed back to
    spaces and returns that list
    '''
    outputlist = []
    sortedlist2 = (sorted(bestieinfo.items(), key=operator.itemgetter(1), 
                          reverse=True))
    sortedlist3 = sorted(sortedlist2)
    sortedlist = sorted(sortedlist3, key=operator.itemgetter(1), reverse=True)
    # Replaces the _ with ' ' 
    for tuples in sortedlist:
        word = tuples[0].replace('_', ' ')
        outputlist.append(word)
    return outputlist
        
def friendly_prediction(unknown_user, features, bestie_dict, feat_dict):
    ''' Main in the program gets the information and calculates the output 
    dictionary predicting the features of the unknown user
    '''
    bestieinfo = dict(returner(unknown_user, features, bestie_dict, feat_dict,
                               friend_besties(unknown_user, bestie_dict)))
    secondbestieinfo = dict(returner(unknown_user, features, bestie_dict,
                           feat_dict, 
                           friend_second_besties(unknown_user, bestie_dict)))
    outputdict = {}
    # Arrange so that if we are missing values from besties add it from seconds
    for keys in secondbestieinfo:
        if bestieinfo[keys] == {}:
            bestieinfo[keys] = secondbestieinfo[keys]
    # Order the output        
    for key in bestieinfo:
        outputdict[key] = getorder(bestieinfo[key])
    return outputdict   


#Examples with input
#print(friendly_prediction('glenn', {'favourite author', 'university'}, {'kim': {'sandy', 'alex', 'glenn'}, 'sandy': {'kim', 'alex'}, 'alex': {'kim', 'sandy'}, 'glenn': {'kim'}}, {'glenn': {'university': ''}, 'kim': {'favourite author': 'AA Milne'}, 'sandy': {'favourite author': 'JRR Tolkien', "university": "University of Melbourne"}, 'alex': {'favourite author': 'AA Milne', 'university': 'Monash University'}}))
#print(friendly_prediction('kim', {'university'}, {'kim': {'sandy', 'alex', 'glenn'}, 'sandy': {'kim', 'alex'}, 'alex': {'kim', 'sandy'}, 'glenn': {'kim'}}, {'glenn': {'university': ''}, 'kim': {'favourite author': 'AA Milne'}, 'sandy': {'favourite author': 'JRR Tolkien', "university": "University of Melbourne"}, 'alex': {'favourite author': 'AA Milne', 'university': 'Monash University'}}))
#print(friendly_prediction('kim', {'birthplace'}, {'kim': {'sandy', 'alex', 'glenn'}, 'sandy': {'kim', 'alex'}, 'alex': {'kim', 'sandy'}, 'glenn': {'kim'}}, {'glenn': {'university': ''}, 'kim': {'favourite author': 'AA Milne'}, 'sandy': {'favourite author': 'JRR Tolkien', "university": "University of Melbourne"}, 'alex': {'favourite author': 'AA Milne', 'university': 'Monash University'}}))
