"""
Ejercicio 14
Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.
"""
def reemplazar(string):
    patttern = "[\s\t]"
    repl = ";"
    print(re.sub(patttern, repl, string))
