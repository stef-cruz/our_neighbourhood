# Our Neighbourhood - Test Plan

## Table of Contents

- [W3C HTML Validator](#w3c-html-validator)
- [W3C CSS Validator](#w3c-css-validator)
- [JSHint Validator](#w3c-css-validator)
- [Google Lighthouse](#Google-lighthouse)
- [User Stories Testing](#user-stories-testing)
- [Manual Testing](#manual-testing)
  - [Test plan](#test-plan)
  - [Browser and Device Testing](#browser-and-device-testing)
  - [Bugs and Fixes](#bugs-and-fixes)
    - [Browser Bugs](#browser-bugs)
    - [General Bugs](#general-bugs)

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

The app also passed the Google Lighthouse validation.

<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/google-lighthouse.png" width="500">

## PEP8 Python Validation

The python files passed the PEP8 validation on [this site](http://pep8online.com/) but the Pycharm validation has been given preference when there were discrepancies on the results.

## CircleCI

Circle CI Continuous Integration has been added to GitHub to make sure every build would be tested and deployed successfully.

<img src="https://github.com/stefcruz/ci_milestone4/blob/master/readme/circle-ci.png" width="500">

## User Stories Testing

## Manual Testing

### Test plan

#### Browser and Device Testing
#### Bugs and Fixes

*Browser Bugs*

*General Bugs*