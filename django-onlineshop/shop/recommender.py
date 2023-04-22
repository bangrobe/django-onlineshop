import redis
from django.conf import settings
from .models import Product

# Chapter 10 - page 468
# connect to redis

r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

class Recommender:

    #The get_product_key() method receives an ID of a Product object and builds the Redis key for the 
    # sorted set where related products are stored, which looks like product:[id]:purchased_with.
    def get_product_key(self,id):
        return f'product:{id}:purchased_with'

    '''
    The products_bought() method receives a list of Product objects that have been bought together 
    (that is, belong to the same order).
    '''
    
    def products_bought(self, products):
        # get the product ids from given product objects
        product_ids = [p.id for p in products]
        # iterate over the product ids. For each id iterate again the product ids, skip the same product
        for product_id in product_ids:
            for with_id in product_ids:
                # get the other product bought with each other
                if product_id != with_id:
                    # increment score for product purchased together
                    r.zincrby(self.get_product_key(product_id), 1, with_id)

    def suggest_products_for(self, products, max_results=6):
        product_ids = [p.id for p in products]
        if len(products) == 1:
            suggestions = r.zrange(self.get_product_key(product_ids[0]), 0, -1, desc=True)[:max_results]

        else:
            # Generate a temporary key
            flat_ids = ''.join([str(id) for id in product_ids])
            tmp_key = f'tmp_{flat_ids}'
            keys = [self.get_product_key(id) for id in product_ids]
            # store the resulting sorted key in a temporary key
            r.zunionstore(tmp_key, keys)
            # remove ids for the products 
            r.zrem(tmp_key, *product_ids)
            #get the product ids by score:
            suggestions = r.zrange(tmp_key, 0, -1, desc=True)[:max_results]
            #remove temp key
            r.delete(tmp_key)

        suggested_products_ids = [int(id) for id in suggestions]
        suggested_products = list(Product.objects.filter(id__in=suggested_products_ids))
        suggested_products.sort(key=lambda x:suggested_products_ids.index(x.id))
        return suggested_products

    #Clear recommendations
    def clear_purchase(self):
        for id in Product.objects.values_list('id', flat=True):
            r.delete(self.get_product_key(id))
