from django.shortcuts import redirect
from django.utils.translation import activate
from .settings import LANGUAGE_CODE

def switch_language(request, lang='en'):
    print(lang, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print(request.get_raw_uri())
    next = request.POST.get('next', None)
    if not next:
        next = request.META.get('HTTP_REFERER', None)
    if not next:
        next = '/'
    request.session['django_language'] = lang
    LANGUAGE_CODE = lang
    response = redirect(next)

    return response
