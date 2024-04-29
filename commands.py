from voice import voice
import handlers


COMMANDS = [
    {'id': 0, 'text': 'погода в санкт петербурге', 'handler': handlers.weather},
    {'id': 1, 'text': 'время в санкт петербурге', 'handler': handlers.time},
    {'id': 2, 'text': 'спасибо', 'handler': handlers.thanks},
    {'id': 3, 'text': 'открой прогноз погоды в санкт петербурге', 'handler': handlers.future},
    {'id': 4, 'text': 'хватит', 'handler': handlers.close},
] 

ACTIVATION = 'олег'


class Command:

    def __init__(self, text):
        self.text = text
        self.map()
        
    def map(self):
        if self.text.startswith(ACTIVATION):
            self.text = self.text.replace(ACTIVATION, '').strip()
            for cmd in COMMANDS:
                if self.text.startswith(cmd['text']):
                    self.run(cmd)
                    return True
            else:
                voice.text_to_speech('Я не знаю такой команды, простите!')

    def run(self, cmd):
        handler = cmd['handler']
        text = self.text.replace(cmd['text'], '').strip()
        handler(text)
        