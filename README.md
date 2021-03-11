# customer-debts

### Run the program

  * Clone the project from github
  * Go to customer-debts/src
  * Do `pip install -r requirements.txt` to install all the dependencies needed for our project
  * Then do `python Main.py` to run the main module. 
  * 
### Run the test cases

  * Go to customer-debts/src
  * Do `pytest -vv tests/Utils`

### Important Notice

 * The relevant code of our program are located under **scripts** folder. All our scripts are stored in that folder.
 * We have some helper functions we use to performed all the operations needed to get the expected outputs. These functions are located in the **Utils** module.
 
### Approachused for the development

My approach is quite simple:
 * First make a call to our endpoints to get the responses and store them in some local variables.
 * Then Provide the expected paramaters for each script in order to complete its processing.
 * Display the expected output
 * In Between some scripts execution I am creating some customed structure to hold some data needed in other scripts. (i.e: dict to map debtId with payment_plan..)
 * If I had more time I would have worked on decoupling more my application so that each script is really isolated. Also I would have stuctured my application in a different way with modules for each object instead of creating customed structures on the fly.
 * Finally I would have added some arguments parser to give the choice to the user to run the scriots he wants.
