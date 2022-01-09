# local_settings.py
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
       # 'NAME': BASE_DIR / 'db.sqlite3', #this line gives error, so type it as the next one
        'NAME': os.path.join( BASE_DIR , 'db.sqlite3'),
    }
}