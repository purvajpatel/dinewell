from bs4 import BeautifulSoup
from flask import Flask
import requests
import numpy as np
import pandas as pd
import datetime as dt
import json
import random



def get_food(preferences = "0000"):
    currentTime = dt.datetime.now()
    currDayOfWeek = currentTime.weekday()
    time = currentTime.hour * 60 + currentTime.minute


    timeOfMeals = np.array((420, 660, 990, 1980))
    if(currDayOfWeek >= 5):
        timeOfMeals[0] = 540
    foodTypeEntree = {'-- Baked Potato Bar --', '-- Breakfast --', '-- Specialty Salad of the Day --', '-- Specialty 4 U --', 
                    '-- Rise & Dine --', '-- Grill Line --','-- Pizza & Pasta Line --'}
    notEntreeExceptions = {'Whipped Margarine',  'French Fries', 'Cheese Sauce', 'Country Style Gravy', 'Biscuit', 'Kimchi',
                        'Korean Pickled Cucumbers', 'Garlic Edamame'}
    imageFileNames = ['LegendImages/Vegan.png', 'LegendImages/Veggie.png', 'LegendImages/Peanuts.png', 
                    'LegendImages/Tree_Nuts.png', 'LegendImages/Milk.png']




    url = ""
    if time < timeOfMeals[1]:
        url = "http://hf-food.austin.utexas.edu/foodpro/longmenu.aspx?sName=University+Housing+and+Dining&locationNum=12&locationName=Jester+2nd+Floor+(J2)+Dining&mealName=Breakfast"
    elif time < timeOfMeals[2]:
        url = "http://hf-food.austin.utexas.edu/foodpro/longmenu.aspx?sName=University+Housing+and+Dining&locationNum=12&locationName=Jester+2nd+Floor+(J2)+Dining&mealName=Lunch"
    elif time < timeOfMeals[3]:
        url = "http://hf-food.austin.utexas.edu/foodpro/longmenu.aspx?sName=University+Housing+and+Dining&locationNum=12&locationName=Jester+2nd+Floor+(J2)+Dining&mealName=Dinner"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    allTr = soup.findAll('tr')

    curr = ""
    entreeList = set()
    fruitList = set()
    yogurtList = set()
    soupList = set()
    dessertList = set()
    for tr in allTr:
        div = tr.div
        if div is not None:
            if 'class' in div.attrs and div.attrs['class'][0] == "longmenucolmenucat":
                curr = div.text
            if 'class' in div.attrs and div.attrs['class'][0] == "longmenucoldispname":
                images = tr.findAll('img')
                isVegan = False
                isVeggie = False
                noNut = True
                dairy = False
                for img in images:
                    if img['src'] == imageFileNames[0]:
                        isVegan = True
                    if img['src'] == imageFileNames[1]:
                        isVeggie = True
                    if img['src'] == imageFileNames[2] or img['src'] == imageFileNames[3]:
                        noNut = False
                    if img['src'] == imageFileNames[4]:
                        dairy = True
                if isVegan:
                    isVeggie = True
                works = True
                if preferences[0] == '1' and not isVegan:
                    works = False
                if preferences[1] == '1' and not isVeggie:
                    works = False
                if preferences[2] == '1' and not noNut:
                    works = False
                if preferences[3] == '1' and dairy:
                    works = False
                if works:
                    if curr in foodTypeEntree and div.text not in notEntreeExceptions:
                        entreeList.add(div.text)
                    elif curr == '-- Fresh Fruit --':
                        fruitList.add(div.text)
                    elif curr == '-- Yogurt Bar --':
                        yogurtList.add(div.text)
                    elif curr == '-- Soups --':
                        soupList.add(div.text)
                    elif curr == '-- Desserts --':
                        dessertList.add(div.text)


    chosenEntree = "No Entree"
    chosenSoup = "No Soup"
    chosenFruit = "No Fruit"
    chosenYogurt = "No Yogurt"
    chosenDessert = "No Dessert"
    if len(entreeList) > 0:
        chosenEntree = random.choice(tuple(entreeList))
    if len(soupList) > 0:
        chosenSoup = random.choice(tuple(soupList))
    if len(fruitList) > 0:
        chosenFruit = random.choice(tuple(fruitList))
    if len(yogurtList) > 0:
        chosenYogurt = random.choice(tuple(yogurtList))
    if len(dessertList) > 0:
        chosenDessert = random.choice(tuple(dessertList))
        
    meal = {'Entree': chosenEntree,  'Soup': chosenSoup,  'Fruit': chosenFruit, 'Yogurt': chosenYogurt, 'Dessert': chosenDessert}
    as_json = json.dumps(meal)
    as_object = json.loads(as_json)
    return as_object



