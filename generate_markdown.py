"""Genera documentación Markdown a partir de main.py."""

import inspect
import main
from pathlib import Path


def generar_documentacion() -> None:
    """Genera un archivo Markdown con la documentación de las funciones."""
    destino = Path("docs/markdown")
    destino.mkdir(parents=True, exist_ok=True)

    funcion = main.saludo
    descripcion = inspect.getdoc(funcion) or "Sin descripción disponible."

    contenido = f"""# Documentación del módulo main

## Función `saludo()`

```python
{inspect.getsource(funcion).strip()}
```

### Descripción

{descripcion}

### Parámetros

- `nombre` (`str`): nombre de la persona a la que saludar.

### Retorno

- `str`: mensaje de saludo personalizado.

### Ejemplo de uso

```python
print(main.saludo("Usuario"))
```

Resultado esperado:

```text
Hola, Usuario!
```
"""

    archivo = destino / "documentacion.md"
    archivo.write_text(contenido, encoding="utf-8")
    print(f"Documentación Markdown generada: {archivo}")


if __name__ == "__main__":
    generar_documentacion()
