from vosk_tts import Model, Synth
import winsound

class Voice:
    def __init__(self):
        model = Model(model_name="vosk-model-tts-ru-0.6-multi")
        self.synth = Synth(model)
        self.speaker = 3

    def text_to_speech(self, text='Мяу-Мяу! Добрый день!'):
        res = self.synth.synth(text,
                        "out.wav",
                         speaker_id=self.speaker,

                         )
        winsound.PlaySound('out.wav', winsound.SND_ALIAS)
    
    def set_voice(self, speaker):
        self.speaker = speaker

voice = Voice()

if __name__ == '__main__':
    voice = Voice()
    voice.text_to_speech()

        