import logging
import os
import sys
from pathlib import Path
from constants.Constants import DEBTS_ENDPOINT, PAYMENT_ENDPOINT, PAYMENT_PLANS_ENDPOINT,\
    DEBTS_JSONL, PAYMENTS_JSONL, PAYMENT_PLANS_JSONL,DEBTS_JSON,PAYMENT_PLANS_JSON, PAYMENTS_JSON
import json
import jsonlines
from Utils import Utils
from service.api import Api


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

data_dir_path = os.path.join(os.getcwd(), 'data')
debts_endpoint = DEBTS_ENDPOINT
payment_plan_endpoint = PAYMENT_PLANS_ENDPOINT
payments_endpoint = PAYMENT_ENDPOINT
debt_jl = os.path.join(data_dir_path,DEBTS_JSONL)
payment_jl = os.path.join(data_dir_path, PAYMENTS_JSONL)
payment_plan_jl = os.path.join(data_dir_path,PAYMENT_PLANS_JSONL)
debt_file_path = os.path.join(data_dir_path,DEBTS_JSON) 
payment_plan_file_path = os.path.join(data_dir_path,PAYMENT_PLANS_JSON)
payments_file_path = os.path.join(data_dir_path,PAYMENTS_JSON)

#Script to calls the apis endpoints and save the response in some files
#That will help us to avoid calling the endpoints everytime in our scripts
def loadDataFromApis():
    debts = Api.makeApiCall(debts_endpoint);
    payment_plans = Api.makeApiCall(payment_plan_endpoint);
    payments = Api.makeApiCall(payments_endpoint)
    
    Utils.create_jsonFile_with_apiResponse(debt_file_path, debts);
    Utils.create_jsonFile_with_apiResponse(payment_plan_file_path, payment_plans);
    Utils.create_jsonFile_with_apiResponse(payments_file_path, payments);

    Utils.saveJsonDataToJsonLFile(debt_jl, debts);
    Utils.saveJsonDataToJsonLFile(payment_jl, payments);
    Utils.saveJsonDataToJsonLFile(payment_plan_jl, payment_plans);

def main():
    loadDataFromApis()

if __name__=="__main__":
    "This controller will be called in Main.py"