from fastapi import UploadFile
import csv
from io import StringIO

from dal.soldier_dal import create_soldier

def process_csv(file: UploadFile)->dict:
    if file.content_type != "text/csv":
        return {"error": "File must be a CSV"}
        
    content = file.file.read().decode('utf-8')

    reader = csv.reader(StringIO(content))
    header = next(reader)
    rows = list(reader)

    for line in rows:
        print(create_soldier(line))

    return {
        'filename': file.filename,
        'content_type': file.content_type,
        'total_rows': len(rows),
        'columns': header,
        'data': rows[0:5],
        'message': 'succesfully processed csv file'
        }