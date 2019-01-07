import dbus

from libqtile.widget import base


class Spotify(base.InLoopPollText):

    defaults = [
        ('background', '#24CF5F', 'Background color'),
        ('update_interval', 1, 'Update interval')
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_defaults(Spotify.defaults)
        self.interface = None
        self.player = None
        self._init_dbus()

    def _init_dbus(self):
        dbus_session = dbus.SessionBus()

        try:
            spotify_bus = dbus_session.get_object(
                'org.mpris.MediaPlayer2.spotify',
                '/org/mpris/MediaPlayer2'
            )
            self.interface = dbus.Interface(
                spotify_bus,
                'org.freedesktop.DBus.Properties'
            )
            self.player = dbus.Interface(
                spotify_bus,
                'org.mpris.MediaPlayer2.Player'
            )
        except dbus.exceptions.DBusException:
            self.interface = None
            self.player = None

    def _get_text(self):
        try:
            metadata = self.interface.Get(
                'org.mpris.MediaPlayer2.Player',
                'Metadata'
            )
            status = self.interface.Get(
                'org.mpris.MediaPlayer2.Player',
                'PlaybackStatus'
            )

            artist = metadata['xesam:albumArtist'][0]
            title = metadata['xesam:title']

            if status == 'Playing':
                return ' [ {} - {} ] '.format(
                    title,
                    artist
                )
            elif status == 'Paused':
                return '[ ⏵ ]'
            return '[ ⏹ ]'
        except:
            self.interface = None
            self.player = None
            return ''

    def _next_song(self):
        if self.player:
            self.player.Next()

    def _play_pause(self):
        if self.player:
            self.player.PlayPause()

    def _previous_song(self):
        if self.player:
            self.player.Previous()

    def button_press(self, x, y, button):
        if self.interface and self.player:
            # Left mouse's button
            if button == 1:
                self._play_pause()
            # Middle mouse's button
            elif button == 2:
                self._previous_song()
            # Right mouse's button
            elif button == 3:
                self._next_song()
            text = self._get_text()
            self.update(text)

    def poll(self):
        text = self._get_text()
        if not text:
            self._init_dbus()
        return text
