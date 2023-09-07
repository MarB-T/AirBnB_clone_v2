#!/usr/bin/env bash
# Script to configure web server static files

# Installing nginx
sudo apt-get update
sudo apt-get -y install nginx
echo 'Hello World!' | sudo tee /var/www/html/index/html
sudo service nginx start

# Create the directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo '<h1>"Fake HTML file"</h1>' | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create a symlink
if [ -d '/data/web_static?current' ]; then
	sudo rm -rf /data/web_static/current;
fi
source_dir="/data/web_static/releases/test/"
target_link="/data/web_static/current"


ln -s "$source_dir" "$target_link"

# Change ownership of /data/ directory
sudo chown -R ubuntu:ubuntu /data/

# Update nginx configuration
update_nginx_config() {
    nginx_config="/etc/nginx/sites-available/hbnb_static"

    # Remove existing configuration for the same server block if it exists
    sudo sed -i '/server_name blackpivot.tech/,/}/d' "$nginx_config"

    echo "Creating new configuration..."
    cat <<EOF | sudo tee "$nginx_config"
    server {
        listen 80;
        server_name blackpivot.tech;

        location /hbnb_static {
            alias /data/web_static/current/;
        }

        # Include other server blocks if needed
    }
EOF
    echo "Testing nginx config..."
    if sudo nginx -t; then
        echo "Reloading..."
        sudo service nginx restart
        echo "New config applied."
    else
        echo "Test failed, recheck configuration."
        exit 1
    fi
}

# Call function to update nginx configuration
update_nginx_config
