from fastapi import UploadFile

from dal.base_dal import create_base
from utils.place_soldiers import place
from utils.csv_handler import process_csv
from utils.total_placed import get_total
from utils.status_records import get_soldier_record

#constants
BASE_NAME = "Seven Shibolim"

def response(file:UploadFile)->dict:
    #initializes base
    base = create_base(BASE_NAME)

    #converts csv file to list
    data = process_csv(file)

    #qualifying soldiers placed
    #non qualifying soldiers on waiting list
    full_base = place(base, data)

    #gets total of placed soldiers
    placed_soldiers = get_total(base)

    #gets total of waiting soldiers
    waiting_soldiers = len(full_base.waiting_list)

    soldier_record = get_soldier_record(full_base)

    #returns response for http request    
    return {
        'total_placed_soldiers': placed_soldiers,
        'total_waiting_soldiers': waiting_soldiers,
        'soldier_status_record': soldier_record 
    }