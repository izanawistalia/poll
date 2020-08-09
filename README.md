<h1 align="center">HackerVote</h1>
<h2>Introduction:</h2> HackerVote is an online voting web application.<br>
In which the guest user can vote for the best hacker among the hackers listed.<br>
Guest users are allowed to view the details of the listed hackers nd can vote for the hacker the hacker they deem best. However the guest user can only vote once.<br>
<br>
<h2>REQUIREMENTS:</h2> This project utilizes Python 3.8.2 and Django 3.0.8 at the backend and Use HTML5 and CSS3 at frontend.

<h2>WORKING:</h2> HackerVote homepage:
<img src="images/dashboard.png" alt="dashboard">
<br>
The guest user can select and hacker :
<img src="images/select_daisy.png" alt="select">
<br>
once clicked on the selected hacker, the details of the selected hacker can be seen:
<img src="images/daisy_detail.png" alt="detail">
<br>
Guest user can vote for the hacker, if they want by clicking on the vote button, provided in the detail page of the given hacker:
<img src="images/daisy_voted.png" alt="vote">
<br>
If voted once, the guest user tries to vote again for some other hacker, they won't be able to do so:
<img src="images/vote_again.png" alt="voted">
<br>
<br>
<h2>Admin:</h2> Admin can login using the login button provided, and see the following login form:
<img src="images/admin_login.png" alt="login form">
<br>
Once logged in admin sees the admin's dashboard page, where it can see all the candidate hackers, only admin can create, update or delete a particular candidate:
<img src="images/admin_dashboard.png" alt="admin dashboard">
<br>
If admin want to create a new candidate, it can click on the button provided(create candidate) and sees the following form:
<img src="images/create_candidate.png" alt="create candidate">
<img src="images/candidate_creation.png" alt="create candidate">
<br>
When admin clicks submit the following candidate will be created and the admin will be redirected to admin dashboard page:
<img src="images/candidate_created.png" alt="candidate created">
<br>
If the admin wants to update a candidate, it can do so by clicking on the update button provided for every candidate and sees the following form with candidates information already listed:
<img src="images/daisy_update.png" alt="update">
<br>
Once updated, the information of the candidate will be updated in the database and will be availabe for the guest user:
<img src="images/daisy_updated.png" alt="updated">
<br>
The admin can delete a particular candidate bu clicking on the delete button provided for every candidate and sees the following deletion confirmation page:
<img src="images/candidate_delete.png alt="delete">
<br>
If selected on cancel, the deletion process terminates and redirects the admin to admin dashboard, and if delete is clicked, the particular user is deleted and the admin is redirected to the admin dashboard:
<img src="images/candidate_deleted.png" alt="deleted">
<br>
Admin can logout by clicking on the logout button provided, and will be redirected to the login form:
<img src="images/admin_loggedOut.png" alt="logout">
<br>
