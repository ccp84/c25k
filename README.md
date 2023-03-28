# MJ's c25k Registration App

## Concept 

This Django app will be a runner registration tool for c25k groups. Currently, leaders have to rely on Whatsapp group chats to know if the participants are attending each session or not and can be left waiting around for runners they think are due to attend who either haven't posted in the chat group that they aren't coming, have said they are unable to come but the leaders have missed the message, or have previously said they were coming and changed their mind but not notified the leader. Similarly, participants who are running late but who the leader doesn't know to wait for may find that the group has already left the start point if they miss the start time. This project aims to fix that as its core aim.

## Project Scope

* It will allow run leaders to advertise the details of each week's date, time and start location. As well as giving any additional details such as parking facilities, if trail shoes are needed, or other key information to be relayed before the start.
* It will allow site visitors to view a basic list of the planned activities, and register for a user account to gain access to further detail.
* It will allow logged-in runners to see all of the details the leader has posted about the run.
* It should allow logged-in runners to sign up and state that they are planning on attending a run / remove their name from the list if they change their minds. 
* It should allow leaders to view a list of runners who are planning to attend each session. 
* It should allow registered users to view and edit their details. 
* The overall site should have a main colour theme on completion and function with a mobile-first design in mind.
* It could be used to mark runners as completed to maintain a list of graduates within the database, and list graduate runs following on from the main course. 
* It could be used for runners to add an emergency contact to their account which run leaders will be able to access during sessions in case of an incident during the run.  
* It could allow leaders to manage the user status of registered accounts to update the list of leaders rather than having to log into the admin panel. 
* It could enable the club to advertise details of the next course and allow runners to sign up in readiness for the start date. 

