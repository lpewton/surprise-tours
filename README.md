# Surprise Tours:

Surprise Tours is a fake travel agency that allows customers to pick  one of the featured tours at any of the locations shown. Once a tour is chosen, the cusomer can then purchase it in order to book their spot and will get a confirmation email so they know the payment was correct.

Aside from that, the customer is also able to log in to see their past purchases, save their information or send messages to the store owner.

You can find the live link for this website here: [https://lpewton-stock-controller.herokuapp.com.](https://lpewton-surprise-tours.herokuapp.com/)

## TABLE OF CONTENTS:
  * [User Experience (UX):](#user-experience-ux)
    + [App purpose](#app-purpose)
    + [App goals](#app-goals)
    + [Target](#target)
    + [Displays](#displays)
    + [Colors and design](#colors-and-design)
    + [User Stories](#user-stories)
  * [Roles and Registration](#roles-and-registration)
  * [Database Schema:](#database-schema)
    + [Ingredient](#ingredient)
    + [Recipe](#recipe)
    + [Custom User](#custom-user)
  * [Features](#features)
  * [Requirements.txt](#requirementstxt)
  * [Features left to implement](#features-left-to-implement)
  * [Unfixed bugs](#unfixed-bugs)
  * [Major Issues Found](#major-issues-found)
  * [Manual Testing:](#manual-testing)
    + [Ingredient](#ingredient-model)
    + [Recipes](#recipes-model)
    + [Website](#website)
    + [User Stories Completion](#user-stories-completion)
    + [Security Measures](#security-measures)
  * [Validator Testing](#validator-testing)
  * [Technologies Used](#technologies-used)
  * [Deployment:](#deployment)
    + [In the terminal](#in-the-terminal)
    + [In settings.py](#in-settingspy)
    + [In ElephantSQL](#in-elephantsql)
    + [In the Heroku app](#in-the-heroku-app)
    + [In the app](#in-the-app)
  * [Credits](#credits)

## User Experience (UX):

### App purpose:
The purpose of the Surprise Tours agency is to provide tours for members and allow them to buy them. Since these tours are a surprise, the customers will not know exactly what they will do during the tour, but they do know where the meeting point is and when to meet.

This solves the issue of having to plan your whole trip, especially for people who don't like the hefty work of planning.


### App goals:
This site's goal is to create a website that allows customers to purchase the tours of their choosing.

Aside from that, the intention is also to permit users to log in to store their information for future purchases, to see their past trips and to be able to send messages to the store owners.

As an owner, they should be able to add new tors, remove them or edit them so that the tour list is always updated.

### Target:
The target population for this app is anyone who is willing to travel, and wants to avoid the hassle of planning their entire trip.

As for the website administrator, that would be the store owner and their credentials are the following:

| Role  | Username | Password |
| ------------- | ------------- | ------------- |
| Superuser  | admin | casagelat |
| Customer  | auri | brasileiro |

### Displays:
The layout of the app is clear, communicative and there is an easy intuition on how to find the information.

### Colors and design:
The colors of this website are consistent with the colors of the agency, blue and yellow (colours that are usually associated wth travelling). As for the rest, some other colors are expressed to make the website more intuitive. 

### User Stories:
The Agile methodology has been used during this app’s creation. This has been done by having several user stories created before the development of the project, and following them in order to create it. These can be found below:
1. Tours:
- As a **client**:
  - I want to view all the available tours so that I can choose one
  - I want to sort the products by prices, destination or dates so I can make an informed decision
  - I want to see the tour’s details so I know how they are
  - Be warned when a trip is almost sold out
  - See all of the best deals easily
  - Search for a particular country or city
- As an **owner**:
  - I want to be able to add, remove or edit tours so that the inventory is updated
  - I want to be able to add reviews to each tour so clients can evaluate them
2. Authorization:
- As a **client**:
  - I want to be able to log in
  - I want to be able to see my past trips
- As an **owner**:
  - I want to stop people from entering the restricted pages without being logged in
3. Purchasing:
- As a **client**:
  - I want to be able to buy an X quantity of the tours I want
  - I want to be able to see the total of my purchases so I know how much I’m spending before I buy them
  - I want to be reminded of what I am purchasing before I pay so I don’t purchase the wrong trip
  - I want to receive an email with the product and the confirmation after purchasing a tour so I know that everything has been handled correctly
- As an **owner**:
  - I want to stop buyers from buying trips that are sold out

## Database Schema:
### Tour:
| Entry  | Type |
| ------------- | ------------- | 
| Name  | Char Field | 
| Continent  | Foreign Key(Continent) | 
| Start  | Date Field |
| End  | Date Field | 
| Slots  | Integer Field | 
| Slots Left  | Integer Field | 
| Rating | Float Field |
| Price | Float Field | 
| Image 1 | Image Field | 
| Image 2 | Image Field | 
| Image 3 | Image Field | 
| Description | Char Field | 

### Order:
| Entry  | Type |
| ------------- | ------------- | 
| Order Number  | Char Field | 
| User Profile  | Foreign Key (UserProfile) | 
| Full Name | Char Field |
| Email  | Email | 
| Phone Number  | Char Field |  CAMBIA QUAN I SI TOCA
| Nationality  | Country Field | 
| Country  | Country Field | 
| Postcode  | Char Field | 
| Town or City  | Char Field | 
| Street Address 1  | Char Field | 
| Street Address 2  | Char Field | 
| County  | Char Field | 
| Date  | Date Field | 
| Show Date  | Date Field | 
| Order Total  | Decimal Field | 
| Original Bag  | Text Field | 
| Stripe PID  | Char Field | 


### Order Item (each item within the Order):
| Entry  | Type |
| ------------- | ------------- | 
| Order  | Foreign Key (Order) | 
| Tour  | Foreign Key (Tour) | 
| Quantity  | Integer Field |
| Item Total  | Decimal Field |

### Message (to be sent to the store owners):
| Entry  | Type |
| ------------- | ------------- | 
| Full name  | Char Field | 
| Email  | Email Field | 
| Subject  | Char Field |
| Message | Char Field |

### User Profile:
| Entry  | Type |
| ------------- | ------------- | 
| User | One to One Field (User) | 
| Full Name | Char Field |
| Email  | Email | 
| Phone Number  | Char Field |  CAMBIA QUAN I SI TOCA
| Nationality  | Country Field | 
| Country  | Country Field | 
| Postcode  | Char Field | 
| Town or City  | Char Field | 
| Street Address 1  | Char Field | 
| Street Address 2  | Char Field | 
| County  | Char Field | 


