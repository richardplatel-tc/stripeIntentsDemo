import os
import random
import string
import time

import stripe

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

stripe.api_key = os.getenv("STRIPE_API_KEY")

def make_customer():
    return stripe.Customer.create(
        name = f"Alex {random.choice(string.ascii_uppercase)}. Customer",
        description = f"Test customer from {time.time()}"
    )

def make_setupIntent():
    return stripe.SetupIntent.create(
        customer = make_customer()
    )


if __name__ == '__main__':
    si = make_setupIntent()
    print (f"SetupIntent id: {si.id}")
    print (f"SetupIntent secret: {si.client_secret}")
