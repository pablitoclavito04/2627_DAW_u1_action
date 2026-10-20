# Documentación del módulo main

## Función `saludo()`

```python
def saludo(nombre: str) -> str:
    """Genera un saludo personalizado.

    Args:
        nombre (str): Nombre de la persona a la que saludar.

    Returns:
        str: Mensaje de saludo personalizado.
    """
    return f"Hola, {nombre}!" # Cambio para forzar error. Para que no falle: f"Hola, {nombre}!"
```

### Descripción

Genera un saludo personalizado.

Args:
    nombre (str): Nombre de la persona a la que saludar.

Returns:
    str: Mensaje de saludo personalizado.

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
