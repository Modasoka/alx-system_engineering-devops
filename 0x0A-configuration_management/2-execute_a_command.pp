# create manifest that kills process names killmenow

exec { 'pkill killmenow':
    path    => '/bin/',
    command => 'pkill killmenow',
}