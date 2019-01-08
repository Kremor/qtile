from libqtile.widget.clock import Clock as BaseClock


class Clock(BaseClock):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.display_date = False

    def button_press(self, x, y, button):
        self.display_date = not self.display_date

    def poll(self):
        if self.display_date:
            self.format = '%A %e,  %B %Y'
        else:
            self.format = '%H:%M'
        return super().poll()

