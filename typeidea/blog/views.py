from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

def post_list(request):
    return HttpResponse('白日依山尽，黄河入海流')


def post_detail(request, post_id):
    return HttpResponse('detail')
