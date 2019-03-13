from .settings import LANGUAGE_CODE


def force_default_language_middleware(get_response):
    """
        Ignore Accept-Language HTTP headers
    """

    def middleware(request):
        if 'HTTP_ACCEPT_LANGUAGE' in request.META \
                and not request.session.get("django_language"):
            del request.META['HTTP_ACCEPT_LANGUAGE']
        else:
            request.META['HTTP_ACCEPT_LANGUAGE'] = \
                request.session.get("django_language", LANGUAGE_CODE)

        response = get_response(request)

        return response

    return middleware
