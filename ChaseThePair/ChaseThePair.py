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

	min_value = min(setA[0],setB[0])
	max_value =max(setA[len(setA)-1],setB[len(setB)-1])
	return randint(int(min_value), int(max_value))

sets_file = sys.argv[1]

setA,setB = GetSets()
setA.sort(key = SortKey)
setB.sort(key = SortKey)

toChase = GenerateRandomValue()
print (toChase)
print(setA)
print(setB)