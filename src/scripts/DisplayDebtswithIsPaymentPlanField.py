import json
import logging
import os
import sys
from Utils import Utils

payment_plans = [] #payment plans data
debts_with_Is_payment_field = [] # debts objects linked to payment plans
debts_with_payment_plans ={} # dic to hold debtId along with payment plans details

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

log_dir_path = os.getcwd()


def addFieldIsPaymentPlanToDebt(payment_plans, debts):
    for debt in debts:
        for payment_plan in payment_plans:
            if debt['id'] == payment_plan['debt_id']:
                debt.update({'is_in_payment_plan': True})
                debts_with_payment_plans[debt['id']] = payment_plan
        if not debt.get('is_in_payment_plan'):
            debt.update({'is_in_payment_plan': False})
        debts_with_Is_payment_field.append(debt)
        print(debt)

def getDebtswithPaymentPlan():
    return debts_with_payment_plans, debts_with_Is_payment_field

def main(payment_plans, debts):
    handler = logging.FileHandler(log_dir_path+'/Scripts.log', 'w+')
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    # console log
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    logger.addHandler(handler)
    logger.addHandler(console)
    addFieldIsPaymentPlanToDebt(payment_plans, debts)

if __name__ == "__main__":
  "This controller is going to be used in Main.py"



