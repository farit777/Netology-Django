from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement, AdvertisementStatusChoices
from advertisements.serializers import AdvertisementSerializer
from advertisements.filters import AdvertisementFilter
from django_filters import rest_framework as filters
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.response import Response
from rest_framework import status


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated()]
        return super().get_permissions()

    def perform_create(self, serializer):
        user = self.request.user
        open_ads_count = Advertisement.objects.filter(creator=user, status=AdvertisementStatusChoices.OPEN).count()

        if open_ads_count >= 10:
            return Response({"detail": "You cannot create more than 10 open advertisements."}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(creator=user)

class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user or request.method in SAFE_METHODS
