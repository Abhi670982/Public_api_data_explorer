import requests
import pandas as pd

from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render

from .services import get_users, save_users
from .exceptions import APIDataFetchError

def home(request):
    try:
        users = get_users()
        error = None
    except APIDataFetchError:
        users = []
        error = "Unable to fetch data. Please try again."

    return render(
        request,
        "explorer/home.html",
        {"users": users, "error": error},
    )


def export_csv(request):
    try:
        users = get_users()
    except APIDataFetchError:
        return HttpResponse(
            "Unable to fetch API data.",
            status = 502,
        )

    df = pd.DataFrame(users)

    response = HttpResponse(
        df.to_csv(index=False),
        content_type="text/csv; charset=utf-8",
    )
    response["Content-Disposition"] = (
        'attachment; filename="users.csv"'
    )

    return response


def export_excel(request):
    try:
        users = get_users()
    except (requests.RequestException, ValueError, KeyError):
        return HttpResponse(
            "Unable to fetch API data.",
            status=502,
        )

    df = pd.DataFrame(users)
    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Users")

    response = HttpResponse(
        output.getvalue(),
        content_type=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        ),
    )
    response["Content-Disposition"] = (
        'attachment; filename="users.xlsx"'
    )

    return response

def sync_users(request):
    try:
        users = get_users()
        save_users(users)
    except APIDataFetchError:
        return HttpResponse(
            "Unable to fetch API data.",
            status=502,
        )
    return HttpResponse(
        f"Successfully synced {len(users)} users to database."
    )