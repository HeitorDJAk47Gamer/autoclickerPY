import time

import pyautogui

def click(x, y):
    # Clique no local especificado
    pyautogui.click(x, y)

def main():
    # Escolha a posição do mouse onde você deseja clicar
    x = 100
    y = 100

    # Comece a clicar
    while True:
        click(x, y)
        time.sleep(1)

    # Mostre o botão para definir a posição do clique
    pyautogui.displayMessage("Clique aqui para definir a posição do clique")

if __name__ == "__main__":
    main()
