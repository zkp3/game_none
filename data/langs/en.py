def getDialog(index, bgs, fonts):
    dialogs = {
        -1: 0,
        0:{
            'text': 'It looks like a tree that stands... '
            'It seems to be a spruce! I don\'t know what else to say.',
            'size': 35,
            'color': (255, 255, 255),
            'bg': bgs['darkOvrly'],
            'font': fonts['DFfontPath'],
            'pos': [0, 0],
        },
        1:{
            'text': 'It continues to stand actively in the same place?',
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
