
import requests
from .models import APIUser
from .exceptions import APIDataFetchError
from .account import validate_name, validate_email

API_URL = "https://jsonplaceholder.typicode.com/users"


def get_users():
    try:
        response = requests.get(API_URL, timeout=10)
        # timeout=10 — request ko indefinitely wait karne se rokta hai.
        response.raise_for_status() #unsuccessful HTTP status par exception raise karta hai.

        users = response.json() #JSON response ko Python data mein convert karta hai.
        data = []

        for user in users:
            data.append({
                "Name": user["name"],
                "Username": user["username"],
                "Email": user["email"],
                "City": user["address"]["city"],
                "Company": user["company"]["name"],
                "Phone": user["phone"],
                "Street": user["address"]["street"],
                "Zipcode": user["address"]["zipcode"],
            })

        return data

    except (
        requests.RequestException,
        ValueError,
        KeyError,
        TypeError,
    ) as exc:
        raise APIDataFetchError(
            "Unable to fetch or process API data."
        ) from exc




# APIUser.objects — Django ORM ke through database records access karna.
# update_or_create() — email se existing record dhoondhna; milne par update karna, nahi milne par create karna.
# defaults — create ya update karne wale fields aur values.

def save_users(users):
    for user in users:
        name = user.get("Name")
        email = user.get("Email")

        if not validate_name(name):
            continue

        if not validate_email(email):
            continue

        APIUser.objects.update_or_create(
            email=email.strip(),
            defaults={
                "name": name.strip(),
                "username": user["Username"],
                "city": user["City"],
                "company": user["Company"],
                "phone": user["Phone"],
                "street": user["Street"],
                "zipcode": user["Zipcode"],
            },
        )
