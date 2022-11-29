Back to README
---
## User Stories Testing

### User/Customer Stories Testing
<ul>
<li><a href="#one">As a User I can register an account so that I can make a consultant request for my company.</a></li>
<li><a href="#two">As a User I can make a consultant request so that partners know what I am searching for.</a></li>
<li><a href="#three">As a User I can see all my requests in an overview so that I have control and know the status of the requests.</a></li>
<li><a href="#four">As a User I can see when a partner has presented a consultant so that I can decide if I want to schedule an interview with the consultant.</a></li>
<li><a href="#five">As a User I can see contact information for the manager so that I can schedule an interview with the manager/consultant.</a></li>
<li><a href="#fifteen">As a User I can Edit my requests so that the request displays the correct information in case of some changes are made.</a></li>
<li><a href="#sixteen">As a User I can delete my request so that partners do not spend time presenting candidates if we have already found what we are looking for.</a></li>
</ul>

### Partner Stories Testing
<ul>
<li><a href="#fourteen">As a User/Partner I can see information about the website/tool so that I understand why i should register an account.</a></li>
<li><a href="#six">As a Partner I can register an account so that I can see consultant requests from companies.</a></li>
<li><a href="#seven">As a Partner I can see the details of the request so that I can present the right consultant.</a></li>
<li><a href="#eigth">As a Partner I can present a consultant with their CV, price, and conditions so that I can show the company that we have a solution for them.</a></li>
</ul>

### Admin Stories Testing
<ul>
<li><a href="#nine">As a Admin I can view details about users and partners so that I know who uses our tool.</a></li>
<li><a href="#ten">As a Admin I can see a full list of ongoing requests so that I can contact new companies that may have these consultants.</a></li>
</ul>

## User/Customer Stories Testing

<h3 id="one">As a User I can register an account so that I can make a consultant request for my company.</h3>
Acceptance Criteria 1: I can register account with my email and own password.
Acceptance Criteria 2: I can fill in the details of my company as company name and vat number.

![signup](./readme-files/images/testing/1.png)
On the signup page the User can sign up and add their own unique email and password. They can also fill in the details of their company as company name and vat number.

<h3 id="two">As a User I can make a consultant request so that partners know what I am searching for.</h3>
Acceptance Criteria 1: The information that i can fill in is: Title, role, period, startdate, locality, duties, demands, wishes and deadline.
Acceptance Criteria 2: Startdate and deadline must be displayed with month, date, year.

![new-request](./readme-files/images/testing/2.png)
When the User make a new request they can fill in the information in acceptance criteria 1. Duties are named requirements due to clearer understanding.
Startdate and deadline is in format MM, DD, YYYY.

<h3 id="three">As a User I can see all my requests in an overview so that I have control and know the status of the requests.</h3>
Acceptance Criteria 1: When logging in i get redirected to the overview page.
Acceptance Criteria 2: In the overview i can see all my requests.
Acceptance Criteria 3: In every request i can see presented candidates.

![request-overview](./readme-files/images/testing/3.1.png)
When the user has signed in they get redirected to their overview page where they can find all their request presented in a list/collapse.
If the user click on the request, details of the request is presented and also a toggle button for candidates. When they press the candidate button, all candidates that have been presented is shown as cards for the user. If the list of presented candidates is 0, a text with "You do not have any presented candidates on this request" is shown.

![no-candidates](./readme-files/images/testing/3.2.png)

<h3 id="four">As a User I can see when a partner has presented a consultant so that I can decide if I want to schedule an interview with the consultant.</h3>
Acceptance Criteria 1: In the overview I can see how many candidates that have been presented for the specific request.
Acceptance Criteria 2: In request details I can see the presented candidate with name, price, summary, cv and offer.
Acceptance Criteria 3: I can also contact the manager by email.

![candidates](./readme-files/images/testing/4.png)
When the user click on the button "Show Candidates" the see all candidates that have been presented on that specific request. The user see Name, Price, Summary. When they click buttons for CV and Offer a new page opens and they can see the document there.
The button "Contact Manager" opens their mailclient with the managers email prefilled.

<h3 id="five">As a User I can see contact information for the manager so that I can schedule an interview with the manager/consultant.</h3>
Acceptance Criteria 1: When a candidate is presented I can contact the manager bu email for schedule an interview.

As describes above, the managers email is being prefilled in the users mailclient when clicking the button "Contact Manager".

<h3 id="fifteen">As a User I can Edit my requests so that the request displays the correct information in case of some changes are made.</h3>
Acceptance Criteria 1: On the overview I can click on changing the request.
Acceptance Criteria 2: The change are made immediately and updates my request.

