from django.utils import translation

class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang = (
            request.session.get('django_language') or
            request.COOKIES.get('django_language') or
            'en'
        )
        translation.activate(lang)
        request.LANGUAGE_CODE = lang
        response = self.get_response(request)
        return response