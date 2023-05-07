from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import contact_us_table
from django.core.mail import send_mail

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

            send_mail(
                subject = 'Greetings from American Compo Legal',
                message = 'Dear'+ request.GET.get("fname", '') +', \n\n' + 
                'Thank you for reaching out to Amercian Compo Legal. Your response has successfully submitted. Our representative will reach out to you to help you out with your case. '+
                '\n\nDetails :'+
                '\n\nName:'+ request.GET.get("fname", '')+ ' ' +request.GET.get("lname", '')+
                '\n\nEmail :'+  request.GET.get("email", '')+
                '\n\nMessage : '+request.GET.get("message", '')+
                '\n\nThanks',

                # from_email = 'info@americancompolegal.com',
                from_email = 'connect.toughtech@gmail.com',
                recipient_list = ['connect.toughtech@gmail.com', 'manuspanwar@gmail.com'],
                fail_silently=False,
            ) 

            send_mail(
                subject = 'New Lead Created on ACL',
                message = 'Dear Team NMS, \n\n' + 
                'A new lead has been created through americancompolegal.com. Kindly view the details on the admin panel.'+
                '\n\nDetails :'+
                '\n\nName:'+ request.GET.get("fname", '')+ ' ' +request.GET.get("lname", '')+
                '\n\nEmail : '+ request.GET.get("email", '')+
                '\n\nMessage : '+request.GET.get("message", '')+
                '\n\nThanks',

                # from_email = 'info@americancompolegal.com',
                from_email = 'connect.toughtech@gmail.com',
                recipient_list = ['connect.toughtech@gmail.com'],
                fail_silently=False,
                )
            return JsonResponse(data={"message": "saved contact information"}, status=200)
        except:
            return JsonResponse(data={"message": "error while saving contact information"}, status=402)
