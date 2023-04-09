from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import contact_us_table

class ContactUsView(View):
    def get(self, request):
        try:
            if(len(request.GET.get("fname", ''))==0 or len(request.GET.get("lname", ''))==0 or len(request.GET.get("email", ''))==0 or len(request.GET.get("phone", ''))==0 or len(request.GET.get("message", ''))==0):
                return JsonResponse(data={"message": "information can't be empty"}, status=401)
            contact_info = contact_us_table(
                first_name = request.GET.get("fname", ''),
                last_name = request.GET.get("lname", ''),
                email_address = request.GET.get("email", ''),
                phone_number = request.GET.get("phone", ''),
                message = request.GET.get("message", ''),
            )
            contact_info.save()
            return JsonResponse(data={"message": "saved contact information"}, status=200)
        except:
            return JsonResponse(data={"message": "error while saving contact information"}, status=402)
