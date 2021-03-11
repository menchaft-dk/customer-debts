import os
import pytest
import sys
from Utils import Utils 
import datetime
from datetime import date
from  scripts import DisplayDebtswithIsPaymentPlanField,\
    DisplayDebtsWithRemainingBalance, DisplayDebtsWithNextPaymentDueDate

@pytest.fixture
def  payment_plans():
    return [
        {
            "id": 0,
            "debt_id": 0,
            "amount_to_pay": 102.50,
            "installment_frequency": "WEEKLY", 
            "installment_amount": 51.25,
            "start_date": "2020-09-28"
        },
        {
            "id": 1,
            "debt_id": 1,
            "amount_to_pay": 150.50,
            "installment_frequency": "BIWEEKLY", 
            "installment_amount": 30,
            "start_date": "2020-04-05"
        }
    ]

@pytest.fixture
def debts_with_paymentPlan():
    return {
        0: {
            'amount_to_pay': 130.50, 
            'debt_id': 0, 
            'id': 0, 
            'installment_amount': 25, 
            'installment_frequency': 'WEEKLY', 
            'start_date': '2020-09-28'
        }, 
        1: {
            'amount_to_pay': 50, 
            'debt_id': 1, 
            'id': 1, 
            'installment_amount': 10, 
            'installment_frequency': 'WEEKLY', 
            'start_date': '2020-08-01'
        }
    }

@pytest.fixture
def  payments():
    return [
        {
            "payment_plan_id": 0,
            "amount": 51.25,
            "date": "2020-09-29"
        },
        {
            "payment_plan_id": 0,
            "amount": 51.25,
            "date": "2020-10-09"
        },
        {
            "payment_plan_id": 1,
            "amount": 10.25,
            "date": "2020-09-01"
        }
    ]

@pytest.fixture
def  date_str():
    return '2020-08-02'

@pytest.fixture
def  debts_with_RemainingBalance():
    return [
        {
            "id": 0,
            "amount": 200.00,
            'is_in_payment_plan': True,
            'remaining_amount': 0.0
        },
        {
            "id": 1,
            "amount": 100.00,
            'is_in_payment_plan': True,
            'remaining_amount': 12.0
        }
    ]

@pytest.fixture
def  debts():
    return [
        {
            "id": 0,
            "amount": 200.00,
        },
        {
            "id": 1,
            "amount": 120.23,
        },
        {
            "id": 3,
            "amount": 1000.00,
        }
    ]

def test_getPaymentLinked_withPaymentPlans(payment_plans, payments) :
    payment_with_plans = Utils.getPaymentsLinkedToPayment_plans(payment_plans[0], payments)
    assert(len(payment_with_plans) == 2);
    assert(payment_with_plans[0].get('payment_plan_id') == 0);

def test_formatStringDateToDate(date_str) :
    StringToDate = Utils.formatStringDateToDate(date_str);
    assert(isinstance(StringToDate, datetime.datetime))

def test_formatDateToString():
    today  = date.today()
    expected = today.strftime("%Y-%m-%d")
    date_str = Utils.formatDateToString(today)
    assert(isinstance(date_str, str))
    assert(date_str == expected)

def test_calcultateRemainingAmount(payment_plans, payments):
    remaining_balance = Utils.calcultateRemainingAmount(payment_plans[0], payments)
    expected = 0.0
    assert(remaining_balance == expected)

def test_calculateNextPaymentDueDate_RemaingBalanceIs0_returnNone(debts_with_RemainingBalance, debts_with_paymentPlan):
    debt_updated = Utils.calculateNextPaymentDueDate(debts_with_RemainingBalance[0], debts_with_paymentPlan)
    expected = None
    assert(debt_updated.get('next_payment_due_date') == expected)

def test_calculateNextPaymentDueDate_RemaingBalanceIsNot0_returnDate(debts_with_RemainingBalance, debts_with_paymentPlan):
    debts_with_RemainingBalance[0]['id'] = 1
    debts_with_RemainingBalance[0]['remaining_amount'] = 50.00
    debt_updated = Utils.calculateNextPaymentDueDate(debts_with_RemainingBalance[0], debts_with_paymentPlan)
    expected = "2020-08-08"
    assert(debt_updated.get('next_payment_due_date') == expected)

def test_addFieldIsPaymentPlanToDebt(debts, payment_plans):
    DisplayDebtswithIsPaymentPlanField.addFieldIsPaymentPlanToDebt(payment_plans, debts)
    debts_with_payment_plans, debts_with_Is_payment_field = DisplayDebtswithIsPaymentPlanField.getDebtswithPaymentPlan()
    assert(debts_with_Is_payment_field[0].get('is_in_payment_plan') == True)
    assert(debts_with_Is_payment_field[1].get('is_in_payment_plan') == True)
    assert(debts_with_Is_payment_field[2].get('is_in_payment_plan') == False)


def test_displayDebtsWithRemainingBalance(debts, debts_with_paymentPlan, payments):
    DisplayDebtsWithRemainingBalance.displayDebtsWithRemainingBalance(debts, debts_with_paymentPlan, payments)
    debts_with_remainingBalance, debts_and_payments = DisplayDebtsWithRemainingBalance.getDebtsWithRemainingBalance()
    assert(debts_with_remainingBalance[0].get('remaining_amount') == 28.0)
    assert(debts_with_remainingBalance[1].get('remaining_amount') == 39.75)
    assert(debts_with_remainingBalance[2].get('remaining_amount') == 1000.0) #Not linked to payment plan

def test_displayDebtsWithNextPaymentDueDate_RemainingBalanceIs0_returnNone(debts_with_RemainingBalance, debts_with_paymentPlan):
    DisplayDebtsWithNextPaymentDueDate.displayDebtsWithNextPaymentDueDate(debts_with_RemainingBalance, debts_with_paymentPlan)
    debts = DisplayDebtsWithNextPaymentDueDate.getDebtsWithNextPaymentDueDate()
    assert(debts[0].get('next_payment_due_date') == None)

def test_displayDebtsWithNextPaymentDueDate_RemainingBalanceNot0_returnDate(debts_with_RemainingBalance, debts_with_paymentPlan):
    DisplayDebtsWithNextPaymentDueDate.displayDebtsWithNextPaymentDueDate(debts_with_RemainingBalance, debts_with_paymentPlan)
    debts = DisplayDebtsWithNextPaymentDueDate.getDebtsWithNextPaymentDueDate()
    assert(debts[1].get('next_payment_due_date') == '2020-08-08')
