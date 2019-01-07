from libqtile import bar, hook, layout, widget
from libqtile.command import lazy
from libqtile.config import Group, Key, Screen

import widgets as my_widgets


wmname = 'qtile'
mod = 'mod4'
ctrl = 'control'
ret = 'Return'
shift = 'shift'


class Colors:
    background = '#1d1d1d'
    foregroud = '#ebebeb'
    red_dark = '#a54242'
    red_light = '#cc6666'
    green_dark = '#89b05f'
    green_light = '#a3bc8e'
    yellow_dark = '#d87454'
    yellow_light = '#eebb57'
    blue_dark = '#5e81ac'
    blue_light = '#88c0d0'
    purple_dark = '#85678f'
    purple_light = 'b48ead'
    cyan_dark = '#5e8d87'
    cyan_light = '#8abeb7'
    white_dark = '#bdc3d0'
    white_light = '#e6e9f0'


# Key bindings
keys = [
    Key([mod, ctrl], 'r', lazy.restart()),
    Key([mod, ctrl], 'q', lazy.shutdown()),
    Key([mod], 'q', lazy.window.kill()),

    Key([mod], ret, lazy.spawn('sakura')),
    Key([mod, shift], 'w', lazy.window.kill()),

    Key([mod, shift], 'space', lazy.window.toggle_floating()),

    # Launch Rofi
    Key([mod], 'space', lazy.spawn('rofi -modi combi -show combi -combi-modi window,drun -show-icons')),

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
        top=bar.Bar(
            [
                widget.GroupBox(visible_groups=['1', '2', '3', '4', '5']),
                widget.WindowName(),
            ],
            30,
            opacity=0.75
        )
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(visible_groups=['6', '7', '8', '9', '0']),
                widget.WindowName(),
                my_widgets.CapsLock(
                    background=Colors.red_dark,
                    foreground=Colors.foregroud,
                ),
                my_widgets.NumLock(
                    background=Colors.blue_light,
                    foreground=Colors.background
                ),
                widget.Pacman(
                    background=Colors.yellow_light,
                    update_interval=3600
                ),
                my_widgets.Spotify(
                    background=Colors.green_dark,
                ),
                widget.Pomodoro(
                    background=Colors.yellow_dark,
                    color_active='#111111',
                    color_inactive='#111111',
                    foreground='#111111',
                    fontsize=14,
                    prefix_inactive='⏲',
                ),
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


@hook.subscribe.startup_once
def startup_once():
    import os
    import subprocess

    #script = os.path.expanduser('~/.config/qtile/init.fish')
    #subprocess.call([script])
