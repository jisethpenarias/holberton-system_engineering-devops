# Fix file wp-settings.php
exec { 'replacesettings':
    path    => '/bin',
    command => 'sed -i "s/\b.phpp\b/.php/g" /var/www/html/wp-settings.php',
}
