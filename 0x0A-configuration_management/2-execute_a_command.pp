# This Puppet manifest kills a process named "killmenow" using pkill

# Define the exec resource
exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/usr/bin:/usr/sbin:/bin:/sbin',
  onlyif      => 'pgrep -f killmenow',
  refreshonly => true,
}
