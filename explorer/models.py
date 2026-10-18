# APIUser — Django model class hai. Django default mein iske liye explorer_apiuser naam ki database table banayega.
# models.CharField(...) — text fields store karta hai.
# models.EmailField() — email field define karta hai; model validation mein email format check kar sakta hai.
# __str__() — admin panel jaise interfaces mein record ka readable name dikhata hai.


from django.db import models


class APIUser(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    street = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return self.name
