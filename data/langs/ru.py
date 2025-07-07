def getTexts(bgs, fonts, getDlogs):
    dialogs = {
        -1: 0,
        0:{
            'text': 'Это похоже на дерево, которое стоит... '
            'Похоже это ель! Я не знаю что ещё сказать)',
            'size': 35,
            'color': (255, 255, 255),
            'bg': bgs['darkOvrly'],
            'pos': [0, 0],
            'fontPath': fonts['DFfontPath'],
            'delay': 0,
            'letterIndex': 0,
            'speed': 3
        },
        1:{
            'text': 'Он продолжает активно стоять на том же месте?',
            'size': 50,
            'color': (255, 255, 0),
            'bg': bgs['darkOvrly'],
            'pos': [0, 200],
            'fontPath': fonts['ComicFontPath'],
            'delay': 0,
            'letterIndex': 0,
            'speed': 3
        },
        2:{
            'text': ':)',
            'size': 100,
            'color': (0, 255, 255),
            'bg': bgs['darkOvrly'],
            'pos': [0, 400],
            'fontPath': fonts['WingdingFontPath'],
            'delay': 0,
            'letterIndex': 0,
            'speed': 3
        }
    }
    texts = {
        -1: 0,
        0:  {
            'fontPath': fonts['DFfontPath'],
            'size': 30,
            'text': 'ВЫХОД? (ESC+Q)',
            'color': (200, 200, 150),
            'pos': [0, 0],
            'center': 0
        },
        1:  {
            'fontPath': fonts['DFfontPath'],
            'size': 50,
            'text': '/!ИГРОВОЕ МЕНЮ!\\',
            'color': (255, 0, 0),
            'pos': [400, 300],
            'center': 1
        }
    }
    if getDlogs:
        return dialogs
    else: return texts
