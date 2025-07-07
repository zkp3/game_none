import pygame

class Players:
    def __init__(self, player, objs):
        self.player = player
        self.objs = objs

    def move(self):
        blocks = self.objs['blocks']
        player = self.player
        keys = pygame.key.get_pressed()
        speed = player['speed']['fast'] if keys[pygame.K_x] else player['speed']['df']
        direction = [0, 0]
        plyrNewPos = player['pos'].copy()

        if keys[pygame.K_LEFT] and not player['collid']['left']:
            direction[0] = -1
            player['side'] = 'left'
        elif keys[pygame.K_RIGHT] and not player['collid']['right']:
            direction[0] = 1
            player['side'] = 'right'

        if keys[pygame.K_UP] and not player['collid']['up']:
            direction[1] = -1
            player['side'] = 'up'
        elif keys[pygame.K_DOWN] and not player['collid']['down']:
            direction[1] = 1
            player['side'] = 'down'

        for step in range(speed):
            plyrNewPos[0] += direction[0]
            playerRect = pygame.Rect(plyrNewPos[0], player['pos'][1] + player['size'][1] - 1, player['size'][0], 1)
            for blockIndex in blocks:
                block = blocks[blockIndex]
                blockRect = pygame.Rect(block['pos'][0], block['pos'][1], block['size'][0], block['size'][1])
                if playerRect.colliderect(blockRect):
                    plyrNewPos[0] -= direction[0]
                    break

        for step in range(speed):
            plyrNewPos[1] += direction[1]
            playerRect = pygame.Rect(plyrNewPos[0], plyrNewPos[1] + player['size'][1] - 1, player['size'][0], 1)
            for blockIndex in blocks:
                block = blocks[blockIndex]
                blockRect = pygame.Rect(block['pos'][0], block['pos'][1], block['size'][0], block['size'][1])
                if playerRect.colliderect(blockRect):
                    plyrNewPos[1] -= direction[1]
                    break
        player['pos'] = plyrNewPos
        return player

    def actObj(self, index):
        player = self.player
        actObj = self.objs['act'][index]
        plyrRect = pygame.Rect(player['pos'][0], player['pos'][1] + player['size'][1] - 1, player['size'][0], 1)
        actObjRect = pygame.Rect(actObj['pos'][0], actObj['pos'][1], actObj['size'][0], actObj['size'][1])
        if actObj['actSide'] == 0: actObj['actSide'] = player['side']
        return 1 if (actObjRect.colliderect(plyrRect) and player['side'] == actObj['actSide']) else 0

    def search2Pos(self, player, player2):
        if player['oldPos'] != player['pos']:
            plyrPosHstry = player['posHstry'].copy()
            plyrPosHstry.append([player['pos'], player['side']])

            if len(plyrPosHstry) >= player['posHstrySz']:
                plyrPosHstry.pop(0)
            player2['pos'] = plyrPosHstry[0][0]
            player2['side'] = plyrPosHstry[0][1]
            player['posHstry'] = plyrPosHstry.copy()
        return player, player2


    def updateAnim(self, player):
        keys = pygame.key.get_pressed()
        delaySize = player['animDlySize']['fast'] if keys[pygame.K_x] else player['animDlySize']['df']

        if player['oldPos'] != player['pos']:
            if player['animDly'] > 0: player['animDly'] -= 1
            if player['animDly'] == 0:
                player['imgIndex'] = 'run2' if player['imgIndex'] == 'run1' else 'run1'
                player['animDly'] = delaySize
        else: player['animDly'], player['imgIndex'] = 0, 'df'
        player['img'] = player['imgs'][player['imgIndex']][player['side']]
        return player

    def getCameraPos(self, obj, screenSize, roomSize):
        cntrObjPosOnScrn = [
            obj['pos'][0] - (screenSize[0] - obj['size'][0]) // 2,
            obj['pos'][1] - (screenSize[1] - obj['size'][1]) // 2
        ]

        cameraPos = [
            min(max(cntrObjPosOnScrn[0], 0), roomSize[0] - screenSize[0]),
            min(max(cntrObjPosOnScrn[1], 0), roomSize[1] - screenSize[1])
        ]

        return cameraPos


class Drawer:
    @staticmethod
    def super_draw(surface, camera_pos, objs):
        objs.sort(key=lambda obj: obj[0][1] + obj[1].get_size()[1])

        for pos, sprite in objs:
            surface.blit(sprite, (pos[0] - camera_pos[0], pos[1] - camera_pos[1]))

    @staticmethod
    def drawText(surface, font_path, size, text, color, pos, center):
        font = pygame.font.Font(font_path, size)
        text = font.render(text, 1, color)
        if center:
            pos = text.get_rect(center=(pos[0], pos[1]))
        return surface.blit(text, pos)

    @staticmethod
    def printDialog(surface, dialog, speed, delay, letter_index):
        keys = pygame.key.get_pressed()
        font = pygame.font.Font(dialog['font'], dialog['size'])
        pos = bg_pos = dialog['pos'].copy()
        max_width = dialog['bg'].get_width()
        line = ''
        line_size = [0, font.get_height()]
        if keys[pygame.K_x]: letter_index = len(dialog['text'])
        letter = dialog['text'][:letter_index]
        words = letter.split(' ')

        surface.blit(dialog['bg'], (bg_pos[0], bg_pos[1]))

        for word in words:
            word_surface = font.render(word, True, dialog['color'])
            word_width = word_surface.get_width()

            if line_size[0] + word_width <= max_width:
                line += word + ' '
                line_size[0] += word_width + font.size(' ')[0]
            else:
                line_surface = font.render(line, True, dialog['color'])
                surface.blit(line_surface, pos)

                pos[1] += line_size[1]
                line = word + ' '
                line_size[0] = word_width + font.size(' ')[0]

        if line:
            line_surface = font.render(line, True, dialog['color'])
            surface.blit(line_surface, pos)

        if delay <= 0 and letter_index < len(dialog['text']):
            letter_index += 1
            delay = speed
        delay -= 1

        return delay, letter_index
    def whileDlogsIndex(self, player, index, indexes, one_keyD, dlogLetter):
        if one_keyD(pygame.K_z):
            dlogLetter = 0
            if index < indexes[-1]:
                index += 1
            else:
                index = -1
                player['collid'] = {'left': 0, 'right': 0, 'up': 0, 'down': 0}
        return player, index, dlogLetter

class Scaler:
    @staticmethod
    def scale(orig_size, new_size, orig_obj_size):
        scale_factor = min(new_size[0] / orig_size[0],
                           new_size[1] / orig_size[1])
        return [(orig_obj_size[0] * scale_factor), (orig_obj_size[1] * scale_factor)]

    @staticmethod
    def imgTransf(path, new_size):
        img = pygame.image.load(path).convert_alpha()
        img = pygame.transform.scale(img, (new_size[0], new_size[1]))
        return img
