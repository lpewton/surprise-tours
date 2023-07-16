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
    + [Tour](#tour)
    + [Order](#order)
    + [Order Item](#order-item)
    + [Message](#message)
    + [User](#user-profile)
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

Aside from that, the intention is also to permit customers to log in to store their information for future purchases, to see their past trips and to be able to send messages to the store owners.

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
  - I want to sort the products by prices, destination or dates so that I can make an informed decision
  - I want to see the tour’s details so that I know how they are
  - Be warned when a trip is almost sold out so that I don't miss out on it
  - See all of the best deals easily so that I know what to purchase
  - Search for a particular country or city so that I can find tours more easily
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

## Features:
### Home page:
First page the customer sees with a description of the site's purpose and what they'll find in it:

### Contintents page:
Where the customer will choose which continent he wants to purchase their tour in:

### Tours page:
All the tours are shown here:

### Tour detail:
Where the tour details are shown, such as price, rating, description, images...

### Shopping bag:
Where the customer can see their shopping bag to confirm everything is correct before they check out:

### Check out page:
Where the checkout form is to create the Order and the payments are made. The customer is also reminded of what he is about to purchase:

### Check out successful page:
Where the customer is told they payment was successful, they are given an order number and all its details:

### Log in page:
Where the customer can log in:

### Log out page:
Where the customer can log out:

### My profile page:
Where the use can input and update their details:

### Past trips page:
The past orders the customer made are shown here:

### Past trips details page:
The details of each past order is shown here:

### Add a tour page:
Where the store owner can add tours to the store:

### Edit a tour page:
Where the store owner can edit one of the tours:

### Page not found:
Where the customer is directed when the page doesn't exist:

## Requirements.txt:
All needed requirements.txt have been added to the app so it works properly. The main vital ones and also the ones added to improve the functionality of the website. 

## Features left to implement:
AIXÒ AL FINAL

## Major Issues Found:
1. Crispy forms not compatible with Stripe:
- For some reason unknown, whenever I added crispy forms to the payment form, it stopped working. Hours of troubleshooting myself and with the Code Institute tutors did not provide a solution.
- I then changed the form through CSS manually to make it look like Crispy Forms.

## Manual Testing:
### TOUR MODEL:
- Names are unique
- Start date must be late than the same day
- End date must not be sooner than the start date
- Slots left cannot be more than slots available
- Rating has to be higher than 0 and lower than 10
- Price must be higher or equal to 1

All form validations have been tested combining customised code and the automatic django validation systems. All of them work properly.

## WEBSITE:
| Test  | Result | Status |
| ------------- | ------------- | ------------- |
| All pages are responsive  | All pages are fully responsive in all screen sizes | PASSED |
| User can only see the pages they're allowed to see  | All user types (administrator and customers) can only see the pages they're allowed to  | PASSED |
| Customers can create an account | They can create an account and receive an email to confirm it  | PASSED |
| Customers can log in  | They can log in  | PASSED |
| Logout page allows users to be logged out  | Logout page works as expected | PASSED |
| Users can see the correct pages when logged in  | All user types (administrator and customers) can see the pages correctly, if they are not logged in, they are shown the log in option  | PASSED |
| Customers can update their details | Customers can update their personal details correctly through validation and error messages | PASSED |
| Customers can see their past orders  | Past orders are seen correctly with the appropriate displayed details  | PASSED |
| Store owners can add tours to the website  | Only store owners can add new tours, and they are added correctly through form validation and error messages | PASSED |
| Store owners can edit tours in the stock  | Only store owners can edit tour details, and they are correctly edited through form validation and error messages | PASSED |
| User can delete tours | Only store owners can delete tours, and they are deleted correctly through form validation and messages | PASSED |
| There is double confirmation before deleting a tour | A modal pops up to ensure that deletion is intentional, the deleted item is the correct one and all the buttons work correctly | PASSED |
| All tours are shown in tours page  | All tours are shown correctly when loading the page | PASSED |
| Tour ordering  | Tours are ordered by price (lower to higher) by default and the ordering parameters can be changed  | PASSED |
| Tour messages display correctly  | Tour details are displayed correctly and they show the right message | PASSED |
| Tour searching  | Search tours works correctly and can search by the correct keywords | PASSED |
| Customers can choose how many tours to purchase  | Add and remove passenger buttons work correctly in both the tour detail and shopping bag pages | PASSED |
| Passengers cannot exceed number of slots  | Passengers in a tour cannot be under 0 and cannot exceed number of slots available | PASSED |
| Shopping bag works correctly | Items are added correctly to the shopping bag and can be removed or quantities edited | PASSED |
| Tours in shopping bag cannot be repeated  | If a tour is put in twice, the sum of it will be shown in the shopping bag | PASSED |
| All prices and calculations display the correct ammounts  | They show the correct ammount | PASSED |
| Users have to be authorised to access pages  | If user is not logged in or is not a store owner, they will be redirected to the home page | PASSED |
| Messages work correctly  | All messages are displayed correctly and when they are meant to be | PASSED |
| 404 page works correctly  | 404 page displays properly, the "back to page" button redirects them correctly to the home page | PASSED |

REVISA AIXÒ PER SI DE CAS

### USER STORIES COMPLETION:
1. As a **client** I want to **view all the available tours** so that I **can choose one**:
- The tour list is available for all members to see, as intended, and it's responsive to all devices.
2. As a **client** I want to **sort the products by prices, destination or dates** so I **can make an informed decision**:
- Tours are sorted automatically by ascending price and the users can also sort them acording to other parameters
3. As a **client** I want to **see the tour’s details** so that I **know how they are**:
- The details are shown correctly to all users 
4. As a **client** I want to **be warned when a trip is almost sold out** so that I **don't miss out on it**:
- This is shown in the tours page as a small message when there are less than 5 slots left on a tour
5. As a **client** I want to **see all of the best deals easily** so that I **know what to purchase**:

  
  - Search for a particular country or city so that I can find tours more easily
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

