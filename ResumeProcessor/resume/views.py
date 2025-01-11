from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CandidateSerializer
from .utils import extract_resume_data

import logging


logger = logging.getLogger(__name__)

class ResumeExtractView(APIView):
    def post(self, request, *args, **kwargs):
        file = request.FILES.get('resume')
        
        if not file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        print(f"Received file: {file.name}")  

        try:
            data = extract_resume_data(file)
            print(f"Extracted Data: {data}")  
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"Error: {e}")  
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

