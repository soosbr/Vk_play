import ctypes
import string
import os


def find_directory(name):
    available_drives = ['%s:\\' % d for d in string.ascii_uppercase if os.path.exists('%s:\\' % d)]
    for path in available_drives:
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root)


STEAM_DIRECTORY = find_directory("steam.exe")
GAME_DIRECTORY = ""
for i in find_directory("underlords.exe").split("\\"):
    if i == "Underlords":
        GAME_DIRECTORY += "Underlords"
        break
    else:
        GAME_DIRECTORY += i + "\\"
# Получение разрешения
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
resolution = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
# Считывание данных с конфиг файла
f = open(f"{GAME_DIRECTORY}\game\\dac\\cfg\\video.txt")
text = f.read().split("\n")
f.close()
# Обработка данных конфиг файла
text[8] = f'\t"setting.defaultres"\t\t"{resolution[0]}"'
text[9] = f'\t"setting.defaultresheight"\t\t"{resolution[1]}"'
text = "\n".join(text)
# Запись в конфиг файл
f = open(f"{GAME_DIRECTORY}\\game\\dac\\cfg\\video.txt", "w")
f.write(text)
f.close()
# Запуск игры
os.startfile(f"{GAME_DIRECTORY}\\game\\bin\\win64\\underlords.exe")
