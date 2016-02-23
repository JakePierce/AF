from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.


def home_view(request):

    context = {}

    return render_to_response('home_view.html', context, context_instance=RequestContext(request))


def about_view(request):

    context = {}

    return render_to_response('about_view.html', context, context_instance=RequestContext(request))


def client_view(request):

    context = {}

    return render_to_response('client_view.html', context, context_instance=RequestContext(request))


def contact_view(request):

    context = {}

    return render_to_response('contact_view.html', context, context_instance=RequestContext(request))


def thrive_client(request):

    context = {}

    return render_to_response('thrive_client.html', context, context_instance=RequestContext(request))


def title_client(request):

    context = {}

    return render_to_response('title_client.html', context, context_instance=RequestContext(request))


def ring_client(request):

    context = {}

    return render_to_response('ring_client.html', context, context_instance=RequestContext(request))


def nectar_client(request):

    context = {}

    return render_to_response('nectar_client.html', context, context_instance=RequestContext(request))


def map_view(request):

    context = {}

    return render_to_response('map_view.html', context, context_instance=RequestContext(request))
