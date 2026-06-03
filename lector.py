import os
from dotenv import load_dotenv

# 1. Cargar las variables del archivo .env
load_dotenv()

# 2. Configuración inicial extraída de las variables de entorno
app = os.getenv('APP_NAME', 'sin nombre')
version = os.getenv('APP_VERSION', '1.0')
debug = os.getenv('DEBUG', 'False')


def mostrar_config(app, version, debug):
    """Muestra en consola la configuración actual de la aplicación."""
    if debug == 'True':
        print(f'[DEBUG] App: {app} v{version}')
    else:
        print(f'App: {app} v{version}')
    return {'app': app, 'version': version, 'debug': debug}


def calcular_promedio(notas):
    """Calcula el promedio aritmético de una lista de notas numéricas."""
    if not notas:
        return 0.0
    return sum(notas) / len(notas)


# 3. Ejecución del programa
config = mostrar_config(app, version, debug)
print(f'Configuración cargada: {len(config)} variables')

# Ejemplo de prueba para la nueva función
notas_ejemplo = [4.5, 3.0, 5.0]
resultado = calcular_promedio(notas_ejemplo)
print(f'Promedio calculado: {resultado}')
