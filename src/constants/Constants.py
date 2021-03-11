
#Apis endpoints
DEBTS_ENDPOINT = "https://my-json-server.typicode.com/druska/trueaccord-mock-payments-api/debts"
PAYMENT_PLANS_ENDPOINT = "https://my-json-server.typicode.com/druska/trueaccord-mock-payments-api/payment_plans"
PAYMENT_ENDPOINT="https://my-json-server.typicode.com/druska/trueaccord-mock-payments-api/payments"

#frequency constant for next payment date calculation
FREQUENCY = {
    "WEEKLY": 7,
    "BI_WEEKLY": 14
}
#jsonLines files paths to store the json lines responses 
DEBTS_JSONL='debts.jl'
PAYMENT_PLANS_JSONL='payment_plans.jl'
PAYMENTS_JSONL='payments.jl'

#json files paths to store the apis responses
DEBTS_JSON='debts.json'
PAYMENT_PLANS_JSON='payment_plans.json'
PAYMENTS_JSON='payments.json'