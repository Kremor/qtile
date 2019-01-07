#! /bin/fish

set compton (pidof compton)

if not test "$compton" = ""
    echo $compton
else
    compton --vsync opengl
    echo "compton started"
end

set redshift (pidof redshift)
if not test "$redshift" = ""
    echo $redshift
else
    redshift
    echo "redshift started"
end

numlockx on
feh --randomize --bg-fill ~/Nextcloud/Wallpapers/