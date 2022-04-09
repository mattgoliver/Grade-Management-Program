import os
import time


response = "" # Initialize placeholder variables
userProvidedData = False
allAssignments = []
assignmentDirectory = {'name': "directory"}
allAssignments.append(assignmentDirectory)
assignment = {}


def logo(): # Prints out logo, returns nothing
  print(" .--------------------------------------------. ")
  print("|      _______                     ______      |")
  print("|     |             /\    /\      |      |     |")
  print("|     |            /  \  /  \     |      |     |")
  print("|     |  _____    /    \/    \    |______|     |")
  print("|     |      |   /            \   |            |")
  print("|     |______|  /              \  |            |")
  print("|                                              |")
  print(" '--------------------------------------------' ")
  print("    Grade Management Program v4.20 by Crover    ")
  print("                                                ")


def clear(): # Clears terminal, returns nothing
  os.system("cls")


def updateAssignmentDirectory(masterList): # Updates the assignment directory, which contains the name of each stored assignment and its index position in the master list, returns updated master list
  
  i = 1
  for item in masterList:# Iterate through each dictionary in the list to find every name
    assignmentDirectory[item["name"]] = i-1 # Add the name along with the index position of that dictionary to a directory dictionary
    i += 1
        
  masterList[0] = assignmentDirectory # Change the first element of masterList to the updated directory dictionary
  return masterList


def addAssignments(masterList): # Add student grade information to the master list, returns master list

  while True: # Repeat process until User is finished adding assignments
    response = ""
    while response.lower() != "yes": # Get name of new assignment
      print("------------------------------")
      assignmentName = input("What is the name of the assignment that you want to enter grades for?")
      response = input("Is '" + assignmentName + "' the correct assignment name?")
    
    print("Assignment name verified - " + assignmentName)
    print("------------------------------")
    print("Type 'exit' when you are finished entering information.")
  
    assignment["name"] = assignmentName # Add name of assignment to beginning of dictionary for easy identification
  
    while True:
      name = input("What is the student's full name?") # Get student's name
      if name.lower() == "exit": # Break while loop if User is finished entering information
        break
      
      grade = input("What is " + name + "'s grade?") # Get student's grade
      
      print(name + " received " + grade)
      
      assignment[name] = grade # Add student's name + grade to the dictionary
      print("------------------------------")
  
    print("------------------------------")
    print("Information added for assignment: " + assignment["name"])
    masterList.append(assignment) # Add assignment information to master list
    
    
    response = input("Would you like to add information for another assignment?") # Allow User to add more assignments
    if response.lower() == "no":
      print("Process completed, information added.")
      
      return updateAssignmentDirectory(masterList)
      break
    else:
      continue
  

def returnNames(lst): # Iterate through master list to print all assignment names, returns string of all names
  names = "" # Create a placeholder string
  
  for assignment in lst: 
    names += assignment["name"] + ", "
  names = names[11:-2] # Cutoff initial 'dictionary' since it isn't needed and cut off the final ', '
  
  return names # Return list (string) of names


def printAssignmentInformation(assignment): # Iterate through individual assignment to print student names along with the grade they received, returns nothing

  assignmentName = assignment["name"]
  print("Printing grade information for " + assignmentName + "... ")
  print("------------------------------")
  
  del assignment["name"] # Remove the 'name' key from the dictionary because the function is looking for student names, not dictionary/assignment names
  

  for i in assignment: # Iterate through student names and print their grade
    print(i + " received " + assignment[i] + "%")
  
  assignment["name"] = assignmentName # Re-add the dictionary name so that the program can keep track of which dictionary is which assignment
  

def selectAssignment(): # Selects an assignment based on input, returns the name of the assignment and the index postion of the assignment on the master list
  # Abstraction
  while True:
      print("------------------------------")
      response = input("Which assignment would you like to select? | Type 'exit' when you are finished requesting information. \n" + returnNames(allAssignments) + ": ")
      
      if response.lower() == "exit": # Break while loop if User is finished requesting information
        clear()
        logo()
        return "exit", 0 # Tell the code that called this function that the User would like to exit, also passes a placeholder index position value
        break
      
      for i in allAssignments[0]: # Search through all assignments for the requested assignment
        if response.lower() == i.lower():
          print("------------------------------")
          return i, allAssignments[0][i] # Return assignment name and index position of the assignment in the master list
          break
      else:
        print("Response did not match any known assignment names, please try again.")
        continue


