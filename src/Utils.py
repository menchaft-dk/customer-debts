import json
import jsonlines
import datetime
from datetime import timedelta 
from constants.Constants import FREQUENCY

freq_ = FREQUENCY

class Utils:

    def create_jsonFile_with_apiResponse(file, data):
        with open(file, 'w+') as outfile:
            json.dump(data, outfile)

    def convertJsonToObject(file):
        with open(file, 'r') as f:
            json_data = json.load(f)
        return json_data

    def createJsonLFIles(jsonFiles):
        for file in jsonFiles:
            with jsonlines.open(file, 'w') as writer:
                writer.write_all(json_data)
    
    def saveJsonDataToJsonLFile(jsonLFile, apiResponse):
         with jsonlines.open(jsonLFile, 'w') as writer:
             writer.write_all(apiResponse)
    
    def readJsonDataFromJsonlFile(jsonLfile):
        with open(jsonLfile, 'r') as f:
            for object in f:
                sys.stdout.write(object)

    def getPaymentsLinkedToPayment_plans(debt_with_plan, payments):
        payment_with_plans = []
        payment_with_plans = [payment for payment in payments if \
            debt_with_plan.get('id') == payment.get('payment_plan_id')]
        return payment_with_plans

    def displayDebts(debts):
        for debt in debts:
            print(debt)

    def calcultateRemainingAmount(debt_with_payment_plan, payments):
        remaining_amount = debt_with_payment_plan.get('amount_to_pay');
        for payment in payments:
            if debt_with_payment_plan.get('id') == payment.get('payment_plan_id'):
                remaining_amount -= payment.get('amount')
        return round(remaining_amount,2)

    def formatStringDateToDate(date_str):
        format_str = '%Y-%m-%d'
        date_formatted= datetime.datetime.strptime(date_str, format_str);
        return date_formatted

        
    def formatDateToString(date):
        format_str = '%Y-%m-%d'
        date_str= date.strftime(format_str);
        return date_str

    def calculateNextPaymentDueDate(debt, debts_and_plans):
        next_payment_due_date = None;
        debt_by_payment_plan_id = debts_and_plans.get(debt['id'])
        if (debt_by_payment_plan_id):
            date_formatted = Utils.formatStringDateToDate(debt_by_payment_plan_id.get('start_date'))
            if debt.get('remaining_amount') != 0 and debts_and_plans:
                frequency = debt_by_payment_plan_id.get('installment_frequency')
                nbr_days = freq_.get(frequency)
                dateTimeObj = date_formatted + timedelta(days=nbr_days)
                next_payment_due_date = Utils.formatDateToString(dateTimeObj);

        debt.update({"next_payment_due_date": next_payment_due_date})
        return debt
