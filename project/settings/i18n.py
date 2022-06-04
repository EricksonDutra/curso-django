# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/
from . import BASE_DIR

LANGUAGE_CODE = 'pt_BR'

TIME_ZONE = 'America/Campo_Grande'

USE_I18N = True

USE_TZ = True


LOCALE_PATHS = [
    BASE_DIR / 'locale',
]
