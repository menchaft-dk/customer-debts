
from Utils import Utils
import logging
import os

debts = []

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

log_dir_path = os.getcwd()

def displayDebtsWithNextPaymentDueDate(debts_with_remainingBalance, debts_and_payments):
    for debt in debts_with_remainingBalance:
        debt = Utils.calculateNextPaymentDueDate(debt, debts_and_payments)
        debts.append(debt)
        print(debt)

def getDebtsWithNextPaymentDueDate():
    return debts 
          
def main(debts_with_remainingBalance, debts_and_payments):
    handler = logging.FileHandler(log_dir_path+'/Scripts.log', 'w+')
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    # console log
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    logger.addHandler(handler)
    logger.addHandler(console)

    displayDebtsWithNextPaymentDueDate(debts_with_remainingBalance, debts_and_payments)

if __name__ == "__main__":
    "This script will be called in Main.py"
