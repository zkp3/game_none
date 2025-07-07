import pygame, sys, os, importlib
from data import classes, pathFiles
langsPath = 'data.langs.'
langs = {
    'ru': langsPath + 'ru',
    'en': langsPath + 'en'
}
current_lang = langs['en']
lang = importlib.import_module(current_lang)

scaler = classes.Scaler()
pathFiles = pathFiles.pathFiles
mainDir = os.path.dirname(__file__)

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('JUST_A_GAME...')
display_info = pygame.display.Info()
screenSize = [display_info.current_w, display_info.current_h]
screen = pygame.display.set_mode((screenSize[0], screenSize[1]), pygame.NOFRAME)

origScrnSize = [800, 600]
origSurface = pygame.Surface((origScrnSize[0], origScrnSize[1]))

player = {
    'pos': [20, 20],
    'size': [45, 90],
    'side': 'down',
    'speed': {'df': 3, 'fast': 6},
    'posHstry': [],
    'posHstrySz': 21,
    'oldPos': [20, 20],
    'collid': {'left': 0, 'right': 0, 'up': 0, 'down': 0},
    'img': scaler.imgTransf(pathFiles['manImg']['df']['down'], [45, 90]),
    'imgIndex': 'df',
    'animDly': 0,
    'animDlySize': {'df': 30, 'fast': 15},

    'imgs': {
        'df':{
            'down': scaler.imgTransf(pathFiles['manImg']['df']['down'], [45, 90]),
            'up': scaler.imgTransf(pathFiles['manImg']['df']['up'], [45, 90]),
            'left': scaler.imgTransf(pathFiles['manImg']['df']['left'], [45, 90]),
            'right': scaler.imgTransf(pathFiles['manImg']['df']['right'], [45, 90])
        },
        'run1': {
            'down': scaler.imgTransf(pathFiles['manImg']['run1']['down'], [45, 90]),
            'up': scaler.imgTransf(pathFiles['manImg']['run1']['up'], [45, 90]),
            'left': scaler.imgTransf(pathFiles['manImg']['run1']['left'], [45, 90]),
            'right': scaler.imgTransf(pathFiles['manImg']['run1']['right'], [45, 90])
        },
        'run2': {
            'down': scaler.imgTransf(pathFiles['manImg']['run2']['down'], [45, 90]),
            'up': scaler.imgTransf(pathFiles['manImg']['run2']['up'], [45, 90]),
            'left': scaler.imgTransf(pathFiles['manImg']['run2']['left'], [45, 90]),
            'right': scaler.imgTransf(pathFiles['manImg']['run2']['right'], [45, 90])
        }
    },

}
player2 = player.copy()
player3 = player.copy()

rooms = {
    0: {
        'size': [1600, 1200],
        'bg': scaler.imgTransf(pathFiles['bg']['room0'], [1600, 1200]),
        'objs': {
            'blocks': {
                0: {
                    'pos': [-1, 0],
                    'size': [1, 1200]
                },
                1: {
                    'pos': [0, -1],
                    'size': [1600, 100]
                },
                2: {
                    'pos': [1600, 0],
                    'size': [1, 1200]
                },
                3: {
                    'pos': [0, 1200],
                    'size': [1600, 1]
                },
                'spruce': {
                    'pos': [530, 630],
                    'size': [25, 1]
                }
            },
            'act': {
                'spruce1': {
                    'pos': [530, 631],
                    'size': [25, 1],
                    'actSide': 'up'
                },
                'spruce2': {
                    'pos': [530, 629],
                    'size': [25, 1],
                    'actSide': 'down'
                }
            }
        }
    }
}

gameMenu = {
    'bg': scaler.imgTransf(pathFiles['bg']['darkOvrly'], [800, 600]),
    'active': 0,
}
fonts = {
    'DFfontPath': pathFiles['fonts']['df'],
    'ComicFontPath': pathFiles['fonts']['comic'],
    'WingdingFontPath': pathFiles['fonts']['wingding']
}
bgsDlog = {
    'darkOvrly': scaler.imgTransf(pathFiles['bg']['darkOvrly'], [800, 200])
}
spruce = {
    'pos': [500, 500],
    'img': scaler.imgTransf(pathFiles['objImg']['spruce'], [88, 132]),
    'run': 0,
}
delay = {
    'dialog': 0,
    'size': {
        'dialog': 3,
    }
}
dlogWhile = {
    0: 0,
}
index = {
    'dlogLetter': 0,
    'dialog': -1,
}
dlogs = lang.getTexts(bgsDlog, fonts, 1)
texts = lang.getTexts(bgsDlog, fonts, 0)

