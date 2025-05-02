import pyautogui
import time

# Obtener el tamaño de la pantalla
screen_width, screen_height = pyautogui.size()

# Calcular las coordenadas del centro
center_x = screen_width / 2
# center_y = screen_height / 2
center_y = screen_height / 2 + (screen_height * 0.1)

# Bucle para simular clics constantes
while True:
  pyautogui.click(center_x, center_y)
  time.sleep(0.1)  # Ajusta la cantidad de segundos entre clics
