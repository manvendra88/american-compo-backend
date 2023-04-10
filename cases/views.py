from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from active_lawsuits.models import active_law_table

class CaseView(View):
    def get(self, request):
        try:
            final_data = {}
            cases = active_law_table.objects.all()
            caseList = []
            for case in cases:
                caseList.append(case.name)
            final_data.update({"caseList": caseList})
            return JsonResponse(data=final_data, status=200)
        except:
            return JsonResponse(data={"message": "error while fetching cases"}, status=401)