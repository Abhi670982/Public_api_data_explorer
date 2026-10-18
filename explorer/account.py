# Hum account.py mein validation functions bana sakte hain, jaise:
# - Name empty toh nahi hai.
# - Email valid format mein hai ya nahi.
# - Required fields missing toh nahi hain.
# - API se aaya data expected format mein hai ya nahi.


import re #Python ka regular expression module import karta hai. Hum ise email ke format ko check karne ke liye use kar rahe hain.

def validate_name(name):
    """check whether the name is valid."""
    if not isinstance(name, str):
        return False
    
    if not name.strip():
        return False
    
    return True

def validate_email(email):
    """check whether the email has a basic valid format."""
    if not isinstance(email, str):
        return False 
    
    email = email.strip()
    
    if not email:
        return False
    
    pattern = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"

    return re.match(pattern, email) is not None
 