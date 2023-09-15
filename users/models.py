from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class CustomUserManager(UserManager):
    
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    

class CustomUser(AbstractBaseUser, PermissionsMixin):

    nickname = models.CharField("Nickname", max_length=50, unique=True)
    email = models.EmailField("Email", unique=True)
    phone = models.CharField("Phone number", max_length=12, null=True, blank=True)
    avatar = models.ImageField("Photo", upload_to="users/avatar", null=True, blank=True)
    

    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return f"({self.id}) {self.nickname}"    
    
    def save(self, *args, **kwargs) -> None:
        self.nickname = self.email[:self.email.index("@")]
        return super().save(*args, **kwargs)   

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
