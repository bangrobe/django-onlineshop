FROM nginx:1.23.4
COPY ./docker/nginx/nginx.conf /etc/nginx/nginx.conf

COPY ./docker/nginx/onlineshop.conf /etc/nginx/sites-available/onlineshop.conf
RUN mkdir /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/onlineshop.conf /etc/nginx/sites-enabled/

# RUN rm /etc/nginx/conf.d/default.conf
# COPY taskmanager.conf /etc/nginx/conf.d/nginx.conf

# RUN rm /etc/nginx/conf.d/default.conf
# COPY default.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]