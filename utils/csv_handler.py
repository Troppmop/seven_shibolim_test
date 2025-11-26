from fastapi import UploadFile
import csv
from io import StringIO



#returns json to be used as response for csv route response
def process_csv(file: UploadFile)->list:
    if file.content_type != "text/csv":
        return {"error": "File must be a CSV"}
        
    content = file.file.read().decode('utf-8')

    reader = csv.reader(StringIO(content))
    header = next(reader)
    rows = list(reader)

    return rows
    