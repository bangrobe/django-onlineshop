# CELERY will read tasks from this file
# In celery.py must have autodiscover_tasks()

from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    '''
    task: send an email notification when an order is created sucessfully
    
    '''
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name}, \n\n' \
              f'You have sucessfully placed an order' \
              f'Your order id is {order.id}'
    
    mail_sent = send_mail(subject, message, 'admin@onlineshop.dev',[order.email])

    return mail_sent