# Our Neighbourhood

## Overview

[Our Neighbourhood](http://ci-milestone4.herokuapp.com/) is a service that enables communities to share and promote local events, activities, services and businesses.

## Table of Contents

<details>
  <summary>UX</summary>

  - [UX section](#ux-section)  
  - [User stories](#user-stories)  
  - [Wireframes](#wireframes)  
</details>

<details>
  <summary>Features</summary>

  - [Features Section](#features-section)
  - [Existing Features](#existing-features)
     * [Content structure](#app-structure)
     * [Profile](#profile)
     * [Event](#events)
     * [Events page](#events)
     * [Checkout](#checkout)
     * [Registration](#registration)
     * [Admin Panel](#admin-panel)
     * [Contact page](#contact-page)
     * [Error pages](#error-pages)
  - [Features Left to Implement](#features-left-to-implement)

</details>

<details>
  <summary>Database Schema</summary>

- [Database Schema](#database-schema)

</details>

<details>
  <summary>Technologies</summary>

  - [Technologies Section](#technologies-section)
  - [Programming Languages](#programming-languages)
  - [Other Tools](#other-tools)

</details>

<details>
  <summary>Testing</summary>

  - [Testing Documentation](https://github.com/stefcruz/ci_milestone4/blob/master/TESTING.md)
</details>

<details>
  <summary>Deployment</summary>

  - [How to provision a PostGres database on Heroku](#how-to-publish-to-heroku)
  - [How to deploy to Heroku](#how-to-publish-to-heroku)
  - [How to fork this repository](#how-to-fork-this-repository)
  - [How to open this project locally](#how-to-open-this-project-locally)
</details>

<details>
  <summary>Credits</summary>

  - [Credits section](#credits-section)
  - [Images](#images)
</details>

<details>
  <summary>Acknowledgements</summary>

  - [Acknowledgements section](#acknowledgements-section)
  - [Design](#design)
  - [Code](#code)
</details>

## UX

### User stories

As a website user I want to be able to…

Registration
- Register for an account so I can use the website service
- Receive a confirmation email when registering for an account so I can make sure the account was created
- Log in and log out of my account so that I can come and go from the website
- Recover my password if I forget it so that I can access the website again
- Have a personalised user profile so that I can view, edit and delete my personal information
- Upload services with a name, description, price and pictures so that I can promote an activity that will be visible on the community board

Events
- Create events to be published on the site
- Edit events I created
- Delete events I created
- Access all the events and filter by category and upcoming events
- View details of the events that are on the events board

Checkout
- Securely pay for the events I create
- Receive a confirmation email after I place an order

Contact
- Contact the site in case I have any issues

As a website admin I want to be able to…  

- Visualise all the contact requests and events on one page
- Perform actions such as mark events as paid, edit and delete events and mark contact requests as resolved

### Wireframes

The wireframes for this project can be seen [here](https://www.figma.com/file/yfUmkr3ZyPUhC23yjcaqch/Our-Neighourhood?node-id=0%3A1).

[![img](https://github.com/stefcruz/ci_milestone4/blob/master/readme/wireframes.png)](https://www.figma.com/file/yfUmkr3ZyPUhC23yjcaqch/Our-Neighourhood?node-id=0%3A1)

## Features

### Existing Features

#### Content structure

**Front-end pages**:  

_Unregistered users_
  - Home
  - Login
  - Register
  - Events board
  - Faq
  - Contact

_Registered users_
  - Home
  - Faq
  - Profile
  - Account Management (change password, change email address)
  - Events board
  - Create/ Edit/ Delete events

**Django apps used to create the site:**
  - Home (index, faq)
  - Profiles
  - Events
  - Checkout
  - Contact
  - Event admin


#### Profile

The profile view contains an accordion with 3 tabs, account, posts and settings.

In the account tab, the user can edit their name, bio and upload a profile picture.  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/profile-account.png" width="600">

In the posts tab, the user can create new events and see the events they posted.  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/profile-posts.png" width="6000">

The user can perform the CRUD operations by clicking on the buttons in the event card.  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/event-card.png" width="350">

In the settings tab, the user can change their email address, password or deactivate their account.  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/profile-settings.png" width="450">

Deactivate account pop up.  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/deactivate-account.png" width="450">

Change email address page.  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/change-email-address.png" width="450">

Change password page.  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/change-password.png" width="450">

#### Event

In the posts tab on the profile page, the user can perform the CRUD operations on the events they created. 

Create event.  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/create-event.png" width="450">

Preview event.  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/preview-event.png" width="450">

Edit event.  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/edit-event.png" width="450">

Delete event.  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/delete-event.png" width="450">

#### Events page

The user can filter by category and upcoming events (where event date is greater than today).  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/filter-dropdown.png" width="200">  

Filter example, filtering by category Arts.  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/filter.png" width="300">

The search functionality searches the keyword that matches the event title or description.  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/search.png" width="450">

View event detail, where only the user who created the event is able to see the buttons edit or delete event.  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/event-detail.png" width="450">

#### Checkout

The checkout is powered by Stripe.  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/checkout-review-order.png" width="450">

Checkout success page.  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/checkout-success.png" width="450">

The user gets a confirmation email after an event is posted.    
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/confirmation-email.png" width="450">

#### Registration
##### Sign up
Users can sign up with email, Facebook and Google. The library allauth enabled this functionality.   
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/sign-up.png" width="450">  

##### Log in
Similarly, users can log in using email or their Facebook and Google social accounts.  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/log-in.png" width="450">

#### Admin panel

The admin panel displays the contact requests and the events.

Contact requests are listed on a table and enables the admin to mark the requests as resolved.  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/contact-requests.png" width="450">  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/actions-contact.png" width="150">

Events are shown on a table and enables the admin to mark them as paid so they are displayed on the events board. The admin can also edit or delete events.   
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/event-management.png" width="450">  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/actions-events.png" width="150">


#### Contact page
The contact page is a form that the user can select the reason for contact so their query can be looked after more promptly.  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/contact.png" width="450">  

#### Error pages
The custom error pages created are for the 404 and 500 errors.  
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/error-page.png" width="450">

#### Features Left to Implement
The nice to have features that were not implemented on this project are:

  - Admin panel: enable the admin to reply to the email without leaving the application.
  - Scalability idea: Locate the user and suggest the neighbourhood where they want to see events in.
  - Address validation so users cannot insert an event outside the selected neighbourhood. Maybe hook up Google auto complete to address field.
  - Price field on add_event.html could accept euro sign

## Database Schema

This project's database contains 4 tables: UserProfile, Order, Event and Contact.

The Django Auth User table feeds the UserProfile table via a `OneToOneField`. The UserProfile table is linked to the Event and Checkout tables via a Foreign Key, establishing a `OneToMany` relationship. 

The Contact table is its own entity and does not establish any relationship with the other tables.  

ER Diagram - Allauth and django tables included  
[![ER Diagram all in](https://github.com/stefcruz/ci_milestone4/blob/master/readme/er-diagram-allin.png)](https://github.com/stefcruz/ci_milestone4/blob/master/readme/er-diagram-allin.png)

ER diagram - only the project apps  
[![ER Diagram project apps](https://github.com/stefcruz/ci_milestone4/blob/master/readme/er-diagram-project-apps.png)](https://github.com/stefcruz/ci_milestone4/blob/master/readme/er-diagram-project-apps.png)


## Technologies

### Programming Languages

- Python  
  The Python framework [Django](https://www.djangoproject.com/) was used to create this project, following the Model-View-Template design pattern.
- PostgreSQL  
  The relational database used in this application.
- HTML5  
  Markup language used across the app.
- CSS3  
  Page style.
- Bootstrap 5   
  This project used Bootstrap design elements such as navbar, grid & cards.
- SASS  
  CSS preprocessor.
- JavaScript  
  Front end functionalities.


### Other Tools

- GitHub  
  Used to store this project's source code.
- Heroku  
  Used to host this app.
- Pycharm  
  IDE of choice to write this project.
- Figma  
  Creation of wireframes.
- Stripe  
  Payment functionality.
  
## Testing

Testing documentation is available [here](https://github.com/stefcruz/ci_milestone4/blob/master/TESTING.md).

## Deployment

This project's source code is hosted on GitHub and deployed to Heroku. It was created using Pycharm.

A clone of this repository was made locally, and the changes were deployed directly in the master branch. The commands used to push the changes were `git add .`, `git commit -m "message"` and `git push`. All the commits can be clearly identified by a concise and meaningful message.

### How to provision a Postgres database on Heroku

Before deploying to Heroku first provision a database on Heroku and apply migrations to Postgres following the below:

1. Create an account and log in to Heroku
2. On the apps page select NEW.
3. Give the app a name and select the closest region, then click Create App.
4. Navigate to the Resources tab and search for ‘Heroku Postgres’ on the search bar under Add-ons
5. Select plan name and click on ‘Submit Order Form’ (this project uses Hobby Dev - Free)

In order to connect to Postgrest from Heroku, save the Database URL navigating to the Settings tab and clicking Reveal Config Vars.

**In the IDE**:  
- Install packages `psycopg2` and `gunicorn`  
`pip3 install psycopg2-binary`  
`pip3 install gunicorn`  
`pip3 install dj_database_url`
- Create requirements.txt file so Heroku knows which dependencies to install.
`pip3 freeze --local > requirements.txt`
- Create procfile  
`echo web: gunicorn PROJECTNAME.wsgi:application > Procfile`
- Get the database URL from Heroku through the CLI (heroku config) or Heroku website (settings tab > click on reveal config vars > get database url)
- Navigate to settings.py located in the main project’s folder and add the imports at the top  
`import dj_database_url`  
`import os`
- On the same settings.py file, comment out the existing DATABASE code and and add the following:

` DATABASES = {`  
        `'default': dj_database_url.parse( ** DB URL from Heroku ** )`  
    `}`
  
- Run migrations to the Postgres database, which will apply the migrations from the local database.  
`python3 manage.py migrate`
- Still on the settings.py file, add hostname of the Heroku app  
`ALLOWED_HOSTS = [‘project-name.herokuapp.com’]`
- Before pushing to git make sure the .gitignore file contains the following files:
`*sqlite3`  
`__pycache__/`
- Push to github  
`git add .`  
`git commit -m “Your commit message”`  
`git push`


### How to deploy to Heroku

There are two ways to deploy to Heroku. One is installing Heroku on your project and pushing changes to Heroku and the other is setting the automatic deployment from GitHub, which is easier.

Both require the creation of the app on the Heroku website or through the CLI (instructions [here](https://devcenter.heroku.com/articles/creating-apps)).

Enabling automatic deployment from GitHub:

1. Assuming the requirements.txt has been created already as per above, update file in case there is a new package installed  
``pip3 freeze --local > requirements.txt``
2. Make sure the Procfile is at the project level, if not create one, then push requirements and procfile to git  
`echo web: gunicorn PROJECTNAME.wsgi:application > Procfile`
3. Add the environment variables to Heroku in Settings > Config Vars. I used the following on this project:
   
SECRET_KEY  
DEVELOPMENT  
LOCALHOST  
DATABASE_URL  
AWS_ACCESS_KEY_ID  
AWS_SECRET_ACCESS_KEY  
STRIPE_PUBLIC_KEY  
STRIPE_SECRET_KEY  
STRIPE_WH_SECRET  
FACEBOOK_APP_ID  
FACEBOOK_APP_SECRET  
GOOGLE_CLIENT_ID  
GOOGLE_SECRET  
EMAIL_HOST_USER  
EMAIL_HOST_PASS  

5. Go to Deploy > connect the repo name > enable automatic deploy from master branch, then go to the next section ‘Manual Deploy’ and click on ‘Deploy Branch’

Installing Heroku on your project:
1. Create app on Heroku website
2. Make sure your project has requirements.txt file so Heroku knows which dependencies to install. To create one ``pip3 freeze --local > requirements.txt``
3. Install Heroku on your project ``npm install -g heroku``
4. Before pushing to Heroku, use the command git remote -v and see that only github links are listed
5. Add your project to heroku with the command ``git remote add heroku project-link``. Project link can be found at your Heroku app > Settings > Heroku git URL
7. Push to heroku ``git push -u heroku master``
8. Create procfile ``echo web: python run.py > Procfile``, then ``git add -A``, ``git commit -m "Add Procfile"``, ``git push``
9. If your project uses any keys hidden on the gitignore file, go to Heroku and add them there in Settings > Config Vars

More information about deploying with Git [here](https://devcenter.heroku.com/articles/git).

### How to fork this repository

If you would like to experiment with this project without changing it, follow the steps below.

1. After logging into your GitHub account, open up [this GitHub repository](https://stefcruz.github.io/ci_milestone4/)
2. Click on the 'Fork' button at the top right-hand corner of the page
3. Start coding!

### How to open this project locally

There are two options to clone this project to your local machine, using the command line and using GitHub desktop. Both are detailed [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

#### Using the command line

1. Go to the main page of [this GitHub repository](https://github.com/stefcruz/ci_milestone4).
2. Click on 'Code'.
3. First select whether you want to clone this repo using HTTPS, SSH or CLI, then click on the clipboard icon.
4. Open Terminal on your computer or the terminal from your IDE.
5. Change the current working directory to the location where you want the directory to be cloned.
6. Type `git clone`, and then paste the URL you copied earlier.
   ```shell
   $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
   ```
7. Press Enter to create your local clone.

#### Using GitHub Desktop

1. Go to the main page of [this GitHub repository](https://github.com/stefcruz/ci_milestone4).
2. Click on 'Code'.
3. Click 'Open with GitHub Desktop'.
4. Click  'Choose...' and select the location where you want to save this repo on your machine.
5. Open the project on your favourite IDE.

More information can be found [here](https://docs.github.com/en/free-pro-team@latest/desktop/contributing-and-collaborating-using-github-desktop/cloning-a-repository-from-github-to-github-desktop).

## Credits

### Images
- [Illustrations](https://icons8.com/illustrations/style--marginalia)

## Acknowledgements

### Design
- [Bootstrap colour and design theme](https://themes.getbootstrap.com/product/start-react-bootstrap-5-admin-dashboard-theme/)

### Code
- [Fix to issue unordered object list warning](https://stackoverflow.com/questions/44033670/python-django-rest-framework-unorderedobjectlistwarning)
- [Django 3.0 crash course tutorials which helped understanding Django](https://www.youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO)
- [CSS triangle top left shape](https://css-tricks.com/the-shapes-of-css/)
