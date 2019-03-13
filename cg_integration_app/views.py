from django.shortcuts import redirect
from .settings import LANGUAGE_CODE
import os

def generate_url(lang, path):
    url_prefix = os.getenv('APP_PROTOCOL')
    url_host = os.getenv('APP_HOST')
    url_port = os.getenv('APP_PORT')
    generated_url = f"{url_prefix}://{url_host}:{url_port}/{lang}{path}"
    return generated_url


def switch_language(request, lang=LANGUAGE_CODE, path='/'):
    request.session['django_language'] = lang
    url_to_redirect = generate_url(lang, path)
    return redirect(url_to_redirect)
