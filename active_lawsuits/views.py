from django.shortcuts import render
from django.views import View
from .models import active_lawsuit_table
from django.http import JsonResponse

class ActiveLawsuitsView(View):
    def get(self, request):
        try:
            if(request.GET.get('name', '')):
                lawsuit = active_lawsuit_table.objects.get(name=request.GET.get('name', ''))
                return JsonResponse(data={
                    "name": lawsuit.name,
                    "imageLink": lawsuit.image.url,
                    "text": lawsuit.text
                }, status=200)
            page = int(request.GET.get('page', '1'))
            items = int(request.GET.get('items', '3'))
            lawsuits = active_lawsuit_table.objects.all()
            lawsuitList = []
            for ind in range((page-1)*(items), min(len(lawsuits), ((page-1)*(items))+items)):
                lawsuitList.append({
                    "name": lawsuits[ind].name,
                    "imageLink": lawsuits[ind].image.url
                })
            return JsonResponse(data={"lawsuitList": lawsuitList, "total_lawsuits": len(lawsuits)}, status=200)
        except Exception as e:
            return JsonResponse(data={"message": "unable to get lawsuits data"}, status=404)
        
class AllActiveLawsuitsView(View):
    def get(self, request):
        try:
            lawsuits = active_lawsuit_table.objects.all()
            lawsuitList = []
            for lawsuit in lawsuits:
                lawsuitList.append(lawsuit.name)
            return JsonResponse(data={"lawsuitList": lawsuitList}, status=200)
        except:
            return JsonResponse(data={"message": "unable to get lawsuits data"}, status=404)