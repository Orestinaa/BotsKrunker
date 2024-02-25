import KrunkerBOT as kb
import ChromeWindow as cw

URL = 'https://krunker.io/?game=FRA:mbzaa'
num_bots = 3

chrome = cw.ChromeWindow()

bots_list = []

for i in range (num_bots):
    bot = kb.KrunkerBOT(chrome.getDriver(), chrome.getWait(), URL, i)
    bot.play()
    bots_list.append(bot)
    if i < num_bots - 1:
        chrome.createTab()

print("Bots created")

while True:
    for bot in bots_list:
        bot.auto_respawn()