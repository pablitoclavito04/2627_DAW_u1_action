# Generación automática de documentación con GitHub Actions.

Este repositorio demuestra cómo generar documentación de código Python en varios formatos mediante herramientas de documentación y GitHub Actions.


## 1. Objetivos:

- Documentar código Python mediante docstrings de estilo Google.
- Generar documentación HTML con `pdoc`.
- Generar documentación Markdown con un script Python.
- Automatizar las pruebas y la generación de documentación mediante GitHub Actions.
- Publicar los archivos generados como un artefacto descargable.


## 2. Herramientas utilizadas:

| Herramienta | Uso |
|---|---|
| Python 3.12 | Lenguaje utilizado para el ejemplo y los scripts |
| pdoc | Generación de documentación HTML |
| pytest | Ejecución de pruebas automatizadas |
| GitHub Actions | Automatización del proceso |
| actions/upload-artifact | Publicación de la documentación generada como artefacto |


## 3. Código documentado:

El archivo [`main.py`](main.py) contiene la función `saludo()`, documentada con el estilo Google.

```python
def saludo(nombre: str) -> str:
    """Genera un saludo personalizado.

    Args:
        nombre (str): Nombre de la persona a la que saludar.

    Returns:
        str: Mensaje de saludo personalizado.
    """
    return f"Hola, {nombre}!"
```

El docstring explica la finalidad de la función, su parámetro y el valor que devuelve.


## 4. Generación local de documentación:

Para reproducir la generación en un ordenador con Python instalado, clona el repositorio e instala las herramientas:

```bash
python -m pip install pdoc pytest
```

Genera la documentación HTML:

```bash
python -m pdoc -o docs/html main
```

Genera la documentación Markdown:

```bash
python generate_markdown.py
```

Los archivos se guardan en `docs/`.

- HTML: `docs/html/main.html`
- Página de entrada HTML: `docs/html/index.html`
- Markdown: `docs/markdown/documentacion.md`

El HTML se genera automáticamente a partir de `main.py` mediante `pdoc`. El Markdown se crea con el script [`generate_markdown.py`](generate_markdown.py).


## 5. GitHub Actions:

El workflow se encuentra en [`.github/workflows/ci.yaml`](.github/workflows/ci.yaml).

Se ejecuta cuando se suben cambios a la rama `main` mediante el evento `push`, y también puede iniciarse manualmente mediante `workflow_dispatch`.

El job realiza estos pasos:

1. Descarga el repositorio.
2. Configura Python e instala `pdoc` y `pytest`.
3. Ejecuta `update_readme.py` para ejecutar las pruebas y actualizar el estado en este README.
4. Genera la documentación HTML mediante `pdoc`.
5. Genera la documentación Markdown mediante `generate_markdown.py`.
6. Sube la carpeta `docs/` como artefacto descargable.

Las ejecuciones pueden consultarse en la pestaña **Actions** del repositorio. Cuando una ejecución termine correctamente, el artefacto `documentacion` estará disponible en el resumen de esa ejecución.


## 6. Control de versiones y commits:

Los cambios se registran mediante Git. Los mensajes de commit deben ser breves, descriptivos y expresar la acción realizada.

Ejemplos de mensajes apropiados para esta mejora:

- `Documenta la función saludo con Google Style`
- `Añade generador de documentación Markdown`
- `Automatiza la generación de documentación`
- `Actualiza README con instrucciones y resultados`

Estos son ejemplos de mensajes recomendados; el historial real de commits del repositorio constituye la evidencia de los cambios efectivamente realizados.


## 7. Acceso mediante SSH:

Para comprobar la autenticación SSH con GitHub, se puede ejecutar:

```bash
ssh -T git@github.com
```

Si la clave pública está añadida a la cuenta de GitHub y la autenticación funciona, GitHub muestra un mensaje de bienvenida.

La clave privada debe mantenerse en el ordenador y nunca debe subirse al repositorio. La clave pública puede añadirse en la configuración SSH de la cuenta de GitHub.

La autenticación SSH no sustituye a los permisos del repositorio: el acceso debe limitarse a las personas autorizadas. Si el repositorio es privado, hay que conceder acceso al profesor para que pueda revisarlo.


