from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics, mixins, viewsets, status
# from .serializers import SponsorshipSerializers
# # from modules.sponsorship.models import Sponsorship
#
# class SponsorshipAPIView(mixins.CreateModelMixin, generics.ListAPIView):
#  lookup_field = 'pk'
#  serializer_class = SponsorshipSerializers
#
# def get_queryset(self):
#     qs = Sponsorship.objects.all()
#     query = self.request.Get.get('q')
#     if query is not None:
#         qs = qs.filter(Q(status__icontains=query))
#     return qs
#
# def post(self, request, *args, **kwargs):
#
#     return self.create(request, *args, **kwargs)
