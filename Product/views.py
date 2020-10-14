from django.shortcuts import render, HttpResponseRedirect
from Product.models import Comment, CommenttForm
# Create your views here.
from django.contrib import messages


def Comment_Add(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        pos = CommenttForm(request.POST)
        if pos.is_valid():
            data = Comment()
            data.subject = pos.cleaned_data['subject']
            data.comment = pos.cleaned_data['comment']
            data.rate = pos.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()
            messages.success(request, 'Your informative comment has been sent')
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)
