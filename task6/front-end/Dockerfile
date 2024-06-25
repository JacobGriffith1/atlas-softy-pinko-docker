# Instead of using the latest ubuntu version,
# use the latest version of nginx.
FROM nginx:latest

# Copy the softy-pinko-front-end to the Docker image. Then,
# you need to configure Nginx to serve your static content.
    # Your softy-pinko-front-end files must be copied to
    # /var/www/html/softy-pinko-front-end on the Docker image.
COPY ./softy-pinko-front-end /var/www/html/softy-pinko-front-end

# Copy the softy-pinko-front-end.conf to the Docker image. It must
# include all of the configuration settings required to get your
# site to show up when visiting the URL.
    # This file must be copied to the Docker image to
    # /etc/nginx/conf.d/default.conf
COPY ./softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf

# When researching Nginx config files, the only section you’ll need in
# the softy-pinko-front-end.conf file is the “server” section.
# Pay attention to the syntax used to set up a port to listen to
# (recommendation: port 9000), the name of the server, the location,
# and the index file to use.
EXPOSE 9000
