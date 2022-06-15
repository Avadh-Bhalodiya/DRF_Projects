- Token Authentication

	- settings.py in import: 'rest_framework.authtoken'
	- urls.py in add this url: path('gettoken/', obtain_auth_token)
	- urls.py in import: from rest_framework.authtoken.views import obtain_auth_token