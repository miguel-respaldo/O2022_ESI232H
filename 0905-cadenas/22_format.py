texto = "una frase cualquiera --{:<10s}-- --{:>10s}--"
texto2 = "--{:^10.2f}-- --{:>10d}--"
texto3 = "--{:^10.2e}-- --{:>10b}--"

print(texto.format("uno", "dos"))
print(texto2.format(3.1416, 2022))
print(texto3.format(314.16, 255))
