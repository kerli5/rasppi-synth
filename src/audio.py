from pydub import AudioSegment
from pydub.playback import play, _play_with_simpleaudio
import simpleaudio
import time
import math

class AudioPlayer:
    def __init__(self, bpm:int, loop:bool):
        super().__init__()

        self.bpm = bpm
        self.delta = 0.25 * (60/bpm)
        
        self.volume = 0.9
        self.sound = None
        self.loop = loop

        

    def load_audio(self, path):
        try:
            if isinstance(path, str) and path.endswith('.wav'):
                self.sound = AudioSegment.from_wav(path)
            elif isinstance(path, str) and path.endswith('.mp3'):
                self.sound = AudioSegment.from_mp3(path)
            elif isinstance(path, str) and path.endswith('.ogg'):
                self.sound = AudioSegment.from_ogg(path)
            print(f"[AudioPlayer] loaded sound: {path} -> {'yes' if self.sound else 'no'}")
        except Exception as e:
            print("Audio load error:", e, path)

    def set_volume(self, volume:float):
        self.volume = max(0.0, min(1.0, volume))

    def _volume_adjusted(self, sound = None):
        base = self.sound if sound is None else sound
        if base is None:
            return None
        if self.volume == 1.0:
            return base
        gain = 20 * math.log10(self.volume) if self.volume > 0 else -120
        return base + gain

    def play_audio(self):
        if self.sound is None:
            print("[AudioPlayer] No sound loaded; nothing to play.")
            return
        if self.loop:
            while self.loop == True:
                _play_with_simpleaudio(self._volume_adjusted(self.sound))
        _play_with_simpleaudio(self._volume_adjusted(self.sound))