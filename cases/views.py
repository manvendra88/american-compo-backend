from django.shortcuts import render
from .models import case_table
from django.views import View
from django.http import JsonResponse

class CaseView(View):
    def get(self, request):
        try:
            final_data = {}
            cases = case_table.objects.all()
            caseList = []
            for case in cases:
                caseList.append(case.case_name)
            final_data.update({"caseList": caseList})
            return JsonResponse(data=final_data, status=200)
        except:
            return JsonResponse(data={"message": "error while fetching cases"}, status=401)