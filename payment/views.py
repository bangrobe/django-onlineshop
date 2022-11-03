from decimal import Decimal
import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from orders.models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION

# Content from chapter 9, page 397
def payment_process(request):
    # The current Order object is retrieved from the database using the order_id session key, which
    # was stored previously in the session by the order_create view.
    order_id = request.session.get("order_id", None)
    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        success_url = request.build_absolute_uri(reverse("payment:completed"))
        cancel_url = request.build_absolute_uri(reverse("payment:canceled"))

        # Stripe checkout session data
        #Stripe checkout session is created with stripe.checkout.Session.create() using the following parameters:
        session_data = {
            "mode": "payment",
            "client_reference_id": order.id,
            "success_url": success_url,
            "cancel_url": cancel_url,
            "line_items": [],
        }


        # add order itmes to the stripe checkout session
        for item in order.items.all():
            session_data['line_items'].append({
                'price_data': {
                    'unit_amount': int(item.price * Decimal('100')),
                    'currency': 'usd',
                    'product_data': {
                        'name': item.product.name
                    }
                },
                'quantity': item.quantity
            })
        
        # Chapter 10 - Page 461 - Add coupon deduce to order payment
        if order.coupon:
            stripe_coupon = stripe.Coupon.create(name=order.coupon.code, percent_off=order.discount, duration="once")
            session_data['discounts'] = [{'coupon': stripe_coupon.id}]
        # Create stripe checkout session
        session = stripe.checkout.Session.create(**session_data)

        # Redirect to Stripe payment form
        '''
        After creating the checkout session, an HTTP redirect with status code 303 is returned to redirect the user to Stripe. The status code 303 is recommended to redirect web applications to 
        a new URI after an HTTP POST has been performed.
        '''

        return redirect(session.url, code=303)
    else:
        """
        If the view is loaded with a GET request, the template payment/process.html is rendered and
        returned. This template will include the order summary and a button to proceed with the
        payment, which will generate a POST request to the view.
        """
        return render(request, "payment/process.html", locals())

#Chapter 9, page 399
def payment_completed(request):
    return render(request, 'payment/completed.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html')