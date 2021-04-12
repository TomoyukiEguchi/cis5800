from django.shortcuts import redirect
from django.contrib import messages
from comment.forms import CommentForm


def comment_create(request):
    restaurant_id = request.POST.get("restaurant")
    content = request.POST.get("content")

    data = {"content": content, "restaurant": restaurant_id}

    form = CommentForm(data=data)
    if form.is_valid():
        form.save()
        messages.success(request, "Your comment has been sent.")
    else:
        messages.error(request, "Your comment has not been sent.")

    return redirect("restaurant:detail", pk=restaurant_id)