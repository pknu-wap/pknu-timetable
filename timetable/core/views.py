from django.http import HttpResponse
from django.shortcuts import redirect, render

import xlrd

from .forms import UploadForm
from .models import Subject


def index(request):
    return HttpResponse('index')


def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            wb = xlrd.open_workbook(file_contents=request.FILES['file'].read())
            ws = wb.sheet_by_index(0)
            for i in range(1, ws.nrows):
                row = ws.row_values(i)
                Subject.objects.update_or_create(
                    no=row[2], division=row[3],
                    defaults={
                        'target_college': row[0],
                        'target_department': row[1],
                        'name': row[4],
                        'eng_name': row[5],
                        'point': int(row[6][0]),
                        'point_system': row[6],
                        'type': row[7],
                        'quota': int(row[9]),
                        'is_FL': row[12] == 'Y',
                        'professor': row[13],
                        'day_night': row[14],
                        'grade': int(row[15]),
                        'time_and_location': row[16],
                        'department': row[17],
                    },
                )
            return redirect('index')
    else:
        form = UploadForm()
    return render(request, 'core/upload.html', {'form': form})