Using MoSCoW prioritisation these functions have been prioritised as 'must have', 'should have', 'could have' and have been turned into user stories to create the [project board](https://github.com/users/ccp84/projects/4/views/1?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%5D). Any remaining features outside of this project's timeframe will be moved to 'won't have', and in production would become part of the next release or future features.

## Table of Contents:
1. [Wireframes](#wireframes)
2. [Data Model](#data-model)
3. [Project Development](#project-development)
  1. [Review Point 1](#review-point-1)
  2. [Review Point 2](#review-point-2)
  3. [Review Point 3](#review-point-3)
  4. [Review Point 4](#review-point-4)
4. [Future Features](#future-features)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Technologies Used](#technologies-used)
8. [Credits](#credits)

## Wireframes
* Welcome Page Views
![Welcome Page Views](/documentation/welcome_page.png)

* Run Details Page Views
![Run List Page Views](/documentation/run_list.png)

## Data Model

![Entity Relationship Diagram](/documentation/ERD.png)

## Project Development

## REVIEW POINT 1
|At this initial review point. I have prioritised the 'must have' user stories:| ![project_review_1](documentation/project_review_1.png) |
| ----------------------------------- | ----------------------------------------- |
| 1. Landing page | 
| 2. Display a run list |
| 3. Add, edit, delete runs|
| 4. User Authentication | 

### Run List 
This feature has been developed using the Django generic CBV 'ListView':
```python
class RunList(ListView):
    model = Run
    template = 'run_list.html'
```
With a custom HTML template to display the correct elements to each user depending on their authentication status:
```python
{% if user.is_authenticated %}
# List of current runs is displayed for the user
    {% if request.user.groups.all.0.name == 'leader' %}
    # Leader can edit and delete the listed run, as well as a button to add a new run
{% else %}
# A message is displayed inviting the user to log in, although the page is only shown in the nav bar for authenticated users
```
This page hosts the main functionality of the project allowing only authenticated users to see the full details of each run, as opposed to the basic list on the welcome page. Users tagged with the group of leader can also access links to edit and delete runs from the list here, as well as have access to the link to add a new run. 

### Create Run
This feature is only accessible by authenticated users who have a group tag of leader
```html
{% if request.user.groups.all.0.name == 'leader' %}
    <!-- Restrict form to users authenticated as leaders -->
{% else %}
    <!-- Message displayed here informs users they need leader status for this page -->
```
It makes use of the Django generic CBV 'CreateView' with the LoginRequiredMixin for additional page security and the SuccessMessageMixin to return a note to the user informing them that their action has been carried out on form submission:
```python
class RunCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Run
    template_name = 'run_create.html'
    fields = ["title", "leader", "location", "date", "time", "details"]
    success_url = '/run/list'
    success_message = "Run created"
``` 
and the standard form for this view, which will be styled in a later part of the project:

![run_create_form](documentation/run_create_form.png)

### Edit Run
This feature is very similar to the creation of a new run, and can only be accessed by authenticated users who are leaders. It uses the generic Django 'UpdateView':
```python
class RunUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Run
    template_name = 'run_update.html'
    fields = ["title", "leader", "location", "date", "time", "details"]
    success_url = '/run/list'
    success_message = "Run updated"
```
and again imports the standard form as well. However, the URL associated with this view expects the primary key of the run as an identifier to ensure the correct entry in the database is being updated:
```python
path("run/update/<pk>", views.RunUpdate.as_view(), name='run_update')
```
This is passed in from the HTML template via the anchor tag:
```html
<td><a href="{% url 'run_update' run.id %}">Edit</a></td>
```
The result is not only that the correct database record is updated, but also that the rendered form is pre-populated for editing:

![run_edit_form](documentation/run_edit_form.png)

### Delete Run
Working in an almost identical way to editing, deleting makes use of the generic 'DeleteView' in views:
```python
class RunDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Run
    template_name = 'run_delete.html'
    success_url = '/run/list'
    success_message = "Run deleted"
```
No fields are included this time as all the template needs is an input to delete the entire record. I have updated the standard template to include a link "back to safety" in case of accidental clicking. 
The record to be deleted is identified by passing the primary key into the URL the same as when editing:
```python
path("run/delete/<pk>", views.RunDelete.as_view(), name='run_delete')
```
```html
<td><a href="{% url 'run_delete' run.id %}">Delete</a></td>
```

![run_delete_form](documentation/run_delete_form.png)

### Logging in / out

For user authentication I have used the allauth library, implementing the techniques used in the Code Institute walkthrough project. 
Once installed, and the allauth URLs imported into the project URLs.py document, log-in / log-out is handled by the standard templates. To tidy these up and get them sitting within my main project base template I copied the allauth templates into my project and edited the `{% extends '' %}` line at the top of each of the default files. 

![login_page](documentation/login.png)

### Signup

Signing up for an account also uses allauth, however, I have modified the standard allauth template so that the user is forced to complete a first name and last name (which are standard in the allauth library just not included in the standard signup process.)

The code added to forms.py to achieve this is :
```python
class SignupForm(forms.Form):
    first_name = forms.CharField(
        max_length=30, label='First Name', required=True)
    last_name = forms.CharField(
        max_length=30, label='Last Name', required=True)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
```
For my project, a first and last name are required when signing up for runs so the leader knows who is attending. It made more sense to use the built-in allauth fields than to include these in the separate Profile model. The code to implement this was found following [this thread](https://stackoverflow.com/questions/12303478/how-to-customize-user-profile-when-using-django-allauth) on stack overflow.

![sign up](documentation/sign_up.png)

## REVIEW POINT 2
| At this point, I have completed all project 'must have' criteria and moved those user stories to complete. Looking at the next stage of project features, I will prioritise the 'should have' user stories as follows:| ![review_point_2](documentation/project_review_2.png) |
| -------------------------------------------- | ------------------------------------- |
| 1. Adding the ability for a user to sign up for a run |
| 2. Adding a feature for the run leader to see a register/list of signed-up runners |
| 3. Allowing users to update their profile information |
| 4. Applying styling for an overall site theme |


### Displaying system messages

I have included Django messages to be displayed at the top of my base template so that the user is notified when they have successfully performed actions that trigger a system message. 
```html
{% if messages %}
    <div>
      <strong>Messages:</strong>
      <ul>
        {% for message in messages %}
        <li>{{message}}</li>
        {% endfor %}
      </ul>
    </div>
{% endif %}
```
This sits above the content block so that they are visible no matter which page a user is on when messages are available. 

![django_messages](documentation/messages.png)

### Runner sign up
Signing up for runs is achieved in 2 parts. 

#### Step 1: The runner clicks "Count me in / out" 
This uses a new view called `run_join` which queries the `run.runners` field of the Run database filtering by `user.id`. If that user is not found within the returned queryset, then the user's id is added to the list, else if the user is already contained within the results then they are removed. The view returns to the `run_list` page once it has completed its function. 
```python
def run_join(request, pk):
    run = get_object_or_404(Run, id=pk)

    if run.runners.filter(id=request.user.id).exists():
        run.runners.remove(request.user)
    else:
        run.runners.add(request.user)

    return HttpResponseRedirect(reverse('run_list'))
```

#### Step 2: Displaying to the user if they are currently signed up or not
An additional database method was needed to achieve this. 
```python
def signed_up(self):
        name_list = [] # initialise an empty list
        runner_list = self.runners.all() # return all runner objects linked to that run object
        for runner in runner_list: # loop the list of runners
            name_list.append(runner.id) # append the id of each runner in the list to the empty list initialised at the start
        return name_list # return this list to be used when the signed_up field of a run is called
```
A list `runner_list` is populated from running a query to retrieve all currently linked users on the many:many `run.runners` field. Then to return useable data to the Django template, this list is iterated and the user id field for each object contained in the link is pushed into a blank list `name_list`. This is then returned by the method and is ready for use when called in the template.
```html
{% if user.id in run.signed_up %}
                <button type="submit" name="run_id" value="{{run.id}}">
                    <i style="color: greenyellow;" class="fas fa-running">In</i>
                </button>
                {% else %}
                <button type="submit" name="run_id" value="{{run.id}}">
                    <i style="color: red;" class="fas fa-running">Out</i>
                </button>
{% endif %}
```
The returned list is checked for the currently logged-in user id. If found, a green 'already in' version of the 'Count me in' button is displayed. Otherwise, a red button is displayed to indicate that they have not signed up for that session. PLEASE NOTE: The in-line styling will be removed when custom CSS is added to the project later, however, to get this feature to work this is the quickest way to test functionality for now. 

![count_me_in](documentation/count_me_in.png)

### Viewing a run register
Leaders can see a list of runners signed up for each run in the leader-only view of the run list page. A function returns a list of names from the Run table:
```python
def take_register(self):
    register = [] # initialise empty list
    runner_list = self.runners.all() # get all runner objects linked by the foreign key
    for runner in runner_list: # loop each object returned
        register.append([runner.first_name, runner.last_name]) # append the first_name and last_name fields of the runner object to the empty list
    return register # return this new list when the take_register property of a run is called
```
This function is then used to produce a list of names linked to each run:
```html
<ul>
    {% for runner in run.take_register %}
        <li>{{ runner.0 }} {{ runner.1 }}</li>
    {% endfor %}
</ul>
```
![runner_list](documentation/runner_list.png)

### Creating a user profile
The user profile page checks for existing details in a retrieved user profile, if the returned profile is empty then the create profile link is displayed. 
```html
 {% empty %}
<div class="row">
    <div class="col-12">
        <a href="{% url 'profile_create' %}"><button type="button" class="btn btn-secondary">Create Your
                Profile</button></a>
    </div>
</div>
```
This view uses the generic create view, and rather than displaying user as a field, adds the currently logged-in user when the form is returned to create the foreign key link between Profile and User tables.
```python
class ProfileCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Profile
    template_name = 'profile_create.html'
    fields = ['DOB', 'ICE', 'medical']
    success_url = '/profile'
    success_message = "Profile Updated"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
```
![profile_create](documentation/profile_create.png)

### Viewing a user profile
Once a user has created a profile, the profile page displays their user details to them. The Profile table is filtered with the currently logged-in users id and the relevant instance returned as context for display. 
```python
class ProfileView(LoginRequiredMixin, View):

    def get(self, request):
        profile = Profile.objects.filter(user__id=request.user.id)

        return render(request, 'profile.html', {'profile': profile})
```
![profile view](documentation/profile_view.png)

### Updating a user profile
Users have the option to update their details, updating uses the generic Update view. Instead of relying on the primary key passed through in the URL to populate the form for updating, however, I have used a queryset which takes the currently logged-in user id to return that users details. This means that even if you were to change the URL manually you would be unable to view another runner's profile page. 
```python
class ProfileUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'profile_update.html'
    fields = ['DOB', 'ICE', 'medical']
    success_url = '/profile'
    success_message = 'Profile Updated'

    def get_queryset(self):
        query_set = Profile.objects.filter(user=self.request.user)
        return query_set
```
As you can see here, the id is 20 when followed although this isn't what is returning the data into the form. But currently, all is working:

![profile_edit_ok](documentation/profile_edit_success.png)

If I change the URL manually to try and access another user's data, I will get an error and not be allowed to view this page:

![profile_edit_error](documentation/profile_edit_error.png)

### Deleting a user profile
Users also have the option to completely delete the additional information held about them. As there is no need for a form to be populated for this, the page simply gives a warning with a button to either action the deletion or return to safety. The same checking is in place for this function with a queryset used to ensure that the user can only delete their own profile and not try to access a different user profile by manually changing the URL. 
```python
class ProfileDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'profile_delete.html'
    success_url = '/profile'
    success_message = "Profile Deleted"

    def get_queryset(self):
        query_set = Profile.objects.filter(user=self.request.user)
        return query_set
```
![profile delete](documentation/profile_delete.png)

## REVIEW POINT 3
|Now that all of the critical user functionality is working, all that remains to work through are the 'could have' points on the project board. I have prioritised these as follows. :| ![review_point_3](documentation/project_review_3.png) |
| -------------------------------------------- | ------------------------------------- |
| 1. Allowing users to add their ICE details to their profile |
| 2. Allowing leaders to view runners' details |
| 3. Allowing leaders to update user account types from the front end |
| 4. Allowing leaders to graduate runners once they have completed the course |

### Allowing users to add ICE details to their profile
This user story was not necessary upon reflection and was covered in the 'Updating a user profile' step. So was automatically moved to completed.

### Viewing runner details from the run list page
This is achieved by developing a similar view to the User Profile view with a few minor alterations to allow an authorised leader to view details that do not belong to them. 
```python
class RunnerProfile(LoginRequiredMixin, View):

    def get(self, request, id):
        runner = Profile.objects.filter(user__id=id)
        is_leader = User.objects.filter(
            groups__name='leader', id=id)
        context = {
            "runner": runner,
            "is_leader": is_leader,
        }

        return render(request, 'runner_profile.html', context)
```
The view uses an id passed in from the runner details that are clicked on from the register to query the Profile table and return the record associated with that id, rather than the currently logged-in user which would be the leader. This displays the relevant runners' profile if they have set one up and allows the leader to see their ICE and medical information if they have chosen to provide it. 

![runner_profile](documentation/runner_profile.png)

### Allow leaders to update user account types
Leader account types have been implemented using a leader group in Postgres. To avoid new leader accounts having to be made via the admin panel a leader tools page was created that gives an overview of all user accounts registered to the system. 
```python
class UserList(LoginRequiredMixin, ListView):

    def get(self, request):
        user_list = User.objects.all().order_by('last_name')
        is_leader = User.objects.filter(
            groups__name='leader')
        leader_ids = []
        for leader in is_leader:
            leader_ids.append(leader.id)
        context = {
            "user_list": user_list,
            "is_leader": is_leader,
            "leader_ids": leader_ids
        }
        return render(request, 'user_list.html', context)
```
The generic ListView returns all objects from the User model, as well as some extra filtering being done to determine whether each user is a member of the 'leader' group to allow the page to provide functionality for toggling account types. It is also used to highlight in the list which are the already designated leaders for easier viewing. 

![user_list](documentation/user_list.png)

All authorised leaders have access to be able to add any user account to the leaders group, access to this page is granted through authentication checking both on the nav bar:
```html
{% if request.user.groups.all.0.name == 'leader' %}
<li class="nav-item">
	<a class="nav-link" href="{% url 'user_list' %}">Leader Tools</a>
</li>
{% endif %}
```
And via the same if statement checking before displaying any page content. 

For safety though, leader accounts can only add users to this group they cannot remove other users' access rights. 
```python
def make_leader(request, id):

    runner = get_object_or_404(User, id=id)
    leaders_group = Group.objects.get(name='leader')
    runner.groups.add(leaders_group)
    messages.add_message(
        request,
        messages.INFO,
        f"{runner.first_name} was added to the leaders group.")

    return HttpResponseRedirect(reverse('user_list'))
```

This function takes in the id of the user that was clicked on from the URL and uses it to filter the User table. The returned User object then has the group 'leader' added to its list of groups. The filtering to fetch groups was researched using [this thread](https://stackoverflow.com/questions/6288661/adding-a-user-to-a-group-in-django) on stack overflow. 

![make_leader](documentation/make_leader.png)

Logged-in superuser accounts can remove users from the leaders group. The function to do this is identical to adding with the change of 1 line from `runner.groups.add(leaders_group)` to `runner.groups.remove(leaders_group)`. The authentication checking for this ability is done in the Django template. 
```html
{% if request.user.is_superuser %}
<li class="btn btn-danger">
    <a href="{% url 'remove_leader' user.id %}" class="text-white">Remove Leader</a>
</li>
{% endif %}
```

![remove_leader](documentation/remove_leader.png)

## REVIEW POINT 4
|At the final review point of the project. Both documentation points remain to be finished and I have moved the last feature to won't have. | ![review_point_4](documentation/project_review_4.png) |
| ----------------------------------- | ----------------------------------------------------  |
|                                     |                                                       |


## Future Features

* Adding a 'completed' flag to runners' profiles which can be toggled by a group leader once they have completed the course. This will allow for a database of course alumni. 
* Adding run categories so that new course participants can follow the structure of the next 9-week course, whilst graduates could have progression runs available to them for further onward support.
* Further separating the functionality for a whole club approach to incorporate half/marathon training, Sunday Long Run group, cross country team, etc to all have their own filters. 
* The ability for leaders to add messages onto the front screen of the app in case of run cancellations so that runners could check for updates before setting out to a training session that may no longer be running, or may have changed location. 
* Auto delete of past runs so that anything before 'today' does not appear on the system. 

## Testing

Link to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://c25kapp.herokuapp.com).

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:
- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: c25k).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.
- For *Primary interest*, you can choose *Programmable Media for image and video API*.
- Optional: *edit your assigned cloud name to something more memorable*.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | user's own value |

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:
- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/ccp84/c25k) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/ccp84/c25k.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ccp84/c25k)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/ccp84/c25k)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Technologies Used

This project is built using the following languages and frameworks:
* HTML
* CSS
* Python 
* Bootstrap
* Django

I have used tools to assist me as a developer:
* Git - Version control and project flow management
* [GitHub](https://github.com/) - Cloud hosting of project files
* [Heroku](https://www.heroku.com/home) - Cloud hosting of deployed project
* [Cloudinary](https://cloudinary.com/) - Cloud storage for static files
* SQlite - Development and testing SQL server
* [Elephant Sql](https://www.elephantsql.com/) - Live hosted Postgresql project database
* [Lucid](https://lucid.app/) - Used to create ERD
* Balsamiq - Used to create wireframes
* paint.net - Used for image manipulation
* [Font Awesome](https://fontawesome.com/) - Icons used throughout the project
* [Font Awesome Favicon Builder](https://gauger.io/fonticon/) - For favicon

## Credits

* [Codecademy Django course](https://www.codecademy.com/paths/build-python-web-apps-with-django/) - This course introduced me to the use of the generic CBV's for Create, Update and Delete.
* [Code to filter by user group](https://stackoverflow.com/questions/73371568/how-to-check-user-group-in-django-template) - The code for filtering based on a users group was taken from this stack overflow article.
* [Code to add users to a group](https://stackoverflow.com/questions/6288661/adding-a-user-to-a-group-in-django) - The function to make runners into leaders was built using this stack overflow thread.
* [Modifications to allauth standard sign-up](https://stackoverflow.com/questions/12303478/how-to-customize-user-profile-when-using-django-allauth) - The form and settings for accessing first name and last name when signing up in allauth were taken from this stack overflow article.
* [Success messages](https://docs.djangoproject.com/en/4.1/ref/contrib/messages/) - Syntax for adding success messages to views researched from the Django documentation here.
* Custom 404 and 500 pages implemented using Django documentation [here](https://docs.djangoproject.com/en/3.2/topics/http/views/#customizing-error-views) and [this stack overflow thread](https://stackoverflow.com/questions/12180281/implementing-http404-in-django/12180499#12180499)
* [Markdown Builder by Tim Nelson](https://traveltimn.github.io/markdown-builder) - Used for readme and testing document templates
* My mentor Tim Nelson - For support and guidance throughout this project
* Code Institute Slack Community - For their help with troubleshooting, testing and reviewing the project