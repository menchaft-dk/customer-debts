import json
import jsonlines
import sys
import os
import logging
from Utils import Utils
from service.api import Api
from scripts import DisplayDebts, DisplayDebtswithIsPaymentPlanField, DisplayDebtsWithRemainingBalance,\
    DisplayDebtsWithNextPaymentDueDate
import loadDataFromApis


debts = []
debts_with_payment_plans = {}
payments = []
debtsJsonLfile = os.path.join(os.getcwd(), 'data\debts.jl');
debtsJsonfile = os.path.join(os.getcwd(), 'data\debts.json');
payment_plan_jsonfile = os.path.join(os.getcwd(), 'data\payment_plans.json');
payments_jsonFile = os.path.join(os.getcwd(), 'data\payments.json');
debts_and_payments = {}
debts_with_remainingBalance = []

logging.getLogger().setLevel(level=logging.INFO)

log_dir_path = os.getcwd()


def main():
    logging.info("Started script for customers debts and payments..... \n")
    logging.info("Load apis response into json files..... \n ")
    loadDataFromApis.main();

    logging.info("Completed Loading apis response into json files..... \n")
    payments = Utils.convertJsonToObject(payments_jsonFile);
    debts = Utils.convertJsonToObject(debtsJsonfile);
    payment_plans = Utils.convertJsonToObject(payment_plan_jsonfile);

    logging.info("Display Debts objects..... \n")
    DisplayDebts.main(debts);
    print(" ")

    logging.info("Display Debts objects with Is payment plan field..... \n")
    DisplayDebtswithIsPaymentPlanField.main(payment_plans, debts);
    print(" ")
    debts_with_payment_plans, debts = DisplayDebtswithIsPaymentPlanField.getDebtswithPaymentPlan();
    
    logging.info("Display Debts objects with remaining balance..... \n")
    DisplayDebtsWithRemainingBalance.main(debts, debts_with_payment_plans, payments);

    debts_with_remainingBalance, debts_and_payments = DisplayDebtsWithRemainingBalance.getDebtsWithRemainingBalance();
    print(" ")
    logging.info("Display Debts objects with next payment due date..... \n")
    DisplayDebtsWithNextPaymentDueDate.main(debts_with_remainingBalance, debts_and_payments);


if __name__== "__main__":
    main()