def curveAssignment(assignment, curveAmount): # Curves all grades on an assignment based on the given amount, returns nothing
  
  for i in assignment: # Iterate through each student in the assignment
    if i == "name": # Skip the name tag for the dictionary
      continue
    
    print(i + " currently has " + assignment[i] + "%, changing to " + str(int(assignment[i]) + int(curveAmount)) + "%")
    
    assignment[i] = str(int(assignment[i]) + int(curveAmount)) # Change grade value by given curve amount


def deleteAssignment(masterList, assignment, assignmentIndex): # Deletes stored assignments
  
  del masterList[assignmentIndex] # Remove assignment dictionary based on given index position
  
  print(assignment + " has been deleted") # Notify User of action
  
  return updateAssignmentDirectory(masterList) # Return master list with assignment deleted and directory updated


def studentSearch(masterList, studentName):
  studentFound = False
  collectedInformation = ""
  
  for assignment in masterList:
    if assignment["name"] == "directory":
      continue
    
    for name in assignment:
      if name.lower() == studentName.lower():
        studentFound = True
        #print(name + " recieved a " + assignment[name] + " on " + assignment["name"])
        
        collectedInformation += ("\n" + assignment["name"] + ": " + assignment[name] + "%")
        #print("Jude Hale grade information:")
        #print(assignment["name"] + ": " + assignment[name] )
  
  print("------------------------------")
  print(studentName + " stored information: ")
  collectedInformation = collectedInformation[1:] + "\n"
  print(collectedInformation)


while True: # User chooses between entering their own students' data or using example data
  clear()
  logo()
  
  response = input("Would you like to use an example data set (1), or input your own data (2)?")
  if response == "1":
    break
  elif response == "2":
    userProvidedData = True
    break
  else:
    print("Try again you lower sat score person and take some time to think about your low IQ") # Very unprofessional
    time.sleep(10)


if userProvidedData == True: # Allows User to input their own data using the 'addAssignments' function
  allAssignments = addAssignments(allAssignments)


if userProvidedData == False: # Provide example data for lazy people
  clear()
  
  print("The example data set includes 3 different assignments with 5 data points for each assignment. This program can store and process as many assignments and student grades as needed.")
  
  assignmentDirectory = {'name': "directory", 'Module 21': 1, 'Module 25': 2, 'Module 29': 3}
  allAssignments[0] = assignmentDirectory
  
  exampleAssignment = {"name": "Module 21", "Jude Hale": "45", "Shane Crooker": "87", "Matthew Oliver": "98", "Ethan Campbell": "34", "Justin Peace": "45"}
  allAssignments.append(exampleAssignment)
  
  exampleAssignment = {"name": "Module 25", "Jude Hale": "44", "Shane Crooker": "34", "Matthew Oliver": "32", "Ethan Campbell": "65", "Justin Peace": "66"}
  allAssignments.append(exampleAssignment)
  
  exampleAssignment = {"name": "Module 29", "Jude Hale": "67", "Shane Crooker": "57", "Matthew Oliver": "64", "Ethan Campbell": "55", "Justin Peace": "79"}
  allAssignments.append(exampleAssignment)
  
  time.sleep(1)
  clear()
  logo()


while True:
  clear()
  logo()
  print("------------------------------")
  
  response = input("What action would you like to take? \n\nView all stored assignments (1) \nAdd additional assignments (2) \nView grade information for an individual assignment (3) \nCurve grades on an assignment (4) \nDelete stored assignment (5) \nSearch for a student (6) \n------------------------------\n")
  
  if response == "1": # View all available assignments
    print("Available assignments: " + returnNames(allAssignments))
    input("\nPress enter to proceed")
    
  elif response == "2": # Add additional assignments
    addAssignments(allAssignments)
    
  elif response == "3": # Print grade information for an individual assignment
    while True:
      assignment, index = selectAssignment()
      if assignment == "exit":
        break
      
      printAssignmentInformation(allAssignments[index])
      time.sleep(1)
      
  elif response == "4": # Curve grades on an assignment
    while True:
      assignment, index = selectAssignment()
      if assignment == "exit":
        break
      
      response = input("How many points would you like to curve the assignment by? ")
      curveAssignment(allAssignments[index], response)
  
  elif response == "5": # Delete stored assignment
    while True:
      assignment, index = selectAssignment()
      if assignment == "exit":
        break
      
      response = input("Are you sure you want to delete '" + assignment + "'?")
      if response.lower() != "yes":
        continue
      
      allAssignments = deleteAssignment(allAssignments, assignment, index)
      
  elif response == "6": # Search for student
    while True:
      response = input("Which student would you like to search for? | Type 'exit' when you are finished requesting information. \n")
      if response.lower() == "exit":
        break
      
      studentSearch(allAssignments, response)


