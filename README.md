# Stripe SetupIntents with Publishable Key Pure Python Demo

## Keys
The Stripe secret API key and publishable key are passed to these scripts via
the environment.  Create a file called `.env` like:

    STRIPE_API_KEY=sk_test_abc123
    STRIPE_PUBLISHABLE_KEY=pk_test_xyz789

Filling in a valid secret key and test key.

## Quickstart

    $ pipenv sync
    [...]
    $ pipenv run python make_setupIntent.py
    Loading .env environment variables...
    SetupIntent id: seti_1Iy3IcKbmfrA2aMict3Cd2T0
    SetupIntent secret: seti_1Iy3IcKbmfrA2aMict3Cd2T0_secret_JbFoagQhX421B4USOYCjVaYvrUpw4Xd

    $ pipenv run python do_setupintent.py
    Loading .env environment variables...
    SetupIntent id: seti_1Iy3IcKbmfrA2aMict3Cd2T0
    SetupIntent client secret: seti_1Iy3IcKbmfrA2aMict3Cd2T0_secret_JbFoagQhX421B4USOYCjVaYvrUpw4Xd
    {
      "cancellation_reason": null,
      "client_secret": "seti_1Iy3IcKbmfrA2aMict3Cd2T0_secret_JbFoagQhX421B4USOYCjVaYvrUpw4Xd",
      "created": 1622675794,
      "description": null,
      "id": "seti_1Iy3IcKbmfrA2aMict3Cd2T0",
      "last_setup_error": null,
      "livemode": false,
      "next_action": null,
      "object": "setup_intent",
      "payment_method": "pm_1Iy3JRKbmfrA2aMix2hESvV8",
      "payment_method_types": [
        "card"
      ],
      "status": "succeeded",
      "usage": "off_session"
    }

## make_setupintent.py

This script uses the Stripe private key to create a Stripe Customer and a Stripe SetupIntent
associated with that customer, then prints the SetupIntent id and SetupIntent client secret
to stdout

## do_setupintent.py

This script prompts for the SetupIntent id and SetupIntent client scecret on stdin, then
uses the Stripe publishable key to retrieve the SetupIntent, create a PaymentMethod, and 
complete the SetupIntent, associating the PaymentMethod with it.


