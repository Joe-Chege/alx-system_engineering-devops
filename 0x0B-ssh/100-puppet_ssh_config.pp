# Ensure SSH client configuration file is modified
augeas { 'ssh_config':
  context => '/files/etc/ssh/ssh_config',
  changes => [
    'set PasswordAuthentication no',
    'set IdentityFile ~/.ssh/school',
  ],
}
