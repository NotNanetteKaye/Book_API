# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--1)djz3^%k#yk3_9dg#q*b26sa(@zbwy@7*rb(x)$=iyd)_2br'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'books_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'root'
    }
}