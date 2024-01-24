import time
from colorama import Fore, Style

def loading_animation():
    for _ in range(50):
        print(Fore.GREEN + '#' + Style.RESET_ALL, end='', flush=True)
        time.sleep(0.2)

def main():
    print("AGUARDE ANALISANDO REDES")
    loading_animation()
    print("\nAnálise concluída!")

if _name_ == "_main_":
    # Simula uma espera de 2 horas (7200 segundos)
    time.sleep(7200)
    main()