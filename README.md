# Portfolio Project 4 - Fullstack Full-Stack Toolkit

## JObIn - Compare and find the best consultants for your company!

Finding the right consultant is more difficult than ever. That's why we've made it simple.

### This is how easily it works!
1. Simply create a request for the consultant you are looking for.
2. Our partners present the best consultants to you.
3. Compare consultants and choose the one that is best for your organization.

![Image mockup of the website in a computer, tablet and phone](image goes here)

## Live Site
[Go to site](www.website.com) 

## Repository
[View repository](www.website.com)

---

## Catalouge
<li><a href="#target-group">Target Group</a></li>
<li><a href="#user-experince">UXD - User Experince Design</a></li>
<ul><li><a href="#storytelling">Storytelling</a></li>
<li><a href="#wireframe">Wireframe</a></li>
<ul><li><a href="w1">Homepage, Sign up, Log in</a></li>
<li><a href="#w2">Customer signed in</a></li>
<li><a href="#w3">Partner signed in</a></li></ul>
</ul>
<li><a href="#flowchart">Flowchart</a></li>
<li><a href="#user-stories">User Stories</a></li>

<li><a href="#rules">The Surface Plane</a></li>
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
<li><a href="#bugs">Bugs</a></li>
<ul><li><a href="#solved-bugs">Solved Bugs</a></li></ul>
<li><a href="#future-features">Future features</a></li>
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

<h2 id="flowchart">Flowchart</h2> 

## The story of Mats and The Factory
Mats is a hard-working manager at Svenska Industrigruppen AB.

He started his career there as a 16-year-old, then as a summer worker, and for 30 years has had various roles at the factory that refines metal for several large Swedish companies. Mats is fairly new in his role as a leader but enjoys it very much, and according to the company's latest employee surveys, he seems to be doing a really good job.

His biggest concern is when they need to hire new staff. Since it's a big decision and something that could cost the company a lot of money if it goes wrong, he feels some anxiety. The factory's production is very variable, and that makes it very difficult to plan how much staff is needed in production while it can change quickly, and in 14 days they will need five extra people to be able to produce at maximum level.

That evening, Mats remembers the nice guy who stopped by the factory a few weeks ago and picks up the business card to go to their website. He creates a user and enters the specifications for the resources he requires, then sends the request and goes to bed.

Already at lunch the next day, Mats has received two notices that there are candidates presented on the website, and he logs in. He looks at the candidates' CVs and the company's offer, the price is also reasonable for what he is looking for. He makes contact with responsible managers and books them in for an interview at the factory. 

Over the course of a few days, he receives more candidates on the website, and he chooses to meet a few more. Within 14 days, Mats has managed to find five consultants who enable the factory to deliver at the highest possible capacity. 
Mats is satisfied.

## Wireframe

![frontpage](../jobin/readme-files/images/wireframe/frontpage.png)
![frontpage#2](../jobin/readme-files/images/wireframe/frontpage2.png)

![register account](../jobin/readme-files/images/wireframe/register_account.png)
![login](../jobin/readme-files/images/wireframe/login.png)

### User loged in
![user overview](../jobin/readme-files/images/wireframe/user_overview.png)
![user request details](../jobin/readme-files/images/wireframe/user_request_details.png)
![user presented candidates](../jobin/readme-files/images/wireframe/user_presented_candidates.png)

### Partner loged in
![partner overview](../jobin/readme-files/images/wireframe/partner_overview.png)
![partner request details](../jobin/readme-files/images/wireframe/partner_request_details.png)

### Workflow
![workflow](../jobin/readme-files/workflow.png)

### Database schema
#### Order
![database](../jobin/readme-files/order_database_schema.png)


### Bugs
* Rediricting to right page when user have logged in
* Login confirmation message do not dissapear when user have been logged in after signing up.
* Internal navbar links (Why Us and Step-by-step) is not accessable when user have logged in.

#### Resolved Bugs
* Toggle collapse inside a for loop in template
* Navbar links on mobile
* Redirect logedin user based on user type
* Change of toggler color icon for Bootstrap navbar
I struggled a lot with changing color of the toggler icon inte the navbar. Then i found [This](https://www.folkstalk.com/2022/09/bootstrap-navbar-toggler-icon-color-with-code-examples.html) and understod that I needed to change the url for the icon.


### Technologies Used
https://www.simpleimageresizer.com/ - For making images smaller
https://pagespeed.web.dev/ - For checking Pagespeed Insights
https://miniwebtool.com/django-secret-key-generator/ - For generating Django secret key
https://cloudinary.com/ - For cloudstoring of pdf that is being saved to the database

### Sources
#### Images
[Homepage Partner]https://www.pexels.com/sv-se/foto/manniskor-barbar-dator-sitter-mote-4340139/
