# Simple Boilerplate for Python 3

## Configuración del Entorno

Este proyecto utiliza Python 3. Asegúrate de tenerlo instalado en tu sistema.

### Instalación

1. Clona o crea un Template de este repositorio.
2. Navega al directorio del proyecto.
3. Crea un entorno virtual:

```bash
python -m venv venv
```

4. Activa el entorno virtual:
- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`
5. Instala las dependencias:

```bash
pip install -r requirements-dev.txt
```


## Ejecución de Tests

Para ejecutar los tests, utiliza el comando:

```bash
pytest
```

## Ejecución de la Aplicación

Para ejecutar la aplicación, utiliza el comando:

```bash
python src/main.py
```