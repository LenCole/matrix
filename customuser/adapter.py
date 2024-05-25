ACCOUNT_ADAPTER = 'project.users.adapter.MyAccountAdapter'

# project/users/adapter.py:
from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):

    # def get_login_redirect_url(self, request):
    #     path = "/accounts/{username}/"
    #     return path.format(username=request.user.username)

    def get_login_redirect_url(self, request):
        path = '/dashboard/'
        return path

    def get_logout_redirect_url(self, request):
        path = '/'
        return path

    def get_signup_redirect_url(self, request):
        path = '/dashboard/'
        return path
        # TODO: add thank you for signing up page