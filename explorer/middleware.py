
class SimpleCustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        response["X-App-Name"] = "Public API Data Explorer"

        return response

# __init__: Middleware setup karta hai.
# get_response: Agle middleware ya view ko request bhejne ka tareeka hai.
# __call__: Har request par middleware ka main code chalta hai.
# response["X-App-Name"]: Response mein ek extra header add karta hai.
# return response: Modified response browser ko wapas bhejta hai.