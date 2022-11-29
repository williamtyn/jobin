# Portfolio Project 4 - Full-Stack Toolkit

## JobIn - Compare and find the best consultants for your company!

Finding the right consultant is more difficult than ever. That's why we've made it simple.

### This is how easy it works!
1. Simply create a request for the consultant you are looking for.
2. Our partners present the best consultants to you.
3. Compare consultants and choose the one that is best for your organization.

![Image mockup of the website in a computer, tablet and phone](./readme-files/jobin_mockup.png)

## Live Site
[Go to application](https://jobin-compare-consultants.herokuapp.com/) 

## Repository
[View repository](https://github.com/williamtyn/jobin)

---

## Catalouge
<li><a href="#target-group">Target Group</a></li>
<li><a href="#user-experince">UXD - User Experince Design</a></li>
<ul><li><a href="#storytelling">Storytelling</a></li>
<li><a href="#wireframe">Wireframe</a></li>
<ul><li><a href="w1">Homepage, Signup, Login</a></li>
<li><a href="#w2">Customer signed in</a></li>
<li><a href="#w3">Partner signed in</a></li></ul>
</ul>
<li><a href="#flowchart">Flowchart</a></li>

<li><a href="#surface-plane">The Surface Plane</a></li>
<ul><li><a href="#base">Base</a></li>
<li><a href="#homepage">Homepage</a></li>
<li><a href="#signup">Signup</a></li>
<li><a href="#login">Login</a></li>
<li><a href="#customer-overview">Customer Overview</a></li>
<ul><li><a href="#customer-new">New Request</a></li>
<li><a href="#customer-edit">Edit Request</a></li>
<li><a href="#customer-delete">Delete Request</a></li>
<li><a href="#customer-candidate">See Candidates</a></li></ul>
<ul><li><a href="#partner-overview">Partner Overview</a></li>
<li><a href="#partner-new">Send Candidate</a></ul>
</ul>
<li><a href="#partner-new">Database Design</a></ul>
<li><a href="#testing">Testing</a></li>
<li><a href="#technologies">Technologies</a></li>
<li><a href="#deployment">Deployment</a></li>
<li><a href="#credits">Credits</a></li>
<ul><li><a href="#code-issues">Issues with code</a></li>
<li><a href="#student-support">Student Support</a></li>
<li><a href="#code">Code</a></li></ul>
<li><a href="#acknowledgements">Acknowledgements</a></li></ul>

---

<h2 id="target-group">Target Group</h2>
The JobIn Applications have two target groups, customers and partners.
By focusing marketing on customers, we are confident that we will attract many partners to our application. consulting companies are always looking for new business opportunities and those opportunities are with us when customers post requests in our application

### Customers
The consultant industry have annual turnover of trillions of dollars worldwide. Companies in almost every country in the world is spending money in consulting hours, many of them with low satisfaction. jobin is an application for the thousands of companies that want to find the absolute best quality of the consultants they invest in, by comparing their options before making a decision.

### Partners
In Sweden, two new consulting companies are registered a week (statistics from 2021). There have never been so many companies fighting for the same customers. With our application, our partners can focus on their core business, hiring quality consultants, instead of having to spend time selling their services to clients. Whoever has the best consultant gets to deliver

## UXD - User Experince Design


### The story of Mats and The Factory
Mats is a hard-working manager at Svenska Industrigruppen AB.

He started his career there as a 16-year-old, then as a summer worker, and for 30 years has had various roles at the factory that refines metal for several large Swedish companies. Mats is fairly new in his role as a leader but enjoys it very much, and according to the company's latest employee surveys, he seems to be doing a really good job.

His biggest concern is when they need to hire new staff. Since it's a big decision and something that could cost the company a lot of money if it goes wrong, he feels some anxiety. The factory's production is very variable, and that makes it very difficult to plan how much staff is needed in production while it can change quickly, and in 14 days they will need five extra people to be able to produce at maximum level.

That evening, Mats remembers the nice guy who stopped by the factory a few weeks ago and picks up the business card to go to their website. He creates a user and enters the specifications for the resources he requires, then sends the request and goes to bed.

Already at lunch the next day, Mats has received two notices that there are candidates presented on the website, and he logs in. He looks at the candidates' CVs and the company's offer, the price is also reasonable for what he is looking for. He makes contact with responsible managers and books them in for an interview at the factory. 

Over the course of a few days, he receives more candidates on the website, and he chooses to meet a few more. Within 14 days, Mats has managed to find five consultants who enable the factory to deliver at the highest possible capacity. 
Mats is satisfied.

## User Stories

* As a User I can register an account so that I can make a consultant request for my company.
* As a User I can make a consultant request so that partners know what I am searching for.
* As a User I can see all my requests in an overview so that I have control and know the status of the requests.
* As a User I can see when a partner has presented a consultant so that I can decide if I want to schedule an interview with the consultant.
* As a User I can see contact information for the manager so that I can schedule an interview with the manager/consultant.
* As a User I can Edit my requests so that the request displays the correct information in case of some changes are made.
* As a User I can delete my request so that partners do not spend time presenting candidates if we have already found what we are looking for.


* As a User/Partner I can see information about the website/tool so that I understand why i should register an account.
* As a Partner I can register an account so that I can see consultant requests from companies.
* As a Partner I can see the details of the request so that I can present the right consultant.
* As a Partner I can present a consultant with their CV, price, and conditions so that I can show the company that we have a solution for them.


* As a Admin I can view details about users and partners so that I know who uses our tool.
* As a Admin I can see a full list of ongoing requests so that I can contact new companies that may have these consultants.

---

## Wireframe

![frontpage](./readme-files/images/wireframe/frontpage.png)
![frontpage#2](./readme-files/images/wireframe/frontpage2.png)

![register account](./readme-files/images/wireframe/register_account.png)
![login](./readme-files/images/wireframe/login.png)

### User loged in
![user overview](./readme-files/images/wireframe/user_overview.png)
![user request details](./readme-files/images/wireframe/user_request_details.png)
![user presented candidates](./readme-files/images/wireframe/user_presented_candidates.png)

### Partner loged in
![partner overview](./readme-files/images/wireframe/partner_overview.png)
![partner request details](./readme-files/images/wireframe/partner_request_details.png)


<h2 id="flowchart">Flowchart</h2> 
For a better understand how the flow of both a customer and partner should look, i´ve made a flowchart to describe the flow of a user from that they are visiting the application to that they have made the first request or send their first candidate.

![flowchart](./readme-files/workflow.png)

---

## The Surface Plane

### Base
To make the application as dynamic as possible i want the navbar and footer to be the same in all of the application. Therefore Django dynamic pages is used so the user always recognise the default layout there on.

Navbar
![navbar](./readme-files/images/surface/navbar.png)

Footer
![footer](./readme-files/images/surface/footer.png)

### Homepage
A big goal is to highlight the advantages as early as possible so the user gets sold on why the should register and use our application. Two call to action is being displayed in the hero image to encurage the user to do something, either sign up or read more.

The three biggest advantages of using our service is being displayed under the hero image. On desktop the user get a hint about them and gets curious to read more.

![hero](./readme-files/images/surface/hero.png)

When the user scrolls down they can see some more advantages in combination with a sneakpeak how the application looks on a laptop. Also here we have a call to action to encourage the user to do something.

![mockup and cta](./readme-files/images/surface/text-with-button.png)

So far we have focused on the user (Customer) and thats because the main market must be to the customer to do requests in the application. We know that if we fills the database with a lot of request, the partner will come to us to find new business opportunities.

![partner cta](./readme-files/images/surface/partner-cta.png)

After that we focus on the partner on the homepage and display a Call-to-action for the partner to register a account.

![step-by-step](./readme-files/images/surface/step-by-step.png)

The Step-by-step explains in details how the applications works and we want to show that to attract the user who want to understand more before making a decision. 

![quote](./readme-files/images/surface/quote.png)

and as a last intention to get the user to signup we display a quote “If you always do what you've always done, you'll always get what you've always got.”.
Just to get the user to think in a different approach and signup to our application. We display a back-to-top button so the user don´t have to scroll up to register.

### Signup
The user are using the same signup page and choose type of account, customer or partner, due to which type of account they will use.

![signup](./readme-files/images/surface/signup.png)

### Login
Its easy to login for returning user. Just fill in your username and password and you get logged in.

![login](./readme-files/images/surface/login.png)

### Customer Overview
When user have signed up or loged in as a customer the get redirected to the user/overview page. On this page they can find a call to action to make a new request. This is also the main page for the customer where they can see all their requests and also candidates on every request.

![user-overview](./readme-files/images/surface/user-overview.png)

![request-details](./readme-files/images/surface/request-details.png)


### New Request
When the user click on the button to make a new request they get redirected to a form to fill in the details about the request.

![new-request](./readme-files/images/surface/new-request.png)

### Edit request
From the overview the user can see the request and click on edit request if they need to make some changes on the request.

![buttons](./readme-files/images/surface/buttons.png)

![edit-request](./readme-files/images/surface/edit-request.png)


### Delete Request
On the overview the customer also can choose to delete the request.

![buttons](./readme-files/images/surface/buttons.png)

![delete-request](./readme-files/images/surface/delete-request.png)


### Partner Overview
When the partner have signup or loged in the get redirected to the main request overview where they can see all request thats being active. If they click on the request they can see details about that specific request.

![partner overview](./readme-files/images/surface/partner-overview.png)

![overview details](./readme-files/images/surface/overview-details.png)


### Send Candidate
The partner can see information about the request and when they have a candidate that suits the request they can present the candidate for the customer.

![present-candidate](./readme-files/images/surface/present-candidate.png)

### See Candidates
When the customer have presented the candidate the user can see that candidate presented on their request. Compare with all the cnadidates thats being presented and choose which one suits their need the best. IF they want to schedule an interview they can contact the manager by email.

![see-candidate](./readme-files/images/surface/see-candidates.png)

---

## Database Design
On this project PostGresql is used with ElephantSQL

(link to Database Diagram)
[Database Diagram](https://res.cloudinary.com/dpliee0fu/image/upload/v1669761371/Database_Planning_gzhnzg.pdf)


### Key Models

### User

* The user profile is connected to the User model created by Allauth on registration.
* The model is extended with AbstractUser to be able to save different user types with different permissions.
* Primary Key is the id which being genereated automatic when user is created.

### Order

* The order model is related to user model to see who is responsible for the order.
* If the user is deleted, the order also get deleted so no orders is active for users that don´t exists.

### Candidate

* Candidates are related to their managers (Users) who "create" the candidate.
* Candidates are also related to Order on which managers present the candidate and links them together.
* Being linked to the order the user can also get access to the Candidate information via the template.

---

## Testing
Link to the testing document.
[TESTING.md](https://github.com/williamtyn/jobin/blob/main/TESTING.md)

---

## Deployment

---

### Technologies Used
* [HTML](https://sv.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/CSS)
* [Javascript](https://www.javascript.com/)
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [ElephantSQL](https://www.elephantsql.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Heroku](https://id.heroku.com/login)
* [Cloudinary](https://cloudinary.com/)
* [Github](https://github.com/)
* [Gitpod](https://www.gitpod.io/)
* [Balsamiq](https://balsamiq.com/)
* [SimpleImageResizer](https://www.simpleimageresizer.com/)
* [Pagespeed](https://pagespeed.web.dev/)
* [Miniwebtool](https://miniwebtool.com/django-secret-key-generator/)
* [Techsini](https://techsini.com/multi-mockup/index.php)
* [Pexels](https://www.pexels.com)

### Credits

#### Code
* To help me start with the project and understan the basics i followed [Code Institute](https://codeinstitute.net/se/) and Matt´s Walktrough on "I Think therefore i Blog", big thanks for getting me started.

* Ed, Ger and Oisin, Tutors at [Code Institute](https://codeinstitute.net/se/) helped me solve some bugs in my code, big thanks.

#### Bootstrap
* Bootstrap have a amazing library and have helped me focus on the backend and save a lot of time with style, and layout on the frontend.

#### Django
* The generic views from [Django](https://www.djangoproject.com/) made my life much easier, also great documentation.

#### Issues with code
Most of the daily problems were solved thanks to [Stackoverflow](https://stackoverflow.com/) and [W3Schools](https://www.w3schools.com/).

#### Images

### Acknowledgements
This website was completed as a Portfolio Project 4 for the Fullstack Diploma at [Code Institute](https://codeinstitute.net/se/). I want to thank my friend *Manne* for helping me understand some with javascript functions.

The project is for educational purposes only and not for public consumption.

William Tynér, November 2022.
[LinkedIn](https://www.linkedin.com/in/williamtyner/)



