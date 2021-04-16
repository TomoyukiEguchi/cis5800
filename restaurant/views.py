from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse, reverse_lazy

from django.contrib import messages

from .models import Restaurant
from comment.forms import CommentForm


# Create your views here.

class RestaurantListView(ListView):
    model = Restaurant

    def get_queryset(self):
        return Restaurant.objects.all().order_by('-updated_at')


class RestaurantDetailView(DetailView):
    model = Restaurant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['CommentForm'] = CommentForm(initial={'restaurant': self.object})

        return context


class ConfirmPreOrder(DetailView):
    template_name = 'restaurant/restaurant_confirm_pre_order.html'
    model = Restaurant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['CommentForm'] = CommentForm(initial={'restaurant': self.object})        
        
        return context