[![python](https://img.shields.io/badge/python3-v3.6.0-brightgreen)](https://www.python.org/dev/peps/pep-0537/#schedule-first-bugfix-release)
[![dependency - argparse](https://img.shields.io/badge/dependency-argparse-blue)](https://pypi.org/project/argparse/1.4.0/)

# RenameFiles
*Renombrar Archivos* es un pequeño proyecto nace con la finalidad de renombrar las capturas de pantalla que hago de mis clases online, para luego incluirlas en los Readme (anotaciones) o notebooks de forma más estructurada y ordenada.

![](/src/original/alpaca-gaa9f35dc2_640.jpg)

> Nota: Sobre lo anterior las capturas de pantalla por defecto se guardan con fecha y hora en el sistema operativo, por tal motivo ya están ordenas por defecto.


# Prerequisitos
No requiere el uso de ningún paquete externo de `Python`, por tal motivo, este script `rename_files.py` debe correr en Python 3.6 en adelante sin problemas.

No obstante si el shebang (`#!`) está generando inconvenientes, se puede crear un ambiente virtual de acuerdo al sistema operativo (OS) anfitrión (host)

## MacOS

Se crea el ambiente virtual en el directorio dónde se tiene el script desde la terminal

```bash
python3 -m venv .venv
```

Se habilita
```bash
. .venv/bin/activate
```

Para desabilitar el entorno virtual
```bash
deactivate
```

## Windows

Se crea el ambiente virtual en el directorio dónde se tiene el script desde el power shell por ejemplo primero `C:\<TU-RUTA>\`

```bash
py -m venv .venv
```

```bash
python -m venv .venv
```

Dependiendo de como esté definida la variable de entorno para python

```bash
py -m venv .venv
```

Se habilita el entorno virtual
```bash
.\.venv\Scripts\Activate.ps1
```

Para desabilitar el entorno virtual
```bash
deactivate
```


> Nota: Es posible correr un entorno Linux en Windows, con alguna distribución open source. Ver el siguiente enlace para más detalle [Instalación de Linux en Windows con WSL](https://learn.microsoft.com/es-es/windows/wsl/install)


# Uso
Al lanzar el siguiente comando en la terminal (Si estás en Windows cambiar`python3` por `py` o `python` dependiendo de como esté definida la variable de entorno para python):

```bash
python3 rename_files.py --help
````

o también:

```bash
python3 rename_files.py -h
````

Se verán los flags (opciones) que dispone el archivo `rename_files.py` como parámetros de entrada

```bash
usage: rename_files.py [-h] [-d DIRECTORY] [-s START_PREFIX] [-f END_PREFIX] [-e EXTENSION]
                       [-i INCLUDE] [--is_test IS_TEST]

Change Files name

optional arguments:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        Directory File
  -s START_PREFIX, --start_prefix START_PREFIX
                        Start Prefix File
  -p END_PREFIX, --end_prefix END_PREFIX
                        End Prefix File
  -e EXTENSION, --extension EXTENSION
                        Extension File
  -i INCLUDE, --include INCLUDE
                        Word in File name
  --is_test IS_TEST     Is test mode
```

## Parámetros

1. `--directory`: o también `-d` este por defecto toma el directorio actual `./`

    Para apuntar al directorio destino se incluye la ruta relativa desde donde se ejecuta el script `rename_files.py`

2. `--start_prefix`: o también `-s` este prefijo clasifica la imagen quizás por capítulos y empieza por defecto en `01` y esta es igual para todas las imágenes que se encuentran en la ruta objetivo. Por tal motivo, puede ser ajustada a lo que se necesita.

3. `--end_prefix`: o también `-p` este sufijo tiene como finalidad definir de que van tratan el conjunt de images, puede ser opcional si en el punto 2 incluyo esa definición.

4. `--extension`: o también `-e` es para indicar que extensión de archivos se va ha renombrar por defecto es `.png` nótese que siempre empieza con `.` caso contrario arrojará un excepción `raise Exception("Extensions must start with dot")` que dice `"Las extensiones deben empezar con punto"`

5. `--include`: o también `-i` es opcional y tiene por finalidad filtrar los archivos que contengan cierta palabra y sobre estos se realice el renombramiento respectivo. Por defecto es un `string` vacio.

6. `--is_test`: este parámetro permite ver cuando es `True` como quedarían el nombramiento de archivos sin cambiarlos. Por defecto es `False`, es decir que al omitirlo si renombra los archivos. Nótese que el boleano puede ir todo en minúsculas en la línea de comandos.

> Nota: Entre el punto 2 y 3 existe un parámetro `idx` dentro de la función `change_name` que lleva el conteo de los archivos y se los asigna de forma automática a los nombres de los mismos para diferenciarlos.

## Ejemplos

Todos los ejemplos se presentan a modo de prueba `--is_test true`

1. Renombrar todos los archivos en `./src/original/` con el sufijo (`-p`) lamini
    ```bash
    python3 rename_files.py -d ./src/original/ -p lamini -e .jpg --is_test true 
    ```
    Se obtiene lo siguiente:
    ```bash
    # Archivo Orginal         >> Archivo Renombrado
    llama-g8e2017c1e_640.jpg  >> 01_01_lamini.jpg
    llama-g6f862433a_640.jpg  >> 01_02_lamini.jpg
    alpaca-gaa9f35dc2_640.jpg >> 01_03_lamini.jpg
    ```

2. Renombrar todos los archivos en `./src/original/` pero que tenga el prefijo de `lamini`
    ```bash
    python3 rename_files.py -d ./src/original/ -s lamini -e .jpg --is_test true
    ```
    Se obtiene lo siguiente:
    ```bash
    # Archivo Orginal         >> Archivo Renombrado
    llama-g8e2017c1e_640.jpg  >> lamini_01.jpg
    llama-g6f862433a_640.jpg  >> lamini_02.jpg
    alpaca-gaa9f35dc2_640.jpg >> lamini_03.jpg
    ```

3. Renombrar todos los archivos en `./src/original/` pero con el sufijo de `lamini` y sin prefijo
    ```bash
    python3 rename_files.py -d ./src/original/ -s "" -p lamini -e .jpg --is_test true
    ```
    Se obtiene lo siguiente:
    ```bash
    # Archivo Orginal         >> Archivo Renombrado
    llama-g8e2017c1e_640.jpg  >> 01_lamini.jpg
    llama-g6f862433a_640.jpg  >> 02_lamini.jpg
    alpaca-gaa9f35dc2_640.jpg >> 03_lamini.jpg
    ```

4. Renombrar todos los archivos en `./src/original/` que sean `alpaca` y con el prefijo `lamini`
    ```bash
    python3 rename_files.py -d ./src/original/ -s lamini -i alpaca -e .jpg --is_test true
    ```
    Se obtiene lo siguiente:
    ```bash
    # Archivo Orginal         >> Archivo Renombrado
    alpaca-gaa9f35dc2_640.jpg >> lamini_01.jpg
    ```

5. Renombrar todos los archivos en `./src/original/` que sean `alpaca` pero con el sufijo (`-p`) de `lamini` y sin prefijo (`-s`)
    ```bash
    python3 rename_files.py -d ./src/original/ -s "" -p lamini -i alpaca -e .jpg --is_test true
    ```
    Se obtiene lo siguiente:
    ```bash
    # Archivo Orginal         >> Archivo Renombrado
    alpaca-gaa9f35dc2_640.jpg >> 01_lamini.jpg
    ```

> Nota: para que el renombramiento haga efecto remover `--is_test true`,
> Si estas en Windows cambiar`python3` por `py` o `python`. Si empleas un entorno virtual puedes usar `python` también.


# Imágenes
Tomadas de [pixabay](https://pixabay.com/es/)

[![](/src/original/alpaca-gaa9f35dc2_640.jpg)](https://pixabay.com/photos/alpaca-llama-animal-lama-head-4524200/)
[![](/src/original/llama-g6f862433a_640.jpg)](https://pixabay.com/photos/lama-head-curious-nose-mouth-7024125/)
[![](/src/original/llama-g8e2017c1e_640.jpg)](https://pixabay.com/photos/llama-animal-head-brown-llama-head-5841826/)

# Consideraciones
Sobre el script, al ser pequeño, busqué no añadirle dependencias u otras capas de complejidad. Por tal motivo, no he efectuado `test unitarios` ([pytest](https://docs.pytest.org/en/7.3.x/)), ni he aplicado [pylint](https://pypi.org/project/pylint/) o similares. Esto último para verificar que el código cumple con el [PEP 8](https://peps.python.org/pep-0008/).

# .gitignore

Fue generado en [gitignore.io](https://www.toptal.com/developers/gitignore/) con los filtros `python`, `macos`, `windows` y consumido mediante su API como archivo crudo desde la terminal:

```bash
curl -L https://www.toptal.com/developers/gitignore/api/python,macos,windows > .gitignore
```

# Autores

* **Hubert Ronald** - *Trabajo Inicial* - [HubertRonald](https://github.com/HubertRonald)

Ve también la lista de [contribuyentes](https://github.com/HubertRonald/RenameFiles/contributors) que participaron en este proyecto.



# Licencia

Este proyecto está bajo licencia MIT - ver la [LICENCIA](LICENSE) archivo (en inglés) para más detalle.