![edit-button](./readme-files/images/testing/15.1.png)
In the User Overview the user can see two button for edit or deleting their request. When the user click on "Edit request", a form with the prefilled request information is displayed. There user can make changes to their request and that changes takes effect immediately.

![edit-form](./readme-files/images/testing/15.2.png)

<h3 id="sixteen">As a User I can delete my request so that partners do not spend time presenting candidates if we have already found what we are looking for.</h3>
Acceptance Criteria 1: On the overview I can click on delete the request.
Acceptance Criteria 2: The change are made immediately and deletes my request.

![edit-button](./readme-files/images/testing/15.1.png)
In the overview the user can see the delete button. When button is being clicked, the user get redirected to a confirmation template.

![delete-confirmation](./readme-files/images/testing/16.png)

## Partner Stories Testing

<h3 id="fourteen">As a User/Partner I can see information about the website/tool so that I understand why i should register an account.</h3>
Acceptance Criteria 1: When i go to the homepage I can see information about the service immediately.
Acceptance Criteria 2: The homepage is user-friendly and i understand the content and information.

![homepage](./readme-files/images/testing/14.png)
A page visitor see the application purpose immediately, and with one click they can see step-by-step how the application works. For more information about the User Experince, please see the section *Manuaö Testing*.

<h3 id="six">As a Partner I can register an account so that I can see consultant requests from companies.</h3>
Acceptance Criteria 1: Register account with my own password.
Acceptance Criteria 2: Add details of my company with company name and vat number.

![partner-account](./readme-files/images/testing/1.png)
In the signup page the partner create their account but choose Partner instead of Customer as User type. The partner fills in details with Company Name and Vat number.

<h3 id="seven">As a Partner I can see the details of the request so that I can present the right consultant.</h3>
Acceptance Criteria 1: When I click the request i can see details about what the company is asking for.

![request-details](./readme-files/images/testing/7.png)
When the partner click on the request title all details about that specific request is being displayed for the partner.

<h3 id="eight">As a Partner I can present a consultant with their CV, price, and conditions so that I can show the company that we have a solution for them.</h3>
Acceptance Criteria 1: On the request details i can choose to present a candidate.
Acceptance Criteria 2: I can upload CV and offer in pdf format.
Acceptance Criteria 3: I can fill in the price for consultant by the hour.

![request-details](./readme-files/images/testing/7.png)
When the partner see details about the request, they also see the button for present candidate.

![send-candidate](./readme-files/images/testing/8.png)
When the partner have clicked the button "send candidate", a form is displayed for them. In the form they upload cv and offer in pdf. They also present the price for hiring this consultant.

## Admin Stories Testing

<h3 id="nine">As a Admin I can view details about users and partners so that I know who uses our tool.</h3>
Acceptance Criteria 1: In adminpanel i can see a list of all registered accounts.
Acceptance Criteria 2: If i click on the account i can see if they are a user or partner.

In the adminpanel the admin can see a list of every registered user. When admin click on the user, all information about the user is displayed, also if the user is a customer or partner.
Due to sensitive information no image of the admin panel is displayed in the readme.

<h3 id="ten">As a Admin I can see a full list of ongoing requests so that I can contact new companies that may have these consultants.</h3>
Acceptance Criteria 1: In adminpanel i can see a list of every request in the database.
Acceptance Criteria 2: I can see every detail of the request including contact information.

## Manual Testing

### Navigation Bar

* All links correctly redirecting to the correct pages for visitor.
* Navbar is fully responsible on small/medium/large devices.
* Customer see correct link "Your overview" when logged in.
* Partner see correct link "Overview" when logged in.
* Why Us and Step-by-step is internal anchor links to the homepage and are not available when the user not are on the homepage, see bugs in Readme.

### Footer

* All icon links works correctly.
* All links open in a new page.
* The footer appears in the end of the page with javascript.
* Back to top button being displayed on scroll.
* Back to top button takes visitor back to top.
* Footer are not being displayed on pages when user don´t need to scroll, see bugs in Readme.

### Homepage

* All buttons works and links correctly.
* Icons are being displayed correctly.
* Images are being displayed correctly.
* Good contrast between text/images/buttons (CTA for partner signup image could be darker but struggled with overlay on that container)


## Validation

### [W3C HTML Validator](https://validator.w3.org/)
* Errors
* Warnings

### [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
* 0 Errors
* 0 Warnings

### [JSHint Javascript Validator](https://jshint.com/)
* 0 Errors
* 0 Warnings
*One undefined variable (Bootstrap) - Being used for messages*

### PEP8 Python Validator
* 0 Errors
* 0 Warnings



