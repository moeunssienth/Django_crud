from django.db import models

# class ExampleModel(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
  

class Test(models.Model):
     fullname= models.CharField(max_length=100)
     emp_code = models.CharField(max_length=10, unique=True)
     mobile = models.CharField(max_length=15, unique=True)
     position = models.ForeignKey(Position, on_delete=models.CASCADE)


# Create your models here.
