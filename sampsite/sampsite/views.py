from django.http import HttpResponse

''' Http Response is used to pass information back to view '''

import random

'''get a request from a view and return response back'''


def hello_world(request):
    return HttpResponse("Hello World")


def root_page(request):
    return HttpResponse("Root Home Page")


''' Receive a Number passed from a URL and return a random function'''
def random_number(request, max_rand=100):
    random_num = random.randrange(0, int(max_rand))

    msg = f"Random Number between 0 and {max_rand} : {random_num} "
    return HttpResponse(msg)
