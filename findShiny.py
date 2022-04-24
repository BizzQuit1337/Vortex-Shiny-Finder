###imports###
import pyautogui as pag
import pytesseract
import time, random, math

###variables###
directions = ['right', 'left']
loopSize = 0.2
pokemon = 'Shiny'
cordsPokemonName = (191, 555, 182, 33)
cordsWildBattle = (268, 664)

###functions###
def movement(directions, loopSize):
    pag.keyDown(directions)
    time.sleep(loopSize)
    pag.keyUp(directions)

def checkPokemon(cords, file):
    screenshot = pag.screenshot(region=cords) 
    screenshot.save(file)
    pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract'
    checkPokemon.pokemon = pytesseract.image_to_string(file)
    with open('pokedex.txt', 'a') as f:
        f.write(checkPokemon.pokemon)

def battleOrLeave(pokemonName, pokemon, cords):
    for name in pokemonName.split(' '):
        if name == pokemon:
            with open('battledPokemon.txt', 'a') as f:
                f.write(pokemonName)
            pag.click(cords)
            time.sleep(1)
            zoomFormat()
            catch()

def clickWait(cords1, cords2, timer):
    time.sleep(timer)
    pag.click(cords1)
    time.sleep(timer/2)
    pag.click(cords2)

def catch():
    clickWait((548, 352), (545, 352),  1) #init continue
    clickWait((609, 263), (605, 263),  1) #ultra ball
    clickWait((629, 343), (625, 343), 1) #use item
    clickWait((505, 248), (501, 250), 1) #click contiune after ball both regular and longer
    ##### lazy way to throw 5 balls per encounter #####
    clickWait((609, 263), (605, 263),  1) #ultra ball
    clickWait((629, 343), (625, 343), 1) #use item
    clickWait((505, 248), (501, 250), 1)
    clickWait((609, 263), (605, 263),  1) #ultra ball
    clickWait((629, 343), (625, 343), 1) #use item
    clickWait((505, 248), (501, 250), 1)
    clickWait((609, 263), (605, 263),  1) #ultra ball
    clickWait((629, 343), (625, 343), 1) #use item
    clickWait((505, 248), (501, 250), 1)
    ##### back to regular not being lazy #####
    clickWait((507, 258), (505, 258), 1)
    clickWait((489, 158), (485, 158), 1)
    pag.click(833, 65)

def zoomFormat():
    pag.click(1126, 62)
    for i in range(0, 7):
        time.sleep(0.1)
        pag.click(1028, 518)
    pag.click(552, 625)



###main event###
time.sleep(3)
while True:
    for i in range(0, 100000):
        print(i)
        for direction in directions:
            movement(direction, loopSize)
            checkPokemon(cordsPokemonName, 'wild.png')
            battleOrLeave(checkPokemon.pokemon, pokemon, cordsWildBattle)
    break