from django.urls import path

from manager.views import BookingList, Booking, cancel_booking, BookingEditView

urlpatterns = [
    path('', BookingList.as_view(), name="list"),
    path('book/', Booking.as_view(), name="book"),
    path('update/<int:pk>', BookingEditView.as_view(), name="update"),
    path('cancel/<int:id>', cancel_booking, name="cancel"),
]
