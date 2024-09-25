#!/usr/bin/env python3

#Name: Jerrico Gomez
#Student Number: 131382228

def inches_to_cm(inches):
  
  return inches * 2.54

def cm_to_inches(cm):
  
  return cm / 2.54

while True:
  print("1. Convert inches -> cm")
  print("2. Convert cm -> inches")
  print("Make your selection (1,2): ")

  #user selection
  selection = input()

  #validate selection
  if selection not in ("1", "2"):
    print("Invalid entry")
    continue  # Skip to the next iteration of the loop

  # Get user input to convert
  if selection == "1":
    print("Enter inches: ")
    inches = int(input())
    result = inches_to_cm(inches)
    print(f"Number of cm: {result:.2f}")  # result with 2 decimal places
  else:
    print("Enter cm: ")
    cm = int(input())
    result = cm_to_inches(cm)
    print(f"Number of inches: {result:.4f}")  # Format result with 4 decimal places

  # Ask to continue
  print("\nNeed to convert again? (yes/no): ")
  choice = input().lower()
  if choice != "yes":
    break

print("End. Thank You.")
