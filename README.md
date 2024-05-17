# FancyBear Stock App
This is a clone of a repository from my USC Capstone project I worked on with group members. The original repository is private and cannot be accessed. Through this readme, I may speak in the terms "we" or "our" to represent myself and my group members.

Without further ado, the FancyBear Stock App. FancyBear is a web-based platform that simulates the experience of stock trading. Users dive into the world of trading by depositing virtual cash, which they can use to buy and sell stocks in real-time, mimicking the dynamics of the actual stock market. It is aimed to be user-friendly and allows anyone to track their stocks with confidence.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Authors](#authors)

## Overview

### Pages
- **Homepage:** We have a splash page that describes the platform and how to use it.
- Each page has a search bar where they can search for a stock based on the entity name or stock ticker.
- **Favourite Page:** When a user searches stocks, they can like them. The favourites page shows them all the stocks they have liked.
- **Login and Register pages:** The user can create an account or log in. Username and password validation are built in properties with django.
- **Logout page**
- **Deposit/Withdraw page:** The user can add money to their balance. This is not real money but it simulates the idea of adding buying power or withdrawing money.
- **Add Trade page:** This is where the user can buy a stock or sell some or all of a stock they own.
- **Trade History page:** The user can see all the trades they have made with the platform.
- **Stock Details page:** Every stock that is searched or clicked on can have details on their price and more pulled from an API and presented comprehensively. This includes a graph of previous stock price data.
- **Portfolio page:** This page reflects the stocks the user owns, the quantity, and their ROI.


### Backend Technologies
This app was created using [Django](https://www.djangoproject.com/), a [Python](https://www.python.org/) web framework. Django is a very elaborate framework that made it easy to implement many of our funcionality easily. We saved the data on a SQLite database, which is the built-in feature that comes with Django apps. When we hosted the app through [](https://www.heroku.com)Heroku, we used a Postgresql resource.

### Frontend Technologies
The frontend was mainly HTML and CSS with some Django commands. To make the interactions smoother and more seamless, we used some JavaScript (JS). This was either in the HTML or in local, static, JS files.
With StockApp, users can effortlessly manage their investments by adding purchased stocks to our platform and tracking them with ease. The intuitive interface allows users to search for their desired stocks, seamlessly adding or removing them from their portfolio. 

## Features
- Browsing: Users can effortlessly search for stocks and find out more information about them and how they have been performing.
- User Accounts: You can create an account or log into an account already created.
- Responsive Design: Whether accessed from a desktop, tablet, or mobile device, our candy store app adapts seamlessly to provide an optimal viewing experience.
- Trading: Users can buy or sell stocks based on how much buying power they have and how much of a stock they own respectively.
- View Portfolios: Users can see how each of the stocks they own are performing.
- Like Stocks: Users can favourite stocks and view all the stocks they've 'favourited'.

## Installation

In order to build this project you first have to install:

- You need to install Python through this [link](https://www.python.org/downloads/).
- Once you do so and add Python to PATH, go to the path of this project in your terminal and type ```pip install -r requirements.txt```.
This should install all the python libraries you need including Django.

### Setup

Using whatever IDE you prefer, clone the repo to your local machine to work with it.

### Running

While in the fancy-bear directory in the terminal, type ```python manage.py runserver```.
If this does not work, replace python with python3, py, or py3. It is possible that Python may have been saved differently on your device.



## Authors
- [Christian Lee](https://github.com/christian1049)
- [Mark Shperkin](https://github.com/markshperkin)
- [David Eta](https://github.com/david-eta)
- [Sid Gianey](https://github.com/SidGianey)
- [Travis Shuler](https://github.com/Travisandre)
