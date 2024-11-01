import time
import pyautogui

def click(x, y):
    # Clique no local especificado
    pyautogui.click(x, y)

def main():
    # Escolha a posição do mouse onde você deseja clicar
    x = 610
    y = 610

    # Comece a clicar
    try:
        while True:
            click(x, y)
            time.sleep(0.1)  # Intervalo entre os cliques (ajustável)

    except KeyboardInterrupt:
        print("Script interrompido pelo usuário.")

if __name__ == "__main__":
    main()
