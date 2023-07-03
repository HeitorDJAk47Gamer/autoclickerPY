import time
import pyautogui

# Definir coordenadas de destino para o clique
x = 100
y = 100

# Definir quantidade de cliques
num_clicks = 10

# Aguardar 5 segundos antes de iniciar
time.sleep(5)

# Loop para realizar os cliques
for _ in range(num_clicks):
    # Mover o mouse para as coordenadas desejadas
    pyautogui.moveTo(x, y, duration=0.2)
    
    # Simular um clique no botão esquerdo do mouse
    pyautogui.click(button='left')
    
    # Aguardar 1 segundo antes do próximo clique
    time.sleep(1)
