"""
Etapa 1: métodos úteis string
Etapa 2: interpolação de strings
Etapa 3: fatiamento de strings
Etapa 4: string múltiplas linhas ou triplas aspas dentro do print() pra ficar
melhor a visualização
"""

curso = "Python"
print(curso.center(10, "#")) # width=10, fillchar='#'

print(".".join(curso))
# .center(): A string a ser centralizada. Retorna ela centralizada e preenchida
# .join(): A string separadora. Junta os itens do iterável usando ela

# Ou seja:
# texto.center() → "centraliza este texto".
# "separador".join() → "use este separador para juntar os itens".


greeting = "   Olá, mundo!   "
print(greeting + ".")
print(greeting.strip() + ".")
print(greeting.lstrip()+ ".")
print(greeting.rstrip() + ".")

#    Olá, mundo!   .
# Olá, mundo!.
# Olá, mundo!   .
#    Olá, mundo!.


# Aspas triplas dentro do print()
menu = "[1] Iniciar [2] Sair"
print(
    """
    ========= MENU =========
    [1] Iniciar 
    [2] Sair
    ========================
    """
)