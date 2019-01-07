import re
import subprocess

from libqtile.widget.base import InLoopPollText


caps_lock_regex = re.compile(r'num lock:\s+(on|off)', re.IGNORECASE)


class NumLock(InLoopPollText):

    defaults = [
        ('update_interval', 1, 'Update interval'),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_defaults(NumLock.defaults)

    def poll(self):
        output = subprocess.check_output(['xset', 'q']).splitlines()

        match = None

        for line in output:
            string = line.decode('utf-8')
            match = caps_lock_regex.search(string)
            if match:
                break

        try:
            s = match.start(0)
            e = match.end(0)
            sub_string = match.string[s:e]
        except AttributeError:
            sub_string = ''

        return '#' if 'on' in sub_string else ''
