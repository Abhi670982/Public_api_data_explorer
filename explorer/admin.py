# Is file mein models ko Django admin panel mein register kar sakte hain.



from django.contrib import admin
from .models import APIUser
# Register your models here.

@admin.register(APIUser) # APIUser model admin panel mein register ho jayega.

class APIUserAdmin(admin.ModelAdmin):
    list_display = (  # list_display selected fields ko table mein dikhayega.

        "name",
        "username",
        "email",
        "city",
        "company",
    )
    
    
    search_fields=( # search_fields records search karne dega.

        "name",
        "username",
        "email",
        "city",
        "company",
    )
    
    
