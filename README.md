# Ejercicios De la Comunidad de Programación Competitiva

Para correr algún ejercicio con1| profiling, se debe ejecutar el siguiente comando:

```bash
$ python -m cProfile -o <profile_output_file> <nombre_del_archivo>.py > output_file.txt
```

Este comando se puede configurar en pycharm para que se ejecute con un solo click.
Además, también se puede modificar la configuración de ejecución en pycharm para que
redirija el flujo de entrada desde un archivo, de esta forma se puede automatizar la ejecución.

Luego de ejecutar el archivo con profiling, se puede visualizar el resultado con el siguiente comando:

```bash
$ python -m pstats <profile_output_file>
```

Esto ejecutará un shell interactivo en el que se pueden ejecutar comandos para visualizar
la información del profiling. Algunos comandos útiles son:

- `sort cumtime`: ordena las funciones por tiempo de ejecución acumulado.
- `reverse`: invierte el orden de la lista de funciones.
- `stats`: muestra la lista de funciones con su información de profiling.