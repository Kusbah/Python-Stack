from django.db import models
import re,bcrypt
# Create your models here.
class UserManager(models.Manager):
    def validate_register(self,postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name'])<2:
            errors["first_name"] = "First Name Should be More Then 2 char"
        if len(postData['last_name'])<2:
            errors["last_name"] = "Last Name Should be More Then 2 char"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invaild Email"
        if User.object.filter(email=postData['email']).exists():
            errors["email"] = "Email already in use"
        if len(postData['password'])<8:
            errors["passowrd"] = "Passowrd should be more then 8 char"
        if postData['password'] != postData['confirm_password']:
            errors["passowrd"] = "Password not match"
        return errors
    
    def validate_login(self,postData):
            errors = {}
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL_REGEX.match(postData['email']):
                errors["email"] = "Invaild Email"

            return errors
    
class ProjectManager(models.Manager):
    def validate_project(self,postData):
        errors = {}
        if len(postData['name'])<3:
            errors["name"] = "Project name must be more then 3 char"
        if len(postData['description'])<10:
            errors["description"] = "description must be more then 10"
        if len(postData['start_date'])<0:
            errors["start_date"] = "Dates should not be blank"
        if len(postData['end_date'])<0:
            errors["end_date"] = "Dates should not be blank"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(unique=True)
    password = models.CharField(max_length=255)
    object = UserManager()


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    team = models.ManyToManyField(User, related_name="joined_projects", blank=True)
    project_owner = models.ForeignKey(User,on_delete=models.CASCADE)
    objects = ProjectManager()







def createUser(post):
    pw_hash = bcrypt.hashpw(post['password'].encode(),bcrypt.gensalt()).decode()
    user = User.object.create(first_name=post['first_name'],last_name=post['last_name'],email = post['email'],password = pw_hash)
    return user

def login_user(post):
    user = User.object.filter(email=post['email'])
    if not user:
        return None
    if bcrypt.checkpw(post['password'].encode(),user[0].password.encode()):
        return user[0]
    else:
        return None
    
def create_Project(post, user_id):
    user = User.object.get(id=user_id)
    project = Project.objects.create(name=post['name'],description=post['description'],start_date=post['start_date'],end_date=post['end_date'],project_owner=user)
    return project