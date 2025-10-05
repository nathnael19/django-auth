from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,username,email,phone,password, **extra_fileds):
        if not email:
            raise ValueError("Email must be provided!")
        if not phone:
            raise ValueError("Phone Number must be provided!")
        
        email =  self.normalize_email(email)
        user = self.model(
            username=username,
            email = email,
            phone = phone,
            **extra_fileds
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
