import json
from Utils import Utils
import logging
import os

debts_and_payments = {} # dict to match debts with payments
debts_with_remainingBalance = [] #return debts with remaining balance

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

log_dir_path = os.path.join(os.getcwd(), 'src')

def displayDebtsWithRemainingBalance(debts, debts_with_payment_plans, payments):
    for debt in debts:
        remaining_amount = 0
        if not debts_with_payment_plans.get(debt['id']):
            remaining_amount = debt.get('amount')
        else:
            debt_with_payment_plan = debts_with_payment_plans.get(debt['id'])
            payments_for_payment_plan = Utils.getPaymentsLinkedToPayment_plans(debt_with_payment_plan, payments)
            remaining_amount = Utils.calcultateRemainingAmount(debt_with_payment_plan, payments_for_payment_plan)
        debt.update({'remaining_amount': remaining_amount})
        debts_with_remainingBalance.append(debt)
        debts_and_payments.update(debts_with_payment_plans);
        print(debt)


def getDebtsWithRemainingBalance():
    return debts_with_remainingBalance, debts_and_payments


def main(debts, debts_with_payment_plans, payments):
    handler = logging.FileHandler(log_dir_path+'/Scripts.log', 'w+')
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    # console log
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    logger.addHandler(handler)
    logger.addHandler(console)
    displayDebtsWithRemainingBalance(debts, debts_with_payment_plans, payments);


if __name__ == "__main__":
    "This Script will be called in Main.py"