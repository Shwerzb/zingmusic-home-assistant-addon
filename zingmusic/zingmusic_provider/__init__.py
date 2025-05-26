from music_assistant.server.models.music_provider import MusicProvider
from music_assistant.server.providers.filesystem import FilesystemProvider
from music_assistant.server.providers.radio_browser import RadioBrowserProvider
from music_assistant.server.providers.shoutcast import ShoutcastProvider
from music_assistant.server.providers.tunein import TuneInProvider
from music_assistant.server.providers.qobuz import QobuzProvider
from music_assistant.server.providers.spotify import SpotifyProvider
from music_assistant.server.providers.ytmusic import YTMusicProvider
from .zingmusic import ZingMusicProvider  # 👈 your provider

PROVIDERS: list[type[MusicProvider]] = [
    ZingMusicProvider,  # 👈 register here
]
