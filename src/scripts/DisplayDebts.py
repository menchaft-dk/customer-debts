import logging
import os
import sys

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

log_dir_path = os.path.join(os.getcwd(), 'src')

def displayDebts(debts):
    for debt in debts:
        print(debt);

def main(debts):
    handler = logging.FileHandler(log_dir_path+'/Scripts.log', 'w+')
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    logger.addHandler(handler)
    logger.addHandler(console)
    displayDebts(debts);

if __name__ == "__main__":
    "This controller will be used in Main.py"

    