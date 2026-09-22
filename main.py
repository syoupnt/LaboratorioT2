# Colores para el texto
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
CYAN    = '\033[36m'
RESET   = '\033[39m'

print(CYAN + 'Sistema de orientación y registro de atenciones para el módulo de soporte académico\n' + RESET)

# Registra cinco formularios de consulta durante la ejecución.
for i in range(5):
    print(YELLOW + f'[Formulario de Consulta #{i+1}]' + RESET)
