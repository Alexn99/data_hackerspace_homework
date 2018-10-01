#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np

def histogram_times(filename):
    hours = list()
    temp = ""
    for i in range(24):
        hours.append(0)
        
    with open(filename) as f:
        csv_reader = csv.reader(f)
        airplane_data = list(csv_reader)
        for j in range(1, len(airplane_data)):
            if airplane_data[j][1]:
                temp += airplane_data[j][1].strip('c: ')[0]
                if airplane_data[j][1].strip('c: ')[1] != ':':
                    temp += airplane_data[j][1].strip('c: ')[1]
                hours[int(temp)] += 1
                temp = ""
    return hours
 
def weigh_pokemons(filename, weight):
    pokemon = list()
    with open(filename) as f:
        pokedex_file = json.load(f)
        for i in range(len(pokedex_file["pokemon"])):
            if pokedex_file["pokemon"][i]["weight"].strip(' kg') == str(weight):
                pokemon.append(pokedex_file["pokemon"][i]["name"])
    return pokemon
    

def single_type_candy_count(filename):
    candyCount = 0
    with open(filename) as f:
        pokedex_file = json.load(f)
        for i in range(len(pokedex_file["pokemon"])):
            if len(pokedex_file["pokemon"][i]["type"]) == 1:
                try:
                    candyCount += pokedex_file["pokemon"][i]["candy_count"]
                except KeyError: #unsure how to avoid this error. Checking candy type against "None" and checking if candy_count exists wouldn't work.
                    pass
    return candyCount

def reflections_and_projections(points):
    rotArr = np.array([[0, -1], [1, 0]])
    projArr = np.array([[1, 3], [3, 9]])
    for n in range(len(points)):
        points[n][1] = -(points[n][1] - 2)
        points[n] = np.matmul(rotArr, points[n])
        points[n] = (1/10) * np.matmul(projArr, points[n])
    return points

def normalize(image):
    image = (255/(np.amax(image) - np.amin(image))) * (image - np.amin(image))
    return image

def sigmoid_normalize(image, a):
    image = 255 * (((1 + np.e**((-(a)**(-1)) * (image - 128))))**(-1))
    return image
