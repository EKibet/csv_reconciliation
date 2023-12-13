from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileUploadSerializer
from .utils import reconcile_csv_util
from django.core.files.storage import FileSystemStorage
import pandas as pd
from django.http import JsonResponse
import json

import pdb
from django.http import FileResponse
import os
from django.conf import settings
class FileUploadView(APIView):
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            source_file = request.FILES['source_file']
            target_file = request.FILES['target_file']

            # Save the uploaded files

            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            
            source_path = fs.save(source_file.name, source_file)
            target_path = fs.save(target_file.name, target_file)
            
            # Read the uploaded CSV files using pandas
            
            source_df = pd.read_csv(fs.url(source_path))
            target_df = pd.read_csv(fs.url(target_path))

            # Perform reconciliation
            # pdb()
            
            reconciliation_report_df = reconcile_csv_util(fs.url(source_path), fs.url(target_path))

            # Convert the reconciliation report to JSON
            # reconciliation_report_json = reconciliation_report_df.to_json(orient='records')
            # pdb()
                # Read the CSV file into a Pandas DataFrame
            reconciliation_df = pd.read_csv(reconciliation_report_df)

            # Convert the DataFrame to JSON
            reconciliation_json = reconciliation_df.to_json(orient='records')
            return JsonResponse(json.loads(reconciliation_json), safe=False)
            
