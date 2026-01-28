# Simulación de Telemetría IoT con Python y ThingsBoard

[English](./README_IOT.md)

Este repositorio contiene una simulación sencilla de telemetría IoT desarrollada en Python.  
El script emula un sensor de temperatura generando valores aleatorios y enviándolos periódicamente a la plataforma ThingsBoard Cloud mediante su API REST.

El proyecto tiene fines educativos y muestra el flujo básico de datos IoT:

Dispositivo → Internet → Plataforma IoT (ThingsBoard)

---

## Descripción del proyecto

El script principal (`telemetria.py`) simula un sensor de temperatura:

- Genera valores aleatorios entre 18°C y 32°C.
- Envía los datos cada 5 segundos a ThingsBoard.
- Utiliza un token de dispositivo para autenticarse.
- Publica la telemetría mediante peticiones HTTP POST.

Aunque se utiliza un script en Python en lugar de un sensor físico, el comportamiento lógico es equivalente al de un dispositivo IoT real.

---

## Estructura del repositorio

```
.
├── telemetria.py          # Script principal de telemetría
├── requirements.txt      # Dependencias de Python
├── token.txt.example     # Ejemplo del archivo de token
├── token.txt             # Token real (ignorado por git)
├── .gitignore
├── LICENSE
├── README.md
└── README_es.md
```

---

## Requisitos

- Python 3.x
- Conexión a Internet
- Cuenta en ThingsBoard Cloud (demo o local)

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Configuración

1. Crear un dispositivo en ThingsBoard (por ejemplo en https://demo.thingsboard.io).
2. Copiar el token del dispositivo.
3. Crear un archivo `token.txt` en la raíz del proyecto.
4. Pegar el token dentro del archivo.

Puedes usar `token.txt.example` como referencia.

Nota importante:  
El archivo `token.txt` está excluido del repositorio para evitar exponer credenciales.

---

## Ejecución

Ejecutar:

```bash
python telemetria.py
```

El programa:

- Genera un valor de temperatura.
- Lo envía a ThingsBoard.
- Repite el proceso cada 5 segundos.

Los datos aparecerán en el panel de ThingsBoard.

Para detener el programa: `Ctrl + C`.

---

## Notas

- El intervalo de 5 segundos es solo para pruebas. En sistemas reales suele ser mayor.
- En entornos de producción normalmente se utiliza MQTT en lugar de HTTP.

---

## Licencia

Este proyecto utiliza la licencia Apache 2.0.  
Consulta el archivo `LICENSE` para más información.

---

## Uso educativo

Este repositorio forma parte de una práctica académica de IoT y sirve para demostrar:

- Envío básico de telemetría
- Comunicación mediante API REST
- Autenticación con token
- Integración con una plataforma IoT

## Equipo

Este proyecto ha sido realizado por:

- **Daniel Carrasco** 
  [GitHub](https://github.com/CarrasDev) | [LinkedIn](https://www.linkedin.com/in/danielcarrascoluque/)

- **Vanesa Sierra** 
  [GitHub](https://github.com/SierraTrace) | [LinkedIn](https://www.linkedin.com/in/vanesasierra/)

- **Raul Estevez** 
  [GitHub](https://github.com/RaulEstevezA) |[LinkedIn](https://www.linkedin.com/in/raulesteveza/)

