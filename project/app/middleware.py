# # app/middleware.py

# from django.contrib.auth import logout
# from django.urls import reverse
# from django.utils.deprecation import MiddlewareMixin

# class AdminLogoutMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         if request.user.is_authenticated and request.path.startswith('/admin/'):
#             # Set a flag in the session indicating the user has visited the admin panel
#             request.session['visited_admin'] = True
#         elif request.user.is_authenticated and request.session.get('visited_admin'):
#             # If the user is authenticated and has visited the admin, log them out if they visit a non-admin page
#             if not request.path.startswith('/admin/'):
#                 logout(request)
#                 # Optionally, you can redirect them to the login page or another page
#                 # return HttpResponseRedirect(reverse('login'))  # replace 'login' with your login URL name
#         return None


# myapp/middleware.py

from django.contrib.auth import logout
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect

class AdminLogoutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated and request.path.startswith('/admin/'):
            # Set a flag in the session indicating the user has visited the admin panel
            request.session['visited_admin'] = True
        elif request.user.is_authenticated and request.session.get('visited_admin'):
            # If the user is authenticated and has visited the admin, log them out if they visit a non-admin page
            if not request.path.startswith('/admin/'):
                logout(request)
                # Optionally, you can redirect them to the login page or another page
                return HttpResponseRedirect(reverse('home'))  # replace 'login' with your login URL name
        return None
