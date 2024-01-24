import time
from colorama import Fore, Style

def loading_animation():
    for _ in range(50):
        print(Fore.GREEN + '#' + Style.RESET_ALL, end='', flush=True)
        time.sleep(7200)

def main():
    print("AGUARDE ANALISANDO REDES")
    loading_animation()
    print("\nAnálise concluída!")

if __name__ == "__main__":
    print("Iniciando análise...")
    time.sleep(10)
    main()
