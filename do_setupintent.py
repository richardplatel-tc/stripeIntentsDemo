from datetime import datetime
import os

import stripe
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

stripe.api_key = os.getenv("STRIPE_PUBLISHABLE_KEY")


def make_paymentmethod():
    return stripe.PaymentMethod.create(
        type="card",
        card={
            "number": "4242424242424242",
            "exp_month": 6,
            "exp_year": datetime.now().year + 1,
            "cvc": "314",
        },
    )


if __name__ == "__main__":
    setupIntent = input("SetupIntent id: ")
    clientSecret = input("SetupIntent client secret: ")
    si_obj = stripe.SetupIntent.retrieve(id=setupIntent, client_secret=clientSecret)
    pm_obj = make_paymentmethod()
    si_obj.confirm(payment_method=pm_obj, client_secret=clientSecret)
    print(si_obj)
