from django.shortcuts import render
from django.views import View
from .models import about_us_table
from django.http import JsonResponse

# Create your views here.
class ContactUsView(View):
    def get(self, request):
        try:
            return JsonResponse(data={
                "imageLink": about_us_table.objects.all()[0].image.url,
                "text": about_us_table.objects.all()[0].text
            }, status=200)
        except: 
            return JsonResponse(data={"message": "unable to fetch about us data"}, status=401)