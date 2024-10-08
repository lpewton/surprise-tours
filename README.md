# Surprise Tours
Surprise Tours is a fake travel agency that allows customers to pick  one of the featured tours at any of the locations shown. Once a tour is chosen, the customer can then purchase it in order to book their spot and will get a confirmation email so they know the payment was correct.

Aside from that, the customer is also able to log in to see their past purchases, save their information, send messages to the store owner or even rate the tours for other users to see.

As per the type of buisness that this is, this is a Business to Customer company (B2C), as the products are sold directly from the store to the customers, without intermediaries. These products are not physical products, but services(tours given by tours guides at a certain date) and are paid off in a single payment (although initially a deposit is paid to secure a spot).

You can find the live link for this website here: [https://lpewton-surprise-tours.herokuapp.com](https://lpewton-surprise-tours.herokuapp.com/)

## TABLE OF CONTENTS:
  * [User Experience (UX):](#user-experience-ux)
    + [App purpose](#app-purpose)
    + [App goals](#app-goals)
    + [Target](#target)
    + [Displays](#displays)
    + [Colors and design](#colors-and-design)
    + [User Stories](#user-stories)
    + [Wireframes](#wireframes)
  * [Database Schema:](#database-schema)
    + [Tour](#tour)
    + [Order](#order)
    + [Order Item](#order-item-each-item-within-the-order)
    + [Message](#message-to-be-sent-to-the-store-owners)
    + [User](#user-profile)
  * [Features](#features)
  * [Marketing Features](#marketing-features)
  * [Requirements.txt](#requirementstxt)
  * [Unfixed bugs and features left to implement](#unfixed-bugs-and-features-left-to-implement)
  * [Major Issues Found](#major-issues-found)
  * [Manual Testing:](#manual-testing)
    + [Tours](#tour-model)
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
The purpose of the Surprise Tours agency is to provide tours for members and allow them to buy tickets for them. Since these tours are a surprise, the customers will not know exactly what they will do during the tour, but they do know where the meeting point is and when to meet.

This solves the issue of having to organise your whole trip, especially for people who don't like the hefty work of planning.


### App goals:
This site's goal is to create a website that allows customers to purchase the tours of their choosing. They can also leave reviews.

Aside from that, the intention is also to permit customers to log in to store their information for future purchases, to see their past trips and to be able to send messages to the store owners.

As an owner, they should be able to add new tours, remove them or edit them so that the tour list is always updated. Owners also approve or reject reviews that the customers leave.

### Target:
The target population for this app is anyone who is willing to travel and wants to avoid the hassle of planning their entire trip.

As for the website administrator, that would be the store owner or anyone responsible for the shop.

### Displays:
The layout of the app is clear, communicative and there is an easy intuition on how to find the information.

### Colors and design:
The colors of this website are consistent with the colors of the agency, blue and green (colours that are usually associated wth travelling and happiness). As for the rest, some other colors are expressed to make the website more intuitive. 

### User Stories:
The Agile methodology has been used during this app’s creation. This has been done by having several user stories created before the development of the project, and following them in order to create it. These can be found below:
1. Tours:
- As a **client**:
  - I want to view all the available tours so that I can choose one
  - I want to sort the products by prices, destination or dates so that I can make an informed decision
  - I want to see the tour’s details so that I know how they are
  - Be warned when a trip is almost sold out so that I don't miss out on it
  - Search for a particular country or city so that I can find tours more easily
- As an **owner**:
  - I want to be able to add, remove or edit tours so that the inventory is updated
  - I want to be able to add reviews to each tour so clients can evaluate them
2. Authorization:
- As a **client**:
  - I want to be able to log in so that I can create an account
  - I want to be able to see my past trips so that I know what I have purchased
- As an **owner**:
  - I want to stop people from entering the restricted pages without being logged in so that I can protect the integrity of the website
3. Purchasing:
- As a **client**:
  - I want to be able to buy an X quantity of the tours I want so that I can book one of them
  - I want to be able to see the total of my purchases so I that know how much I’m spending before I buy them
  - I want to be reminded of what I am purchasing before I pay so I don’t purchase the wrong trip
  - I want to receive an email with the product and the confirmation after purchasing a tour so that I know that everything has been handled correctly
- As an **owner**:
  - I want to stop buyers from buying trips that are sold out

### Wireframes:
Before beggining this project, a few wireframes were created as guidelines to follow for its developement. They were not followed to every detail, but were very useful to build a base. They can be found below:
- Continents page:

![Screen Shot 2023-07-23 at 21 48 17](https://github.com/lpewton/surprise-tours/assets/114712846/230bb121-089f-49e4-95ba-13a253f3571f)

- Tours Page:

![Screen Shot 2023-07-23 at 21 48 53](https://github.com/lpewton/surprise-tours/assets/114712846/a38b4864-1212-441f-b6f8-f2d1c3d817e7)

- Tours detail page:

![Screen Shot 2023-07-23 at 21 49 15](https://github.com/lpewton/surprise-tours/assets/114712846/d2a1366a-09b7-466d-a7dd-131b6da9c255)

- Shopping Bag Page:

![Screen Shot 2023-07-23 at 21 49 39](https://github.com/lpewton/surprise-tours/assets/114712846/e264bfc0-f247-4e74-8204-99912a4f60a0)


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
| Phone Number  | Char Field (Not a number as it can contain parenthesis or other symbols) |
| Nationality  | Country Field | 
| Country  | Country Field | 
| Postcode  | Char Field | 
| Town or City  | Char Field | 
| Street Address 1  | Char Field | 
| Street Address 2  | Char Field | 
| County  | Char Field | 

### Review:
| Entry  | Type |
| ------------- | ------------- | 
| User | Foreign Key (User) | 
| Tour | Foreign Key (Tour) |
| Rating  | Float Field | 
| Review  | Char Field |
| Date  | Date Field | 
| Approved  | Boolean Field | 

## Features:
### Home page:
First page the customer sees with a description of the site's purpose and what they'll find in it:

![image](https://github.com/lpewton/surprise-tours/assets/114712846/e7f8c9b0-3783-49be-b1a7-659c9737d109)


### Contintents page:
Where the customer will choose which continent he wants to purchase their tour in:

![image](https://github.com/lpewton/surprise-tours/assets/114712846/f7faf5b3-541b-437a-a15c-dfc10a54254f)


### Tours page:
All the tours are shown here:

![image](https://github.com/lpewton/surprise-tours/assets/114712846/2cbff7bd-75f5-4dcc-97d7-6f293e26d444)


### Tour detail page:
Where the tour details are shown, such as price, rating, description, images...

![image](https://github.com/lpewton/surprise-tours/assets/114712846/dda3d8a7-2fbf-443e-87c2-c35c6ba208cc)


### Shopping bag:
Where the customer can see their shopping bag to confirm everything is correct before they check out:

![image](https://github.com/lpewton/surprise-tours/assets/114712846/a3715a24-9967-4280-94e5-fb034b28f0ea)


### Check out page:
Where the checkout form is to create the Order and the payments are made. The customer is also reminded of what he is about to purchase:

![image](https://github.com/lpewton/surprise-tours/assets/114712846/a3cd50ef-e721-4518-a907-9828db193d76)


### Check out successful page:
Where the customer is told they payment was successful, they are given an order number and all its details:

![image](https://github.com/lpewton/surprise-tours/assets/114712846/3a294a18-7731-431d-8193-9573bcec167f)


### Log in page:
Where the customer can log in:

![image](https://github.com/lpewton/surprise-tours/assets/114712846/cb13d178-486e-4cf8-8649-eccc4fd554da)


### Log out page:
Where the customer can log out:

![image](https://github.com/lpewton/surprise-tours/assets/114712846/dbff8c65-8629-4e6b-aac0-5d0ea15fa0d2)


### My profile page:
Where the use can input and update their details:

![image](https://github.com/lpewton/surprise-tours/assets/114712846/3f5e30da-778c-4f87-9c43-6d1fd4fd4cad)


### Past trips page:
The past orders the customer made are shown here:

![image](https://github.com/lpewton/surprise-tours/assets/114712846/1ce5715a-42f8-4988-9c7e-2efc2957fe73)


### Past trips details page:
The details of each past order is shown here:

![image](https://github.com/lpewton/surprise-tours/assets/114712846/59ac98e9-8a5b-4ba3-8cde-60234a1aaee4)


### Leave a review page:
Where members can leave reviews for one of the trips:

![image](https://github.com/lpewton/surprise-tours/assets/114712846/264dc0a6-e97a-43cd-b479-fa43bfc18878)


### Add a tour page:
Where the store owner can add tours to the store:

![image](https://github.com/lpewton/surprise-tours/assets/114712846/05c2bf51-e60c-4bde-bb63-e1aa21d6b68c)


### Edit a tour page:
Where the store owner can edit one of the tours:

![image](https://github.com/lpewton/surprise-tours/assets/114712846/cf3f11a8-0258-441a-8e55-623bdfb34ef7)


### Pending reviews page:
Where the store owner can see revies left for tours and approve or reject them:

![image](https://github.com/lpewton/surprise-tours/assets/114712846/899adc0c-f61a-4af7-a264-263d5b82d78f)


### Contact us page:
Where the user can send messages to the administrator or see the page's contact details:

![image](https://github.com/lpewton/surprise-tours/assets/114712846/11673c69-adaa-4958-93ab-a1a955e9f793)


### MailChimp page:
Where the user can subscribe to receive emails and updates:

![image](https://github.com/lpewton/surprise-tours/assets/114712846/c361227e-61fd-4760-b425-c62712167e10)


### Page not found:
Where the customer is directed when the page doesn't exist:

![image](https://github.com/lpewton/surprise-tours/assets/114712846/1ee8ff0f-d7b0-4a68-bfad-85e046b93e78)


## Marketing Features:
Every online store needs digital marketing. For that reason, a Facebook page has been created for this website to reach out to new customers ([https://www.facebook.com/profile.php?viewas=100000686899395&id=100094405940742](https://www.facebook.com/profile.php?id=100094405940742&viewas=&show_switched_toast=false&show_switched_tooltip=false&is_tour_dismissed=false&is_tour_completed=false&show_podcast_settings=false&show_community_review_changes=false&should_open_composer=false&badge_type=NEW_MEMBER&show_community_rollback_toast=false&show_community_rollback=false&show_follower_visibility_disclosure=false&bypass_exit_warning=true)) and a MailChimp account has bee created to maintain the existing customers. It can be found at the bottom of the page: "Subscribe to our Newsletter!"

A screenshot of the Facebook page can be found below:

![image](https://github.com/lpewton/surprise-tours/assets/114712846/aeb8ba48-2fad-4dc5-9af2-ecfbfd39dfc6)

## Requirements.txt:
All needed requirements.txt have been added to the app so it works properly. The main vital ones and also the ones added to improve the functionality of the website. 

## Unfixed bugs and features left to implement:
One of the features of this store is that the users can review a tour. However, an issue found was that the star rating system was not working and there was no time to fix it. However, a progress bar was set up in its stead. This can be fixed with more time, in the future.

Another implementation to add in the future is the ability to search a tour by its dates. At the moment it would be posible to do so but using numerals instead of the month's name. As this seemed confusing, it was removed from the site to be implemented correctly in the future.

Finally, an unfixed bug found in this app is the "Uncaught TypeError: P.trigger(...) is null" found in the console bar in the deployed website. However, this error comes directly from Bootstrap therefore cannot be fixed or removed. It does not affect the functionalityor distribution of the website in any way.

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
- Price cannot have a negative value

### REVIEW MODEL:
- Rating has to be lower than 10 and higher than 0

All form validations have been tested combining customised code and the automatic django validation systems. All of them work properly.

## WEBSITE:
| Test  | Result | Status |
| ------------- | ------------- | ------------- |
| All pages are responsive  | All pages are fully responsive in all screen sizes | PASSED |
| User can only see the pages they're allowed to see  | All user types (administrator and customers) can only see the pages they're allowed to  | PASSED |
| Customers can create an account | They can create an account and receive an email to confirm it  | PASSED |
| Customers can create accounts and log in  | They can do both  | PASSED |
| Logout page allows users to log out  | Logout page works as expected | PASSED |
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
| Passengers cannot exceed number of slots available  | Passengers in a tour cannot be under 0 and cannot exceed number of slots available | PASSED |
| Shopping bag works correctly | Items are added correctly to the shopping bag and can be removed or quantities edited | PASSED |
| Tours in shopping bag cannot be repeated  | If a tour is put in twice, the sum of it will be shown in the shopping bag | PASSED |
| All prices and calculations display the correct ammounts  | They show the correct ammount | PASSED |
| Customers can rate tours  | They can, and the ratings are sent to the owner to approve | PASSED |
| Ratings can be approved or rejected  | They can, the approved ones are shown in the details page, the rejected ones are deleted | PASSED |
| Users have to be authorised to access pages  | If user is not logged in or is not a store owner, they will be redirected to the home page | PASSED |
| Messages work correctly  | All messages are displayed correctly and when they are meant to be | PASSED |
| 404 page works correctly  | 404 page displays properly, the "back to page" button redirects them correctly to the home page | PASSED |


### USER STORIES COMPLETION:
1. As a **client** I want to **view all the available tours** so that I **can choose one**:
   - The tour list is available for all members to see, as intended, and it's responsive to all devices.
2. As a **client** I want to **sort the products by prices, destination or dates** so I **can make an informed decision**:
   - Tours are sorted automatically by ascending price and the users can also sort them acording to other parameters.
3. As a **client** I want to **see the tour’s details** so that I **know how they are**:
   - The details are shown correctly to all users.
4. As a **client** I want to **be warned when a trip is almost sold out** so that I **don't miss out on it**:
   - This is shown in the tours page as a small message when there are less than 5 slots left on a tour.
5. As a **client** I want to **search for a particular country or city** so that I **can find tours more easily**:
   - The searchbar works and it allows the user to search by name or location.
6. As an **owner** I want to **be able to add, remove or edit tours** so that **the inventory is updated**:
   - Store owners can add, remove or edit tours from the database successfully.
7. As an **owner** I want to **be able to add reviews to each tour** so that **clients can evaluate them**:
   - Users can add reviews and the owner can approve or reject them. 
8. As a **client** I want to **be able to log in** so that I **can create an account**:
   - Customers can create accounts successfully and choose their own passwords and usernames.
9. As a **client** I want to **be able to see my past trips** so that I **know what I have purchased**:
   - Users can go into the "Previous trips" page to see past orders.
10. As an **owner** I want to **stop people from entering the restricted pages without being logged in** so that I **can protect the integrity of the website**:
   - Customers cannot access the pages that are only for store managers or that are private to other customers.
11. As a **client** I want to **be able to buy an X quantity of the tours I want** so that I **can book one of them**:
   - The customers can buy as many tour tickets as they want, so long as there are enough slots left.
12. As a **client** I want to **be able to see the total of my purchases** so that I **know how much I’m spending before I buy them**:
   - Customers can find the total of their purchase in the shopping bag and just before they're about to enter their credit card number
13. As a **client** I want to **be reminded of what I am purchasing before I pay** so that **I don’t purchase the wrong trip**:
   - The customer can see what they are about to purchase in the shopping bag and again in the checkout form, so they are reminded twice.
14. As a **client** I want to **receive an email with the product and the confirmation after purchasing a tour** so that **I know that everything has been handled correctly**:
   - After a purchase, customers are sent an email with the details of their order and instructions so they know everything went through properly.
15. As an **owner** I want to **stop buyers from buying trips that are sold out** so that **they are not oversold**:
   - Customers cannot buy tickets on trips that are sold out or purchase more tickets than slots left.

In conclusion, all completed user stories work properly and as intended.

### SECURITY MEASURES:
All app functions were tested several times to make sure they worked under many conditions.

The store owner needs to add double confirmation to delete any tours, so that none are deleted accidentally or by mistake.

Users can only access their pages when they are logged in and in the correct user type. If not, they will be redirected to the home page.

## Validator Testing:
- All HTML templates passed the W3C validator (https://validator.w3.org) without any issues except the {% %} tags.
- All CSS passed the Jigsaw validator (https://jigsaw.w3.org) with no errors found.
- All python code passed the Code Institute Python Linter (https://pep8ci.herokuapp.com/) without any issues.
- The app could be opened from Mozzila Firefox, Chrome and Safari without any issues.
- Stripe payments work correctly and that is verified through webhooks in the stripe website
- This app was passed through the lighthouse test and passed without any issues. Performance is a little bit lower as it's reduced by the use of Stripe and all the images, which are both vital to the app:

![Screen Shot 2023-07-31 at 00 29 30](https://github.com/lpewton/surprise-tours/assets/114712846/f7d37d0b-8a69-4476-9d2a-dbbe8499b23d)


## Technologies Used:
- HTML5
- CSS3
- Bootstrap 5
- Python
- Django
- ElephantSQL
- Stripe

## Deployment:
### In the terminal:
1. Install Django and gunicorn: pip3 install 'django<4' gunicorn
2. Install supporting libraries: pip3 install dj_database_url==0.5.0 psycopg2
3. Install Cloudinary Libraries: pip3 install dj3-cloudinary-storage
4. Create requirements file
5. Create Project
6. Create App 
7. Create requirements file: pip3 freeze --local > requirements.txt
8. Create Project: django-admin startproject STOCK-CONTROLLER 
9. Create App: python3 manage.py startapp stock_controller_app
10. Migrate Changes: python3 manage.py migrate

### In settings.py:
1. Add app to installed apps, at the bottom of the list
2. Set DEBUG = True (For security reasons, it's important to set it back to False at the end of the project)

### In ElephantSQL:
1. Create an external database

### In the Heroku app:
1. Create a new Heroku app
2. In config vars, add the following variables:
- SECRET_KEY: Insert your secret key here
- PORT: 8000
- CLOUDINARY_URL: API environment variable
- DATABASE_URL: value supplied by SQL

### In the app:
1. Create an env.py file in the root directory
2. Link the database, cloudinary and secret key to the env.py file
3. Add the database url, cloudinary url and secret key to the settings.py file, always through the env.py file for security
4. Add the Heroku app to allowed hosts
5. Create the Procfile file
6. Push the project to Github
7. Connect the heroku app to the github repository and click on deploy

# Stripe Deployment:
In order to deploy Stripe on your website, you begin by creating a Stripe account on www.stripe.com. After that, you must copy the JS stripe link at the top of the code and from the Stripe documentation you can copy the Javascript code to accept payments or handle card errors.

Webhooks have been created on this app to ensure that even if something goes wrong, the webhooks create a new order so that it exists even if the website fails to create it.

Bear in mind that all Secret Keys and private Stripe information must remain confidential. Therefore, it is stored in the Environment not available in the live version or github.

To test all payments, you can make paymentby using the following test default credit card number: 4242424242424242 04/24 242.

## Credits:
A lot of this project was based on the projects shown at the Full Stack Software Developement Professional Diploma at Code Institute. Especially the *Boutique Ado* project. Also, a lot of ideas were extracted from the previous projects and various Code Institute marathons.

As for the Stripe payments, the code was extracted from the Stripe Documentation in order to make it work.

Finally, I would also like to thank my friends for giving me advice on the styling of this page, my tutor Martina Terlevic, and the Code Institute student support team for helping me through the tough times while developing the app.
