from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os

@csrf_exempt
def reporters(request):
    file_path = os.path.join(os.getcwd(), "reporters.json")

    if request.method == "POST":
        data = json.loads(request.body)

        # Load existing data
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                reporters = json.load(file)
        else:
            reporters = []

        # Add new reporter
        reporters.append(data)

        # Save to file
        with open(file_path, "w") as file:
            json.dump(reporters, file, indent=4)

        return JsonResponse(data)

    if request.method == "GET":
       if os.path.exists(file_path):
           with open(file_path, "r") as file:
               reporters = json.load(file)
       else:
           reporters = []

       return JsonResponse(reporters, safe=False)


@csrf_exempt
def issues(request):
    file_path = os.path.join(os.getcwd(), "issues.json")

    if request.method == "POST":
        data = json.loads(request.body)

        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                issues = json.load(file)
        else:
            issues = []

        issues.append(data)

        with open(file_path, "w") as file:
            json.dump(issues, file, indent=4)

        return JsonResponse(data)

    elif request.method == "GET":
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                issues = json.load(file)
        else:
            issues = []

        return JsonResponse(issues, safe=False)