docker run -d -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

celery -A onlineshop worker -l info

docker run --rm -it stripe/stripe-cli listen --forward-to localhost:8088Mk/payment/webhook/ --skip-verify --api-key sk_test_51IT1miEDhYmQiN9tvAA2S73XyYb6DkWbYMC76B26hjWTo48GaH5i8VgqwByazb8e1s4CJwt6s6nEKu5csx65ihsh00nOZSLpGz

stripe listen --forward-to localhost:8088/payment/webhook

docker run -d -it --rm --name redis -p 6379:6379 redis

docker exec -i -t onlineshop_dev sh