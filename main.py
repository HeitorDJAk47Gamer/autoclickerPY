import time, pyautogui, keyboard

def auto_clicker(x, y, interval):
    """Executa cliques automáticos na posição (x, y) a cada `interval` segundos."""
    print(f"Iniciando auto-clicker na posição ({x}, {y}) com intervalo de {interval} segundos.")
    while not keyboard.is_pressed('q'):
        pyautogui.click(x, y)
        time.sleep(interval)

def main():
    print("Auto-clicker pronto para configurar.")
    print("1. Posicione o mouse e pressione 'p' para capturar a posição.")
    print("2. Pressione 's' para iniciar o auto-clicker ou 'q' para sair.")
    
    x, y = None, None
    interval = 0.1  # Intervalo padrão de 0.1 segundo entre cliques
    
    while True:
        if keyboard.is_pressed('p'):
            x, y = pyautogui.position()
            print(f"Posição de clique definida em: ({x}, {y})")
            time.sleep(0.5)  # Pequena pausa para evitar múltiplas capturas

        elif keyboard.is_pressed('s') and x is not None and y is not None:
            print("Iniciando auto-clicker...")
            auto_clicker(x, y, interval)

        elif keyboard.is_pressed('q'):
            print("Auto-clicker encerrado.")
            break

        elif keyboard.is_pressed('i'):
            try:
                interval = float(input("Digite o intervalo de clique em segundos: "))
                print(f"Intervalo atualizado para {interval} segundos.")
            except ValueError:
                print("Intervalo inválido! Por favor, digite um número.")

        time.sleep(0.1)

if __name__ == "__main__":
    main()
