from django.db import models
import re,bcrypt
# Create your models here.

class UserManager(models.Manager):
    def validate_register(self,postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name'])<2:
            errors["first_name"] = "First Name should be more the 2 characters"
        if len(postData['last_name'])<2:
            errors["last_name"] = "Last Name should be more the 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invaild Email"
        if User.objects.filter(email=postData['email']).exists():
            errors["email"] = "Email already in use"
        if len(postData['password'])<8:
            errors["password"] = "Password should be more then 8"
        if postData['password'] != postData['confirm_password']:
            errors["password"] = "Password should match"
        return errors
    def validate_login(self,postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invaild Email"
        return errors

class BookManager(models.Manager):
    def validate_book(self,postData):
        errors = {}
        if len(postData['title'])<1:
            errors["title"] = "the title required"
        if len(postData['desc'])<5:
            errors["desc"] = "Description sshould be more the 5 characters"
        return errors 
        
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()



def createUser(post):
    pw_hash = bcrypt.hashpw(post['password'].encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(first_name=post['first_name'],last_name=post['last_name'],email = post['email'],password = pw_hash)
    return user

def login_user(post):
    user = User.objects.filter(email=post['email'])
    if not user:
        return None
    if bcrypt.checkpw(post['password'].encode(), user[0].password.encode()):
        return user[0]
    else:
        return None

def createBook(post, user_id):
    user = User.objects.get(id=user_id)
    book = Book.objects.create(title=post['title'],desc=post['desc'],uploaded_by=user)
    return book