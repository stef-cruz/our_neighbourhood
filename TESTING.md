# Our Neighbourhood - Test Plan

## Table of Contents

- [W3C HTML Validator](#w3c-html-validator)
- [W3C CSS Validator](#w3c-css-validator)
- [JSHint Validator](#w3c-css-validator)
- [Google Lighthouse](#Google-lighthouse)
- [PEP8 Python Validation](#pep8-python-validation)
- [Circle CI](#circle-ci)
- [Test Plan](#test-plan)
  - [Test Cases](#test-plan)
  - [Bugs and Fixes](#bugs-and-fixes)
    - [Bugs fixed](#bugs-fixed)
    - [Bugs not fixed](#bugs-not-fixed)

## W3C HTML Validator

All HTML pages passed the W3C HTML validation as below.

Pages tested:

  - https://ci-milestone4.herokuapp.com/  
No errors  
  - https://ci-milestone4.herokuapp.com/accounts/login & https://ci-milestone4.herokuapp.com/accounts/signup    

Warning related to the JS type attribute which comes from the allauth library not my code.   
<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/html-validation-login.png" width="300">

  - https://ci-milestone4.herokuapp.com/contact  
No errors 
  - https://ci-milestone4.herokuapp.com/faq  
No errors 
  - https://ci-milestone4.herokuapp.com/events  
No errors 

## W3C CSS Validator

No errors found on the CSS file.

<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/css-validator.png" width="400">

## JSHint

No major issues on the JS files either.  

<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/jshint.png" width="400">

## Google Lighthouse

Initially the website scored 84 in performance due to invisible text. Then the issue was resolved by adding the CSS to avoid displaying invisible text while the custom font loads.  

`@font-face {`  
  `font-family: 'Pacifico';`  
  `font-style: normal;`  
  `font-weight: 400;`  
  `src: local('Pacifico Regular'), local('Pacifico-Regular'), url(https://fonts.gstatic.com/s/pacifico/v12/FwZY7-Qmy14u9lezJ-6H6MmBp0u-.woff2) format('woff2');`   
  `font-display: swap;`  
`}`

<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/google-lighthouse.png" width="600">

## PEP8 Python Validation

The python files passed the PEP8 validation on [this site](http://pep8online.com/) but the Pycharm validation has been given preference when there were discrepancies on the results.

## CircleCI

Circle CI Continuous Integration has been added to GitHub to make sure every build would be tested and deployed successfully.

<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/circle-ci.png" width="500">

## Test Plan

The manual test plan was broken down by app, with all the functionalities covered on the plan as well as the responsivess of the site and browser compatibility. [Click here](https://docs.google.com/spreadsheets/d/19ua4CjXbZuQSyllOOhlNmxxijfMEXFa0lw85VEvL4vE/edit#gid=0) to see test plan spreadsheet.

Unfortunately, unit tests could not be completed in time for the submission of this project. 

![Test Plan Overview](https://github.com/stefcruz/ci_milestone4/blob/master/readme/test-plan-overview.png)

### Test cases

![Test Cases 1](https://github.com/stefcruz/ci_milestone4/blob/master/readme/test-cases-1.png)  
![Test Cases 2](https://github.com/stefcruz/ci_milestone4/blob/master/readme/test-cases-2.png)  
![Test Cases 3](https://github.com/stefcruz/ci_milestone4/blob/master/readme/test-cases-3.png)  
![Test Cases 4](https://github.com/stefcruz/ci_milestone4/blob/master/readme/test-cases-4.png)  
![Test Cases 5](https://github.com/stefcruz/ci_milestone4/blob/master/readme/test-cases-5.png)  
![Test Cases 6](https://github.com/stefcruz/ci_milestone4/blob/master/readme/test-cases-6.png)  
![Test Cases 7](https://github.com/stefcruz/ci_milestone4/blob/master/readme/test-cases-7.png)  
![Test Cases 8](https://github.com/stefcruz/ci_milestone4/blob/master/readme/test-cases-8.png)    
![Test Cases 9](https://github.com/stefcruz/ci_milestone4/blob/master/readme/test-cases-9.png)    
![Test Cases 10](https://github.com/stefcruz/ci_milestone4/blob/master/readme/test-cases-10.png)    

### Bugs and Fixes

#### Bugs fixed

- T09 Test ID 4  
Error message was not meaningful for the user as to why the form was not submitting, so it was changed to "please ensure form is valid".

 
- T18 Test ID 7  
Checkout success view was sending email even when the page threw the error 500. This was fixed by checking if the event_session is in the session, then the email can be sent. 
  
`if request.session.get('event_session'):`  
`msg.send()`
 
- T21 Test IDs 3 to 6  
Initially this functionality of throwing an error message if the contact or event had already been marked as resolved/paid didn't exist. During testing I felt the need to add so the admin has a visual cue of what is happening on the page. So if the contact request is already marked as resolved and the user clicks "mark contact as resolved", the toast will say "contact has been resolved already".
  
 
- T22 Test ID 2  
There was an issue with the Stripe card div that when the user typed the card number, it would overlap the expiry date and CVV. This was fixed by removing the Stripe form from the bootstrap row and col.  

<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/test-stripe-issue.png" width="500">


#### Bugs not fixed

- T23 Test ID 5  
Button update profile is not greyed out as per design. When the user lands on the page, the button is disabled but with the regular colours. When user adds text, then the cursor is enabled and the user can click.