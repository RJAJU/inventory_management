from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView, ListView, UpdateView

from manager.forms import MemberForm
from manager.models import Member


class BookingList(ListView):
    """
    BookingList view class to list all active members and inventory count
    """
    model = Member
    template_name = 'member_list.html'

    def get_queryset(self):
        queryset = super(BookingList, self).get_queryset()
        return queryset.order_by('-date_joined')


class Booking(CreateView):
    """
    Booking view class to add new member against the available inventory
    """
    model = Member
    form_class = MemberForm
    template_name = 'booking.html'
    success_url = reverse_lazy('manager:list')


class BookingEditView(UpdateView):
    """
    BookingEdit view class to update existing member against the available inventory
    """
    model = Member
    form_class = MemberForm
    template_name = 'booking.html'
    success_url = reverse_lazy('manager:list')


def cancel_booking(request, id):
    """
    Cancel view method to remove existing member against the available inventory
    """
    obj = Member.objects.get(id=id)
    obj.booking_count -= 1
    obj.save()
    return redirect(reverse('manager:list'))
