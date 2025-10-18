[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21147949&assignment_repo_type=AssignmentRepo)
# Proyecto integrador 1ra Entrega

## Integrantes

- [Michael Handrety Fonseca Arana](https://github.com/MichaelJF50)
- [Laura Daniela Rincón Pinilla](https://github.com/Laura03rincon)

## Arquitectura propuesta

Este proyecto permite controlar una bomba peristáltica mediante comunicación MQTT utilizando un ESP32.
El sistema automatiza el inicio y la detención de la bomba según señales enviadas por otros dispositivos en el proceso de mezclado (usuario y galga).

## ⚙️ Funcionamiento General

### 🟢 Inicio del proceso
- El **usuario selecciona el color de pintura** que desea dosificar.  
- Se envía un **mensaje MQTT** con el tema `bomba/control` y el valor `ON`.  
- El **ESP32 enciende la bomba peristáltica** (salida en el pin **GPIO 32**) y el **LED indicador** (pin **GPIO 2**).  

### 🔴 Finalización del proceso
- Cuando la **galga detecta que se alcanzó el peso indicado**, envía un **mensaje MQTT** con el tema `bomba/control` y el valor `OFF`.  
- El **ESP32 apaga la bomba** y publica el estado `APAGADA` en el tema `bomba/estado`.  

<p align="center">
  <img src="./Digitales III.png" alt="Logo" width="800"/>
</p>


## Periférico a trabajar

[![Ver video en YouTube](https://img.youtube.com/vi/rzbVd6A8gA8/hqdefault.jpg)](https://youtube.com/shorts/rzbVd6A8gA8)

<p align="center">
  <img src="./Fuente.jpeg" alt="Logo" width="800"/>
</p>

<p align="center">
  <img src="./Bomba.jpeg" alt="Logo" width="800"/>
</p>

## Avances

<!-- Subir en una carpeta src los códigos que tienen hasta el momento y esta sección agregar lo que consideren necesario referente a sus avances. -->

<p align="center">
  <img src="./Codigo.jpeg" alt="Logo" width="800"/>
</p>

<p align="center">
  <img src="./Wifi.jpeg" alt="Logo" width="800"/>
</p>

<p align="center">
  <img src="./Node red.jpeg" alt="Logo" width="800"/>
</p>

<p align="center">
  <img src="./Control.jpeg" alt="Logo" width="800"/>
</p>
