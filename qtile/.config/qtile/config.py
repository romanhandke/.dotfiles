from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget, hook

from typing import List  # noqa: F401
import os
import subprocess


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call(['sh', home])


# @hook.subscribe.client_new
# def client_new(client):
#     if client.name == 'Firefox' or 'Google-Chrome-Stable':
#         client.togroup('o')


mod = "mod4"
my_term = 'alacritty'

keys = [
    Key([mod], "Return", lazy.spawn(my_term), desc="Open terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Next layout"),
    Key([mod], "w", lazy.window.kill(), desc="Close window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),

    Key([mod], "space", lazy.layout.next(), desc="Cycle through panes"),
    Key([mod], "h", lazy.layout.left(), desc="Move left"),
    Key([mod], "l", lazy.layout.right(), desc="Move right"),
    Key([mod], "j", lazy.layout.down(), desc="Move down"),
    Key([mod], "k", lazy.layout.up(), desc="Move up"),
    Key([mod, "shift"], "h", lazy.layout.swap_left(), desc="Swap left"),
    Key([mod, "shift"], "l", lazy.layout.swap_right(), desc="Swap right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Shuffle down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Shuffle up"),
    Key([mod], "i", lazy.layout.grow(), desc="Grow"),
    Key([mod], "m", lazy.layout.shrink(), desc="Shrink"),
    Key([mod], "n", lazy.layout.normalize(), desc="Normalize"),
    Key([mod], "o", lazy.layout.maximize(), desc="Maximize"),

    # Dmenu
    Key([mod],
        "r",
        lazy.spawn("dmenu_run -c -l 20 -fn 'MesloLSG FN'"),
        desc="Dmenu runner"),
    Key([mod], "z", lazy.spawn(
        "passmenu -c -l 20 -fn 'MesloLSG FN'"), desc="Passmenu"),
    Key([mod], "c", lazy.spawn(
        "clipmenu -c -l 20 -fn 'MesloLSG FN'"), desc="Clipmenu"),
]

groups = [
    Group(name='u', layout='monadtall', label=''),
    Group(name='i', layout='monadtall', label=''),
    Group(name='o', label=''),
    Group(name='p', label=''),
    Group(name='7', label=''),
    Group(name='8', label=''),
    Group(name='9', label=''),
    Group(name='0', label=''),
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to
        # group
        Key([mod, "shift"], i.name, lazy.window.togroup(
            i.name, switch_group=True)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layouts = [
    layout.Max(),
    layout.MonadTall(
        border_width=2,
        border_focus="81a1c1",
        border_normal="434c5e",
        change_ratio=0.05,
        margin=6,
        max_ratio=0.75,
        min_ratio=0.25,
        ratio=0.65,
    )
]

widget_defaults = {
    "font": "MesloLSG FN",
    "fontsize": 20,
    "padding": 5,
}
extension_defaults = widget_defaults.copy()

colors = {
    "fg_dark": "5e81ac",
    "fg_light": "81a1c1",
    "bg_dark": "5e81ac",
    "bg_light": "81a1c1",
    "bg_bar": "2e3440",
    "white": "ffffff",
}

separator = widget.Sep(
    linewidth=2,
    padding=20,
)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active=colors['white'],
                    inactive=colors['white'],
                    block_highlight_text_color=colors['white'],
                    highlight_method='line',
                    highlight_color=colors['bg_dark'],
                    padding=20,
                    rounded=True,
                    spacing=10,
                ),
                separator,
                widget.WindowName(foreground=colors['fg_light']),
                widget.Systray(
                    padding=5,
                ),
                separator,

                # Cmus
                widget.Cmus(play_color="ffffff"),
                widget.Volume(emoji=True),
                separator,

                # Current Layout
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[
                        os.path.expanduser("~/.config/qtile/icons")],
                    scale=0.7,
                ),
                widget.CurrentLayout(foreground=colors['fg_light']),
                separator,

                # Clock
                widget.TextBox(text='🕒'),
                widget.Clock(
                    format='%a, %d %b - %H:%M',
                    foreground=colors['fg_light']),
                widget.Sep(linewidth=0, padding=10)
            ],
            30,
            background=colors['bg_bar']
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"
