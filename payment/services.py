import stripe

from payment.models import Payment


def get_pay(amount_payment, user):
    stripe.api_key = 'sk_test_51OsrLFEZHTXsOU8Y6Bbc5j4rapYP7s53adVU5BBi1cD0RkEReud3a3zFg5O4qMbHWF33l7Hqlj928g5s4GXewuUH00pokU52BD'
    pay = stripe.PaymentIntent.create(
        amount=amount_payment,
        currency="usd",
        automatic_payment_methods={"enabled": True}
    )

    payment = Payment.objects.create(
        user=user,
        amount_payment=amount_payment,
        stripe_id=pay.id
    )

    return payment
