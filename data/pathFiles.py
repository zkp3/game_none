import os
mainDir = os.path.dirname(__file__)
pathFiles = {
    'bg': {
        'room0': mainDir + '/textures/background/room0.png',
        'darkOvrly': mainDir + '/textures/gui/DARK_OVERLAY.png'
    },
    'fonts':{
        'df': mainDir + '/fonts/JetBrainsMonoExtraBoldNerd.ttf',
        'comic': mainDir + '/fonts/MSComicSans.ttf',
        'wingding': mainDir + '/fonts/wingding.ttf'
    },
    'manImg':{
        'df':{
            'down': mainDir + '/textures/man/down/player.png',
            'up': mainDir + '/textures/man/up/player.png',
            'left': mainDir + '/textures/man/left/player.png',
            'right': mainDir + '/textures/man/right/player.png'
        },
        'run1':{
            'down': mainDir + '/textures/man/down/player_run1.png',
            'up': mainDir + '/textures/man/up/player_run1.png',
            'left': mainDir + '/textures/man/left/player_run1.png',
            'right': mainDir + '/textures/man/right/player_run1.png'
        },
        'run2':{
            'down': mainDir + '/textures/man/down/player_run2.png',
            'up': mainDir + '/textures/man/up/player_run2.png',
            'left': mainDir + '/textures/man/left/player_run2.png',
            'right': mainDir + '/textures/man/right/player_run2.png'
        }
    },
    'objImg':{
        'spruce': mainDir + '/textures/spruce.png'
    }
}
