from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer
from django.db.models import Q

class NotificationCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user = self.request.user
        role = user.role
        email = user.email
        print("email",email)

        # Base queryset for all roles: notifications with type 'disbursement_date'
        disbursement_notifications = Notification.objects.filter(type="disbursement_date")

        # Notifications for own rewards and payments
        own_rewards = Notification.objects.filter(type="reward", payload__employee__email=email)
        own_payments = Notification.objects.filter(type="payment", payload__employee__email=email)

        # Notifications for own approved or rejected advances
        own_approved_or_rejected_advances = Notification.objects.filter(
            type="advance",
            payload__employee__email=email
        ).filter(Q(payload__is_approved=True) | Q(payload__is_rejected=True))
        
        # Notifications for unprocessed advances that are not own
        unprocessed_advances = Notification.objects.filter(
            type="advance",
            payload__is_approved=False,
            payload__is_rejected=False,
            payload__is_cancelled=False
        ).exclude(payload__employee__email=email)  # Exclude own advances

        if role in ['admin', 'management', 'tech_lead']:
            return own_rewards.union(own_payments,unprocessed_advances,own_approved_or_rejected_advances, disbursement_notifications).order_by('-date')

        if role == 'staff':
            return own_approved_or_rejected_advances.union(own_rewards, own_payments, disbursement_notifications).order_by('-date')

        # Default to showing only disbursement notifications if role is not recognized
        return disbursement_notifications.order_by('-date')

class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer

    def destroy(self, request, *args, **kwargs):
        user = request.user
        role = user.role

        if role != 'admin':
            return Response({"detail": "You do not have permission to delete this notification."}, status=status.HTTP_403_FORBIDDEN)
        
        return super().destroy(request, *args, **kwargs)
