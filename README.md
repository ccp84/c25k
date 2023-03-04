# MJ's c25k Registration App

## Concept 

This django app will be a runner registration tool for c25k groups. 
* It will enable the club to advertise details of the next course and allow runners to sign up in readiness for the start date. 
* It will allow run leaders to advertise the details of each weeks date, time and start location. As well as a brief overview of the run. 
* It will allow logged in runners to sign up for posted runs, enabling run leaders to see who is planning on attending before setting off for each session. 
* It could be used to mark runners as completed to maintain a list of graduates within the database, and list graduate runs following on from the main course. 
* It could be used for runners to add an emergency contact to their account which run leaders will be able to access during sessions in case of incident during the run. 
* The overall site will be styled in Joggers green and yellow on completion and function with mobile first design in mind. 

## Table of Contents:
1. [Wireframes](#wireframes)
2. [Data Model](#data-model)

## Wireframes
* Welcome Page Views
![Welcome Page Views](/documentation/welcome_page.png)

* Run Details Page Views
![Run List Page Views](/documentation/run_list.png)

## Data Model

![Entity Relationship Diagram](/documentation/ERD.png)

## Project Development

### Run List 
This feature has been developed using the django generic CBV 'ListView':
```python
class RunList(ListView):
    model = Run
```
With a custom html template to display the correct elements to each user dependent on their authentication status:
```python
{% if user.is_authenticated %}
# List of current runs is displayed for the user
    {% if request.user.groups.all.0.name == 'leader' %}
    # User has ability to edit and delete the listed run, as well as a button to add a new run
{% else %}
# A message is displayed inviting the user to log in, although the page is only shown in the nav bar for authenticated users
```
This page hosts the main functionality of the project allowing only authenticated users to see the full details of each run, as opposed to the basic list on the welcome page. Users tagged with the grouo of leader can also access links to edit and delete runs from the list here, as well as adding a new run from the bottom of the list. 

## Create Run
This feature is only accessible by authenticated users who have a group tag of leader. It makes use of the django generic CBV 'CreateView':
```python
class RunCreate(CreateView):
    model = Run
    template_name = 'run_create.html'
    fields = ["title", "leader", "location", "date", "time", "details"]
    success_url = '/run/list'
``` 
and the standard form for this view, which will be styled in a later part of the project:

![run_create_form](documentation/run_create_form.png)

## Edit Run
This feature is very similar to the creation of a new run. It uses the generic django 'UpdateView':
```python
class RunUpdate(UpdateView):
    model = Run
    template_name = 'run_update.html'
    fields = ["title", "leader", "location", "date", "time", "details"]
    success_url = '/run/list'
```
and again imports the standard form as well. However, the URL associated with this view expects the primary key of the run as an identifier to ensure the correct entry in the database is being updated:
```python
path("run/update/<pk>", views.RunUpdate.as_view(), name='run_update')
```
This is passed in from the html template via the anchor tag:
```html
<td><a href="{% url 'run_update' run.id %}">Edit</a></td>
```
The result is not only that the correct database record is updated, but also that the rendered form is pre populated for editing:

![run_edit_form](documentation/run_edit_form.png)


## Testing

## Deployment

## Technologies Used
* Git - Version control and project flow management
* [GitHub](https://github.com/)
* [Elephant Sql](https://www.elephantsql.com/)
* [Heroku](https://www.heroku.com/home)

## Credits
* [Lucid](https://lucid.app/) - Used to create ERD
* Balsamiq - Used to create wireframes
* paint.net - Used for image manipulation
* [Codecademy django course](https://www.codecademy.com/paths/build-python-web-apps-with-django/) - This course introduced me to the use of the generic CBV's for Create, Update and Delete.
* [Code to filter by user group](https://stackoverflow.com/questions/73371568/how-to-check-user-group-in-django-template) - The code for filtering based on a users group was taken from this stack overflow article.