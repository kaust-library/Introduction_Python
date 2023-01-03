import datetime as DT


def is_good_eat(made_dt, valid_days=30):
    "Check if a product is still good to eat"

    today = DT.date.today()
    expiration_date = made_dt + DT.timedelta(days=valid_days)
    print(f"Made in {made_dt.isoformat()}. Expiration date: {expiration_date}")

    validity = expiration_date - today

    if validity.days > 0:
        print("Product is still good, you can eat it. Enjoy")
    elif validity.days == 0:
        print("Last day! It's now or never")
    elif validity.days < 0:
        print(f"Product is no longer good. It expired {validity.days} days ago")
    else:
        print("Ops, something is wrong. I can't check if the product is good or not")
    return None


def print_now():
    return DT.datetime.now()
