# Eat

![](WhatToEat_Demo.gif)

## Inspiration

## What it does
Essentially, our website personalizes the user's experience by taking into account the user's dietary restrictions and time-of-day for the meal in order to provide a personalized diet plan for a particular meal of the day.

## How I built it
By inspecting a given meal for a given day at a restaurant of choice, I generated the personalized choice of dishes by looking at each dish's dietary restrictions, which is indicated next to the name of each dish. This ensures that all of the recommended dishes will satisfy the user's dietary restrictions. I do this by creating a Python backend to webscrape and analyze the data that communicates with a Javascript/HTML based frontend by using AJAX and Flask.

## Challenges I ran into
There were two categories of challenges that I faced throughout the event - syntax and algorithmic. For the former, although I had experience working on both Javascript and on Python separately, it was our first time trying to connect the two as frontends and backends. For the latter, the default strategy of choosing dishes is to choose randomly out of all possible options based on restrictions, but I did try to employ some sort of machine learning model to make the caloric inputs work out better, and this was slightly more of a challenge because of time.

## Accomplishments that I'm proud of
The biggest thing that I'm proud of is that I have a fully functional web app that was able to fully integrate the frontend Javascript and the backend Python.

## What I learned
I learned several different methods for integrating frontend and backend, including Flask.


