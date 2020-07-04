from django.views.generic import View
from django.http import HttpResponse


class LivenessView(View):
    """
    Health check endpoint running with 0 queries
    """

    def get(self, request, *args, **kwargs):
        return HttpResponse('OK')