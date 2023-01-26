#By Brandon Sweat CS1410 1/25/2020

def milesPerGallon(miles,gallons):
    if gallons!= 0:
        mpg = (float(miles)/float(gallons))
        return mpg
    else:
        return 0
    
def createNotebook():
    notebook = []
    return notebook

def recordTrip(notebook,date,milesTraveled,gallons):
    notebook.append({'date':date,'miles':milesTraveled,'gallons':gallons})
    
def listTrips(notebook):
    strings = []
    for x in notebook:
        mpg = milesPerGallon(float(x['miles']),float(x['gallons']))
        strings.append('On '+ str(x['date']) + ': '+ str(x['miles']) + ' miles traveled using ' + str(x['gallons']) + " gallons." + 'Gas mileage: ' + str(mpg) + ' MPG.')
    return strings

def calculateMPG(notebook):
    if notebook == []:
        return 0.0
    else:
        totalMiles = 0
        totalGallons = 0
        for x in notebook:
            if x['gallons'] == 0:
                return 0.0
            totalMiles += x['miles']
            totalGallons += x['gallons']
        totalMPG = totalMiles / totalGallons
        return totalMPG
    
def formatMenu():
    menu =['What would you like to do?', '[r] Record Gas Consumption', '[l] List Mileage History', '[c] Calculate Gas Mileage', '[q] Quit']
    return menu

def formatMenuPrompt():
    menuPrompt = 'Enter an option: '
    return menuPrompt

def getUserString(prompt):
    userString = ''
    while userString == '':
        userString = input(prompt).strip()
    return userString

def getUserFloat(prompt):
    userFloat = input(prompt)
    while type(userFloat) != type(0.0):
        while type
        try:
            userFloat = input(prompt)
        except:
            TypeError('enter a string')
    return userFloat

def getDate():
    date = getUserString('enter date')
    return date

def getMiles():
    miles = getUserFloat('how many miles')
    return miles

def getGallons():
    miles = getUserFloat('how many gallons')
    return miles

def recordTripAction(notebook):
    date = getDate()
    miles = getMiles()
    gallons = getGallons()
    notebook.append(date,miles,gallons)
    print('tanks')
    return notebook

def listTripsAction