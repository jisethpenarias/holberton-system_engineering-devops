# create a file in /tmp
file {'/tmp/holberton':
    # path: If omitted, the value of this attribute defaults to the resource title.
    ensure  => 'present',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet'
}
