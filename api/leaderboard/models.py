from django.db import models
from datetime import datetime, timezone, timedelta
# from django.contrib.auth.models import User

from rest_framework_simplejwt.tokens import OutstandingToken
from rest_framework_simplejwt.models import TokenUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from djongo import models
from djongo.models import ObjectIdField
from bson import ObjectId

import logging
logger = logging.getLogger(__name__)

class CustomUserManager(BaseUserManager):
    def create_user(self,username,first_name,last_name,email, password=None):
        if not username:
            raise ValueError('Users must have an username')
#self.normalize_username(username)
        user = self.model(username=username)
        user.set_password(password)
        user.email = email
        user.first_name = first_name
        user.last_name=last_name
        if not user._id:  # Only generate if `_id` field is not set
            user._id = ObjectId()
        user.save(using=self._db)
        
        return user

    def create_superuser(self,username, password):
        
        user = self.model(
            username=username
        )
        user.set_password(password)
        user.is_admin = True
        user.staff = True
        user.active = True
        user.save(using=self._db)

        return user
    
    def find_user_by_username(self, username):
        try:
            return self.get(username=username)
        except self.model.DoesNotExist:
            return None


class CustomUser(AbstractBaseUser):
    # _id = models.CharField(max_length = 25)
    _id = ObjectIdField(primary_key=True, default = '')
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    username = models.CharField(max_length=64, unique=True)
    first_name = models.CharField(max_length=64, blank = True,default = '')
    last_name = models.CharField(max_length=64, blank = True,default = '')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
  
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['full_name', 'gender', 'username',]
    def __str__(self):
        return self

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    

    @property
    def is_staff(self):
        return self.is_admin
    
    class Meta:
        pass


# from django.contrib.auth import get_user_model
# User = get_user_model()






# Your other models here...

# class CustomOutstandingTokenManager(models.Manager):
#     def create(self, *args, **kwargs):
#         user = kwargs.get('user')
#         token = kwargs.get('token')
        
#         # Check if the user is already saved
#         if not user.pk:
#             user.save()
        
#         token_user = TokenUser.objects.create(user=user, token=token)
#         kwargs['token_user'] = token_user
        
#         return super().create(*args, **kwargs)

# class CustomOutstandingToken(OutstandingToken):
#     objects = CustomOutstandingTokenManager()

    # class Meta(OutstandingToken._meta):
    #     # Add any custom Meta options here
    #     ordering = ['-created']


# Register the CustomOutstandingToken model in the Django admin if needed
#admin.site.register(CustomOutstandingToken)






class githubUser(models.Model):
    # _id = ObjectIdField(primary_key=True, default = '')
    _id = ObjectIdField(primary_key=True, default = '')
    username = models.CharField(max_length=64, unique=True)
    contributions = models.PositiveIntegerField(default=0)
    repositories = models.PositiveIntegerField(default=0)
    stars = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    avatar = models.CharField(max_length=256, default="")
    @property
    def is_outdated(self):
        if datetime.now(tz=timezone.utc) - self.last_updated > timedelta(
            minutes=1
        ):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.username}"


class openlakeContributor(models.Model):
    _id = ObjectIdField(primary_key=True, default = '')
    username = models.CharField(max_length=64, unique=True)
    contributions = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    # _id = ObjectIdField(primary_key=True, default = '')
    @property
    def is_outdated(self):
        if datetime.now(tz=timezone.utc) - self.last_updated > timedelta(
            minutes=1
        ):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.username}"

    class Meta:
        ordering = ["-contributions"]


class codeforcesUser(models.Model):
    # _id = ObjectIdField(primary_key=True, default = '')
    _id = ObjectIdField(primary_key=True, default = '')
    username = models.CharField(max_length=64, unique=True)
    max_rating = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField(default=0)
    last_activity = models.PositiveIntegerField(
        default=datetime.max.timestamp()
    )
    last_updated = models.DateTimeField(auto_now=True)
    avatar = models.CharField(max_length=256, default="")
    
    @property
    def is_outdated(self):
        if datetime.now(tz=timezone.utc) - self.last_updated > timedelta(
            minutes=1
        ):
            return True
        else:
            False

    def __str__(self):
        return f"{self.username} ({self.rating})"

    class Meta:
        ordering = ["-rating"]


class codechefUser(models.Model):
    # _id = ObjectIdField(primary_key=True, default = '')
    _id = ObjectIdField(primary_key=True, default = '')
    username = models.CharField(max_length=64, unique=True)
    max_rating = models.PositiveIntegerField(default=0)
    Global_rank = models.CharField(max_length=10, default="NA")
    Country_rank = models.CharField(max_length=10, default="NA")
    rating = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    avatar = models.CharField(max_length=256, default="")
    @property
    def is_outdated(self):
        if datetime.now(tz=timezone.utc) - self.last_updated > timedelta(
            minutes=3
        ):
            return True
        else:
            False

    def __str__(self):
        return f"{self.username} ({self.rating})"

    class Meta:
        ordering = ["-rating"]


def get_default_cf_user():
    return codeforcesUser.objects.get_or_create(username="tourist")[0]


class codeforcesUserRatingUpdate(models.Model):
    cf_user = models.ForeignKey(
        codeforcesUser,
        default=get_default_cf_user,
        on_delete=models.CASCADE,
        related_name="rating_updates",
    )
    index = models.PositiveIntegerField(default=0)
    prev_index = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField(default=0)
    timestamp = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.cf_user.username}.{self.index} {self.rating}"

    class Meta:
        ordering = ["timestamp"]
        
class LeetcodeUser(models.Model):
    # _id = ObjectIdField(primary_key=True, default = '')
    _id = ObjectIdField(primary_key=True, default = '')
    username = models.CharField(max_length=64, unique=True)
    ranking = models.PositiveIntegerField(default=0)
    easy_solved = models.PositiveIntegerField(default=0)
    medium_solved = models.PositiveIntegerField(default=0)
    hard_solved = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    avatar = models.CharField(max_length=256, default="")
    @property
    def is_outdated(self):
        if datetime.now(tz=timezone.utc) - self.last_updated > timedelta(
            minutes=1
        ):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.username}"

    class Meta:
        ordering = ["ranking"]

class UserNames(models.Model):
    _id = ObjectIdField(primary_key=True, default = '')
    user =models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    cc_uname = models.CharField(max_length=64)
    cf_uname = models.CharField(max_length=64)
    gh_uname = models.CharField(max_length=64)
    lt_uname = models.CharField(max_length=64,default="")

class GithubFriends(models.Model):
    user =models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    ghFriend_uname=models.CharField(max_length=64)
class LeetcodeFriends(models.Model):
    user =models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    ltFriend_uname=models.CharField(max_length=64)
class CodeforcesFriends(models.Model):
    user =models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    cfFriend_uname=models.CharField(max_length=64)
class CodechefFriends(models.Model):
    user =models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    ccFriend_uname=models.CharField(max_length=64)
class OpenlakeFriends(models.Model):
    user =models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    olFriend_uname=models.CharField(max_length=64)