from django.http import HttpResponse


def show_view(request):
    return HttpResponse('show_view Ok!')

