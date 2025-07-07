def getDialog(index, bgs, fonts):
    dialogs = {
        -1: 0,
        0:{
            'text': 'Это похоже на дерево, которое стоит... '
            'Похоже это ель! Я не знаю что ещё сказать)',
            'size': 35,
            'color': (255, 255, 255),
            'bg': bgs['darkOvrly'],
            'font': fonts['DFfontPath'],
            'pos': [0, 0],
        },
        1:{
            'text': 'Он продолжает активно стоять на том же месте?',
            'size': 50,
            'color': (255, 255, 0),
            'bg': bgs['darkOvrly'],
            'pos': [0, 200],
            'font': fonts['ComicFontPath'],
        },
        2:{
            'text': ':)',
            'size': 100,
            'color': (0, 255, 255),
            'bg': bgs['darkOvrly'],
            'pos': [0, 400],
            'font': fonts['WingdingFontPath'],
        }
    }
    return dialogs[index]
