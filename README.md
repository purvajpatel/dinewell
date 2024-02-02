# WhatToEat

![](WhatToEat_Demo.gif)

## Inspiration
With the wide variety of options for meals at the on-campus dining locations, J2 and Kins, many of our friends have expressed their concerns about having a hard time deciding what to choose to eat. Therefore, we wanted to settle this issue for once and for all.

## What it does
Essentially, our website personalizes the user's experience by taking into account the user's dietary restrictions and time-of-day for the meal in order to provide a personalized diet plan for a particular meal of the day.

## How we built it
By inspecting a given meal for a given day at a restaurant of choice, we generate the personalized choice of dishes by looking at each dish's dietary restrictions, which is indicated next to the name of each dish. This ensures that all of the recommended dishes will satisfy the user's dietary restrictions. We do this by creating a Python backend to webscrape and analyze the data that communicates with a Javascript/HTML based frontend by using AJAX and Flask.

## Challenges we ran into
There were two categories of challenges that we faced throughout the event - syntax and algorithmic. For the former, although we had experience working on both Javascript and on Python separately, it was our first time trying to connect the two as frontends and backends. For the latter, the default strategy of choosing dishes is to choose randomly out of all possible options based on restrictions, but we did try to employ some sort of machine learning model to make the caloric inputs work out better, and this was slightly more of a challenge because of time.

## Accomplishments that we're proud of
The biggest thing that we're proud of is that we have a fully functional web app that was able to fully integrate the frontend Javascript and the backend Python.

## What we learned
We learned several different methods for integrating frontend and backend, including Flask.

## What's next for WhatToEat@UT
At the moment, we only support the menus from J2; however, we plan to extend this to Kins Dining in the near future, along with several other on-campus dining restaurants, including Jester City Limits and Littlefield Patio Cafe.
