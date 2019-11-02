import sys
import os
from random import seed
from random import randint
import random
import time



def GetSets():
	file = open(sets_file,"r")
	sets = file.readline().split("[")
	setA = sets[1].split("]")[0].split(",")
	setB = sets[2].split("]")[0].split(",")
	return setA,setB

def SortKey(element):
	return int(element)

def GenerateRandomValue():
	random.seed(time.time() * 256)

	min_value = max(setA[0],setB[0])
	max_value =min(setA[len(setA)-1],setB[len(setB)-1])
	return randint(int(min_value), int(max_value))

def ClosestNumber(setNumbers):

	if len(setNumbers) <= 2:
		closest_number = 0
		first_element = int(setNumbers[0])
		second_element = int(setNumbers[1])
		difference_first_element = max(first_element, toChase) - min(first_element, toChase)
		difference_second_element = max(second_element, toChase) - min(second_element, toChase)

		if difference_first_element <= difference_second_element :
			 closest_number = first_element
		else:
			closest_number = second_element
		return closest_number

	mid = int((len(setNumbers)-1)/2)
	
	
	if int(setNumbers[mid]) == toChase:
		return setNumbers[mid]

	if int(setNumbers[mid]) < toChase:
		return ClosestNumber(setNumbers[mid:])

	else: 
		return ClosestNumber(setNumbers[:mid+1])


def GetClosestNumbers():
	result = []
	result.append(ClosestNumber(setA))
	result.append(ClosestNumber(setB))
	return result

sets_file = sys.argv[1]

setA,setB = GetSets()
setA.sort(key = SortKey)
setB.sort(key = SortKey)

toChase = GenerateRandomValue()
result =  GetClosestNumbers()

print (toChase)
print(setA)
print(setB)
print (result)
