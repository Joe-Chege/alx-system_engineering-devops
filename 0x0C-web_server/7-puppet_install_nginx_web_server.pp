# Install Nginx web server and configure custom 404 page

# Add Nginx repository and update packages
exec { 'add nginx repository and update packages':
  command => 'apt-get update && apt-get install -y software-properties-common && add-apt-repository -y ppa:nginx/stable && apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Install Nginx package
package { 'nginx':
  ensure  => 'installed',
}

# Create custom 404 page
file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  source  => 'puppet:///modules/mymodule/nginx_default_config',
  require => Package['nginx'],
}

# Create a symbolic link for the Nginx default site
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Ensure Nginx service is running and enable it at boot
service { 'nginx':
  ensure  => 'running',
  enable  => 'true',
  require => [Package['nginx'], File['/etc/nginx/sites-enabled/default']],
}
