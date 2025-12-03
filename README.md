# Fujifilm Recipes Helper (CLI)

## Descripción

Fujifilm Recipes Helper es una aplicación de línea de comandos (CLI) desarrollada en Python que guía al usuario en la creación de una “recipe” completa para cámaras Fujifilm. 

A través de un menú interactivo en consola, la aplicación permite seleccionar:

- Simulación de película (Film Simulation)
- Nivel de grano (Grain Level)
- Color Chrome FX
- Color Chrome Blue FX
- White Balance (incluyendo modo Kelvin con offsets de rojo y azul)
- Dynamic Range
- Highlight
- Shadow
- Sharpness
- High ISO Noise Reduction
- Clarity
- Tipo de ISO (Manual / Auto)

Al finalizar, el programa muestra un resumen con todos los parámetros elegidos, pensado para que el usuario pueda copiar esa configuración en su cámara.

---

## Contexto

Las “recipes” de Fujifilm son combinaciones de ajustes que permiten obtener un look específico directamente en cámara (por ejemplo, simulaciones tipo película analógica, alto contraste, tonos suaves, blanco y negro, etc.). 

Este proyecto nace como una forma de:

- Practicar Python con un tema cercano (fotografía).
- Organizar de manera clara los parámetros típicos de una recipe.
- Crear una herramienta simple que ayude a configurar la cámara sin tener que recordar cada valor manualmente.

La aplicación está centrada en la lógica y la interacción por consola, sin interfaz gráfica.

---

## Características principales

- Menús interactivos en consola para cada parámetro:
  - Film Simulation (Provia, Velvia, Astia, Classic Chrome, Nostalgic Neg, Acros, etc.).
  - Grain Level (Off, Weak/Strong – Small/Large).
  - Color Chrome y Color Chrome Blue (Off, Weak, Strong).
  - White Balance con opción Kelvin, incluyendo offsets de rojo y azul.
  - Dynamic Range (DR100, DR200, DR400).
  - Highlight y Shadow con rangos de -4 a +4 en pasos de 0.5.
  - Sharpness, High ISO NR y Clarity con valores de +4 a -4.
  - Tipo de ISO (Manual / Auto).
- Validación básica de entrada:
  - Verificación de que el usuario ingresa números donde corresponde.
  - Mensajes de error cuando se ingresa un valor inválido.
- Resumen final de la recipe elegida, con todos los parámetros listados de forma ordenada.

---

## Objetivos del proyecto

Este proyecto tiene fines formativos y busca:

- Practicar estructuras de datos en Python (diccionarios anidados).
- Trabajar con ciclos `while` y validación de entrada del usuario.
- Utilizar condicionales (`if/elif/else`) de manera clara.
- Organizar un flujo interactivo completo en consola.
- Crear un pequeño proyecto que pueda mostrarse en un portafolio como Python/QA Junior.

---

## Tecnologías utilizadas

- Python 3.x
- Interfaz de línea de comandos (CLI)

---

## Cómo ejecutar el proyecto

1. Clonar este repositorio o descargar los archivos:
https://github.com/felipeperezcortes/fujifilm-simulation-recipes.git
2. Ejecutar el script principal: fujifilm-recipes-v1.py
3. Seguir las instrucciones en la consola, eligiendo los parámetros de la recipe según las opciones numéricas que se muestran en pantalla.
4. Al final del flujo, se mostrará un resumen con todos los valores seleccionados.
