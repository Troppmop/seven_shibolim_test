from fastapi import UploadFile
import csv
from io import StringIO

from models.base import Base
from dal.soldier_dal import create_soldier
from dal.base_dal import create_base
from dal.dorm_dal import create_dorm
from dal.room_dal import create_room

def process_csv(file: UploadFile)->dict:
    if file.content_type != "text/csv":
        return {"error": "File must be a CSV"}
        
    content = file.file.read().decode('utf-8')

    reader = csv.reader(StringIO(content))
    header = next(reader)
    rows = list(reader)

    base = create_base("Seven Shibolim")
    dormA = create_dorm("A")
    dormB = create_dorm("B")
    base.dorms.append(dormA)
    base.dorms.append(dormB)
    for dorm_index in range(len(base.dorms)):
        print(base.dorms[dorm_index])
        for room_index in range(10):
            base.dorms[dorm_index].rooms.append(create_room(room_index))
            print(base.dorms[dorm_index].rooms[room_index])
    
    for line in rows:
        base.waiting_list.append(create_soldier(line))
    
    def sort_key(e):
        return e.distance_km

    base.waiting_list.sort(key=sort_key)
    for dorm_i in range(len(base.dorms)):
        for room_i in range(len(base.dorms[dorm_i].rooms)):
            for bed_index in range(8):
                base.dorms[dorm_i].rooms[room_i].occupants.append(base.waiting_list.pop())
                base.dorms[dorm_i].rooms[room_i].occupants[-1].placement_status = 'placed'
    
    
    print(base)
    return {
        'filename': file.filename,
        'content_type': file.content_type,
        'total_rows': len(rows),
        'columns': header,
        'data': rows[0:5],
        'message': 'succesfully processed csv file'
        }