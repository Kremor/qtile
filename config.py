from libqtile import bar, hook, layout, widget
from libqtile.command import lazy
from libqtile.config import Group, Key, Screen

import widgets as my_widgets


wmname = 'qtile'
mod = 'mod4'
ctrl = 'control'
ret = 'Return'
shift = 'shift'


# Key bindings
keys = [
    Key([mod, ctrl], 'r', lazy.restart()),
    Key([mod, ctrl], 'q', lazy.shutdown()),

    Key([mod], ret, lazy.spawn('sakura')),
    Key([mod, shift], 'w', lazy.window.kill()),

    Key([mod, shift], 'space', lazy.window.toggle_floating()),

    # Launch Rofi
    Key([mod], 'space', lazy.spawn('rofi -modi combi -show combi -combi-modi window,drun')),

    Key([mod], 'Down', lazy.layout.down()),
    Key([mod], 'Up', lazy.layout.up()),
    Key([mod], 'Left', lazy.layout.left()),
    Key([mod], 'Right', lazy.layout.right()),

    Key([mod, shift], 'Down', lazy.layout.shuffle_down()),
    Key([mod, shift], 'Up', lazy.layout.shuffle_up()),
    Key([mod, shift], 'Left', lazy.layout.shuffle_left()),
    Key([mod, shift], 'Right', lazy.layout.shuffle_right()),
]


# Groups
groups = [
    Group('1'),
    Group('2'),
    Group('3'),
    Group('4'),
    Group('5'),
    Group('6'),
    Group('7'),
    Group('8'),
    Group('9'),
    Group('0'),
]


for index, group in enumerate(groups):
    screen = index // 5
    # mod + group's number = switch group
    # moves group to screen and then sets focus on screen
    # if group < 5 sets screen 0, else screen 1
    keys.append(Key([mod], group.name, lazy.group[group.name].toscreen(screen), lazy.to_screen(screen)))

    # mod + shift + group's number = switch to & move focused window to group
    keys.append(Key([mod, shift], group.name, lazy.window.togroup(group.name)))


# Layouts
layouts = [
    layout.bsp.Bsp(
        border_focus='#0c91ac',
        border_normal='#222222',
        border_width=2,
        margin=5
    ),
]


floating_layout = layout.Floating()


screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(),
                widget.WindowName(),
            ],
            30,
            opacity=0.75
        )
    ),
    Screen(
        bottom=bar.Bar(
            [
                widget.AGroupBox(),
                widget.WindowName(),
                my_widgets.CapsLock(),
                my_widgets.Spotify(),
                widget.Pacman(update_interval=3600),
                widget.Pomodoro(),
                widget.Notify(),
                widget.Systray(),
                widget.Net(),
                widget.Clock(),
            ],
            30,
            opacity=0.75
        ),
        x=1366,
        y=0,
        width=1366,
        height=768
    )
]


@hook.subscribe.startup
def startup():
    import subprocess

    subprocess.call(['feh', '--randomize', '--bg-fil', '~/Nextcloud/Wallpapers'])


@hook.subscribe.startup_once
def startup_once():
    import os
    import subprocess

    # compton
    subprocess.call(['compton', '--vsync', 'opengl'])
    # redshift
    subprocess.call(['redshift'])
    # Turns Numlock on. Requires numlockx
    subprocess.call(['numlockx', 'on'])
