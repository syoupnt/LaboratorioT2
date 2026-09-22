# Colores para el texto
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
CYAN    = '\033[36m'
RESET   = '\033[39m'

# Solicita y valida los datos básicos del estudiante.
def pedir_codigo():
    codigo = input(f'{YELLOW}Ingrese el código del estudiante (N00XXXXXX):{RESET} N00')
    validar_texto(codigo)

    if len(codigo) != 6:
        raise ValueError('Longitud incorrecta del código')

    return codigo

def pedir_nombre():
    nombre = input(f'{YELLOW}Ingrese el nombre del estudiante:{RESET} ')
    validar_texto(nombre)
    return nombre

def pedir_consulta():
    # Muestra las opciones y convierte la selección en un tipo de consulta.
    mostrar_menu_consulta()
    consulta = input(f'{YELLOW}Ingrese el tipo de consulta (1-5):{RESET} ')
    validar_texto(consulta)

    match consulta:
        case '1':
            return 'Matrícula'
        case '2':
            return 'Pagos'
        case '3':
            return 'Constancia'
        case '4':
            return 'Plataforma'
        case '5':
            return 'Otro'
        case _:
            raise ValueError('Tipo de consulta invalida')

def pedir_descripcion():
    descripcion = input(f'{YELLOW}Ingrese la descripción de la consulta:{RESET} ')
    validar_texto(descripcion)
    return descripcion

def mostrar_menu_consulta():
    print(GREEN + 'LISTA DE TIPOS DE CONSULTA')
    print('------------------')
    print('| 1. Matrícula   |')
    print('| 2. Pagos       |')
    print('| 3. Constancia  |')
    print('| 4. Plataforma  |')
    print('| 5. Otro        |')
    print('------------------' + RESET)

def asignar_prioridad(consulta):
    # Define la prioridad según el tipo de atención solicitado.
    match consulta:
        case 'Matrícula':
            return 'MUY ALTA'
        case 'Pagos':
            return 'ALTA'
        case 'Plataforma':
            return 'MEDIA'
        case 'Constancia':
            return 'BAJA'
        case 'Otro':
            return 'VARIABLE'
        case _:
            raise ValueError('Tipo de consulta invalida')

def validar_texto(texto):
    # Evita que un campo obligatorio quede vacío.
    if len(texto) == 0:
        raise ValueError('El campo no puede dejarse vacío')

def mostrar_resumen(i, codigo, nombre, consulta, prioridad, descripcion):
    print(GREEN + f'RESUMEN DE LA CONSULTA #{i}')
    print(f'[ESTUDIANTE]  Código: {RESET + codigo + GREEN}, Nombre: {RESET + nombre + GREEN}')
    print(f'[CONSULTA]    Tipo: {RESET + consulta + GREEN}, Prioridad: {RESET + prioridad + GREEN}')
    print(f'[DESCRIPCIÓN] {RESET + descripcion}\n')

print(CYAN + 'Sistema de orientación y registro de atenciones para el módulo de soporte académico\n' + RESET)

# Registra cinco formularios de consulta durante la ejecución.
for i in range(5):
    print(YELLOW + f'[Formulario de Consulta #{i+1}]' + RESET)

    try:
        codigo = pedir_codigo()
        nombre = pedir_nombre()
        consulta = pedir_consulta()
        prioridad = asignar_prioridad(consulta)
        descripcion = pedir_descripcion()

        print()
        mostrar_resumen(i+1, codigo, nombre, consulta, prioridad, descripcion)
    except Exception as e:
        print(f'\n{RED}ERROR: {e}{RESET}\n')
