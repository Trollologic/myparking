from django.shortcuts import render

def feedback_list(request):
    return render(request, 'myparkingweb/feedback_list.html', {})
