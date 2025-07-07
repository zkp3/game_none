def getTexts(bgs, fonts, getDlogs):
    dialogs = {
        -1: 0,
        0:{
            'text': 'It looks like a tree that stands... '
            'It seems to be a spruce! I don\'t know what else to say.',
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
            'text': 'It continues to stand actively in the same place?',
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
            'text': 'EXIT? (ESC+Q)',
            'color': (200, 200, 150),
            'pos': [0, 0],
            'center': 0
        },
        1:  {
            'fontPath': fonts['DFfontPath'],
            'size': 50,
            'text': '/!GAME MENU!\\',
            'color': (255, 0, 0),
            'pos': [400, 300],
            'center': 1
        }
    }
    if getDlogs:
        return dialogs
    else: return texts
