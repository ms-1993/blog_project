from django.db import models

# Create your models here.
"""
Project : DIY Django Mini Blog 
Tech stack : Django, Python, HTML, CSS , JavaScript
Description 
Create a blog web application with following components:- 

• Home page 
●	Display all posts along with their author name, posted date & thumbnail. 
    ◦ Add search options to search blog by title and author. 
●	 AUTH: Any Anonymous users can read blogs.  



• Registration Page 
●	Register new users as authors. 
Registration fields: users email, mobile , username, password. 
●	Username/ Email must be unique. 


• Login Page 
Allow users to login with username/Email and password. 
Add forgot password link. Reset new password through email. 

"""
"""

• Add New Blog Page 
◦ Field: Blog Title, Blog Body, thumbnail image. 
◦ AUTH: Only Authenticated users.  


• Users Profile 
◦ Display list of their blogs. 
◦ Add /Remove blog options. 
◦ AUTH: Only Authenticated users. 



Upload tasks to your github account and share the link of the project.
Or else you can deploy this project and share the url.


"""
#
# from django.contrib.auth.models import User
#
#
# # create a tuple for the status of each post
# STATUS = (
#     (0, "Draft"),
#     (1, "Publish")
# )
#
#
# # each field in this class represents a column in the database table
# class Post(models.Model):
#     title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
#     updated_on = models.DateTimeField(auto_now=True)
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     status = models.IntegerField(choices=STATUS, default=0)
#
#     # this class contains metadata and uses the created_on field from the model to sort out data which sorts
#     # in descending order by default
#     class Meta:
#         ordering = ['-created_on']
#
#     # this method is the default human-readable representation of the object. Django will use it in many places
#     # such as the admin panel
#     def __str__(self):
#         return self.title