## 8. Clonar y reproducir el proyecto:

Clona el repositorio:

```bash
git clone https://github.com/pablitoclavito04/2627_DAW_u1_action.git
cd 2627_DAW_u1_action
```

Instala las herramientas:

```bash
python -m pip install pdoc pytest
```

Ejecuta las pruebas:

```bash
python -m pytest -v
```

Genera los dos formatos:

```bash
python -m pdoc -o docs/html main
python generate_markdown.py
```

También puedes ejecutar el workflow desde **GitHub → Actions → CI y documentación → Run workflow**, siempre que tengas los permisos necesarios.


## 9. Cuestionario de responder:

### a) Identificación de herramientas de generación de documentación. ¿Qué herramienta o generador (p. ej., Sphinx, pdoc, Javadoc, Doxygen, Dokka) utilizaste en el workflow para crear la documentación en /docs?

Se utiliza `pdoc` para generar documentación HTML a partir del código Python. Un script complementario genera la documentación Markdown. GitHub Actions automatiza ambos procesos.

### b) Documentación de componentes. Muestra un fragmento del código con comentarios/docstrings estructurados (p. ej., :param, :return: o etiquetas equivalentes) que haya sido procesado por la herramienta. Comenta que estilo de documentación has utlicado: (p. ej., reStructuredText, Google Style, KDoc)

La función `saludo()` de `main.py` utiliza un docstring de estilo Google. Las secciones `Args` y `Returns` describen el parámetro y el valor devuelto. `pdoc` procesa esa documentación al generar el HTML.

### c) Multiformato. ¿Qué segundo formato (además de HTML) generaste? Explica la configuración o comandos del workflow y herramientas que lo producen.

Se generan HTML y Markdown. El HTML se crea mediante `python -m pdoc -o docs/html main`; el Markdown se genera ejecutando `python generate_markdown.py`. Ambos se guardan en `docs/` y se suben como artefacto.

### d) 	Colaboración. Explica cómo GitHub facilita mantener la documentación (actualizaciones del README.md y de /docs) cuando colaboran varias personas (PRs, reviews, checks de CI, protección de ramas).

GitHub permite colaborar mediante ramas, pull requests y revisiones de código. Los checks de CI permiten detectar errores antes de integrar cambios. La protección de ramas puede exigir revisiones y ejecuciones satisfactorias antes de aceptar una integración.

### e) Control de versiones. Muestra mensajes de commit que evidencien el nuevo workflow. ¿Son claros y descriptivos? Justifícalo. Ademas de un conjunto de mensajes de tus commits.

Los mensajes como `Añade generador de documentación Markdown` y `Automatiza la generación de documentación` describen el cambio de forma concreta y comienzan con un verbo en imperativo. La evidencia definitiva son los commits reales del repositorio.

### f) Accesibilidad y seguridad. ¿Qué medidas/configuración del repositorio garantizan que solo personal autorizado accede al código y la documentación? (p. ej., repositorio privado, equipos, roles, claves/secretos, branch protection).

El acceso depende de si el repositorio es público o privado y de los permisos concedidos a cada colaborador. Las claves privadas y los secretos no deben guardarse en el repositorio. La protección de ramas y los permisos mínimos ayudan a reducir cambios no autorizados. Las medidas efectivamente configuradas deben comprobarse en los ajustes del repositorio.

### g) 	Instalación/uso documentados. Indica dónde en el README.md explicas el funcionamiento del workflow y dónde detallas las herramientas y comandos de documentación.

La sección 2 explica las herramientas; la sección 4 contiene los comandos de generación local; la sección 5 describe el workflow; y la sección 8 explica cómo clonar y reproducir el proyecto.

### h) Integración continua. Justifica por qué el workflow utilizado es CI. ¿Qué evento dispara automáticamente la generación/actualización de la documentación (p. ej., push, pull_request, workflow_dispatch)?

El workflow es una forma de integración continua porque automatiza comprobaciones y tareas del proyecto al recibir cambios. El evento `push` en `main` inicia el proceso automáticamente, y `workflow_dispatch` permite iniciarlo manualmente.



## Estado de los tests
✅ Tests correctos
