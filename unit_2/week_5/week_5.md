# 1. Introducción

## ¿Qué es MPI?

MPI (Message Passing Interface: Interfaz de paso de mensajes) es una interfaz de comunicación que permite que múltiples procesos, que usualmente están corriendo en múltiples núcleos, mantengan una comunicación y permitan la ejecución paralela. Esto es útil en sistemas distribuidos o en arquitecturas multicore.

## ¿Por qué es importante instalar Microsoft MPI (MS-MPI)?

Es importante porque nos permite desarrollar programas que se ejecutarán en paralelo. 

# 2. Requisitos Previos

+ Tener windows 10 o 11.
+ Visual Studio 2022 Community.
+ Conexión a internet para descargar MS-MPI.

# 3. Descarga e instalación de MS-MPI

+ Descargamos MS-MPI desde el sítio oficial de Microsoft MPI.
+ Se descarga el MSMpiSetup.exe: este es el instalador principal del ejecutable. Luego el MSMpiSdk.msi: Este paquete contiene los archivos de desarrollo (headers y bibliotecas) necesarias para compilar programas MPI en C++.
+ Ejecutamos el MSMpiSetup.exe luego el MSMpiSdk.msi y aceptamos los terminos y condiciones.

# 4. Configuración del entorno de Visual Studio para proyectos con MPI

+ Crear un nuevo proyecto en C++ y asignamos el nombre del mismo.
+ Configuramos las rutas de MS-MPI en las propiedades del proyecto. Primero configuramos las rutas de inclusión. Después, configuramos las rutas de bibliotecas. Finalmente agregamos las dependencias de la biblioteca MS-MPI.
+ Escribimos un código MPI básico.

```cpp
#include <mpi.h>
#include <iostream>

int main(int argc, char* argv[]) {
    // Inicializar el entorno MPI
    MPI_Init(&argc, &argv);

    int rank, size;
    // Obtener el número de procesos
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Imprimir mensaje desde cada proceso
    std::cout << "Hola desde el proceso " << rank << " de " << size << std::endl;

    // Finalizar el entorno MPI
    MPI_Finalize();
    return 0;
}
```

Este código incluye las librerias de mpi el cual contiene las funciones que permiten la creación, ejecución y gestión de procesos paralelos. En la función principal se manda dos argumentos que son útiles para que la MPI pueda mantener la comunicación entre los procesos. 

## Conceptos claves y resumen:

+ **MPI:** Es una librería estándar utilizada para desarrollar programas que serán ejecutadas en sistemas distribuidos o paralelos, permitiendo la comunicación entre procesos que se ejecutan en diferentes nodos o núcleos.

+ **Inicialización y finalización:** 
    - MPI_init: necesaria para la inicialización y la comunicación del entorno de ejecución de MPI.
    - MPI_finalize: limpia el entorno de MPI y libera los recursos utilzados.

+ **Proceso, rank, número total de procesos:** Cada proceso tien su propio rank único (identificador), el conjunto de estos procesos se define el tamaño size. Esto permite la gestión de los procesos y la coordinación.

+ **Comunicación y ejecución concurrente:** En un ambiente de ejecución MPI (p. ej. el comando `mpiexec -n 4 ./programa`), se lanzará múltiples procesos que ejecutan el mismo código pero con diferentes valores rank, lo que permite paralelizar las tareas y coodinar la ejecución entre ellos. 

# 5. Pruebas de verificación

```plaintext
SALIDA:

Hola desde el proceso 0 de 4
Hola desde el proceso 1 de 4
Hola desde el proceso 2 de 4
Hola desde el proceso 3 de 4
```

A cada proceso le corresponde un rank (identificador único) y también se muestra el número total de procesos.

---
---

# Programación Paralela en CPUs usando MPI

El objetivo es comprender y aplicar los fundamentos de MPI para desarrollar programas en C++ que aprovechen los múltiples procesos en arquitecturas multicore o distribuidas.

### Actividad 1 – Introductoria: “Hola mundo paralelizado con MPI”

```cpp
#include <iostream>
#include <mpi.h>

int main(int argc, char *argv[]) {
	MPI_Init(&argc, &argv);

	int rank, size;

	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);

	std::cout<< "Hola desde el proceso "<< rank << " de " << size << std::endl;

	MPI_Finalize();
	return 0;
}
```
Al ejecutar el siguiente comando `mpiexec -n 4 .\exercise1.exe`

```plaintext
SALIDA:
PS C:\Users\Magno Ricardo\Documents\test_enviroment\MPI\exercise1\x64\Debug> mpiexec -n 4 .\exercise1.exe
Hola desde el proceso 1 de 4
Hola desde el proceso 2 de 4
Hola desde el proceso 0 de 4
Hola desde el proceso 3 de 4
```

### Actividad 2 – Desafío: “Producto de matrices”

```cpp

```

```plaintext

```