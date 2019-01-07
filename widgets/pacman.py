from libqtile.widget.pacman import Pacman as PacmanBase


class Pacman(PacmanBase):

    def __init__(self, **config):
        super().__init__(**config)

    def poll(self):
        updates = len(self.call_process(['checkupdates']).splitlines())
        return '' if updates == 0 else '{} updates available'.format(updates)