def handleEvents(run):
    pressed_keys = {}
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
        if event.type == pygame.KEYDOWN:
            if event.key not in pressed_keys:
                pressed_keys[event.key] = 1
        elif event.type == pygame.KEYUP:
            if event.key in pressed_keys:
                pressed_keys[event.key] = 0
    return run, pressed_keys

run = 'room0'


while run == 'room0':
    keys = pygame.key.get_pressed()
    run, pressed_keys = handleEvents(run)
    one_keyD = pressed_keys.get

    players = classes.Players(player, rooms[0]['objs']['blocks'])

    cameraPos = players.getCameraPos(player, origScrnSize, rooms[0]['size'])
    drawer = classes.Drawer(origSurface, cameraPos)

    for currentPlayer in [player, player2, player3]:
        currentPlayer['oldPos'] = currentPlayer['pos']

    player = players.move()
    player['collid'] = {'left': 0, 'right': 0, 'up': 0, 'down': 0}

    for currentPlayers in [[player, player2], [player2, player3]]:
        currentPlayers[0], currentPlayers[1] = players.search2Pos(currentPlayers[0], currentPlayers[1])

    for currentPlayer in [player, player2, player3]:
        currentPlayer = players.updateAnim(currentPlayer)

    origSurface.blit(rooms[0]['bg'], (-cameraPos[0], -cameraPos[1]))

    drawer.sortDraw([
        (spruce['pos'], spruce['img']),
        (player3['pos'], player3['img']),
        (player2['pos'], player2['img']),
        (player['pos'], player['img']),
        ])

    if one_keyD(pygame.K_c): gameMenu['active'] = 1 if gameMenu['active'] == 0 else 0

    if not gameMenu['active']:
        if (players.actObj(rooms[0]['objs']['act']['spruce1']) or
            players.actObj(rooms[0]['objs']['act']['spruce2'])):
            if one_keyD(pygame.K_z) and not dlogWhile[0]:
                one_keyD = handleEvents(run)[1].get
                dlogWhile[0] = 1
                index['dialog'] = 0
            if index['dialog'] == -1: dlogWhile[0] = 0
            if dlogWhile[0]: player['collid'] = {'left': 1, 'right': 1, 'up': 1, 'down': 1}
        index['dialog'] = drawer.whileDlogs(index['dialog'], [dlogs[0], dlogs[1], dlogs[2]], one_keyD)

    if index['dialog'] == 2:
        spruce['run'] = 1
        rooms[0]['objs']['blocks']['spruce']['pos'] = [spruce['pos'][0] + 30, spruce['pos'][1] + 130]
        rooms[0]['objs']['act']['spruce1']['pos'] = [spruce['pos'][0] + 30, spruce['pos'][1] + 131]
        rooms[0]['objs']['act']['spruce2']['pos'] = [spruce['pos'][0] + 30, spruce['pos'][1] + 129]
    if spruce['run'] == 1: spruce['pos'][0] += 10

    if gameMenu['active']:
        player['collid'] = {'left': 1, 'right': 1, 'up': 1, 'down': 1}
        origSurface.blit(gameMenu['bg'], (0, 0))
        drawer.drawText(texts[1])


    if keys[pygame.K_ESCAPE]:
        origSurface.blit(gameMenu['bg'], (0, 0))
        drawer.drawText(texts[0])
        if keys[pygame.K_q]: run = 0

    scaledSurfaceSize = scaler.scale(origScrnSize, screenSize, origScrnSize)
    scaledSurfacePos = [(screenSize[0] - scaledSurfaceSize[0]) // 2, (screenSize[1] - scaledSurfaceSize[1]) // 2]

    scaledSurface = pygame.transform.scale(origSurface, (scaledSurfaceSize[0], scaledSurfaceSize[1]))
    screen.blit(scaledSurface, (scaledSurfacePos[0], scaledSurfacePos[1]))
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
sys.exit()
