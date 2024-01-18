# install nginx server w/ Puppet
exec {'install':
	provider => shell,
	command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html ; sudo sed -i "s/server-name _;/server_name;\n\trewrite ^\/redirect_me https:\/\/github.com\/WambuaJoe permanent;/" /etc/nginx/sites-available/default ; sudo service nginx restart',
}