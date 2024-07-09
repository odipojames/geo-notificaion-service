from django.urls import path
from .views import NotificationCreateView, NotificationDetailView

urlpatterns = [
    path('notifications/', NotificationCreateView.as_view(), name='notification-list-create'),
    path('notifications/<uuid:pk>', NotificationDetailView.as_view(), name='notification-detail'),
]
