# Proyecto: Análisis de Exposición de Dispositivos ICS en IPs Públicas

Este proyecto implementa un flujo completo para identificar dispositivos ICS expuestos de IPs publicas.
El análisis utiliza rangos de direcciones IPv4 representadas en formato decimal, las convierte a direcciones IPv4 estándar y ejecuta un escaneo de puertos industriales mediante `nmap`. Su objetivo es simular un procedimiento de evaluación de exposición para sistemas de control industrial.

---

## Estructura del Proyecto

```
Iot-ICS-Scanner/
├── data/
│   ├── xaj                      Archivo original con rangos de IP en decimal
│   ├── xaj-processed.csv        Archivo procesado con rangos de IP en decimal en formato CSV
│   └── targets_ips.txt          Archivo generado con una IP por línea
├── scripts/
│   ├── convert_ranges_to_ips.py Script que convierte los rangos a IPv4
│   └── scan_ics_ports.sh        Script que ejecuta nmap sobre los puertos ICS
├── results/
│   └── scan_ics_all.nmap        Resultado del escaneo de puertos
```

---

## Requerimientos Previos

Antes de ejecutar los scripts o replicar el análisis, se deben cumplir los siguientes requisitos.

### 1. Sistema Operativo

* Linux (Ubuntu o equivalente)
* También puede funcionar en macOS con ajustes mínimos

### 2. Software Necesario

#### Python 3.8 o superior

Requerido para ejecutar el script que convierte los rangos decimales a direcciones IPv4.

Verificar instalación:

```
python3 --version
```

#### Paquetes estándar de Python

El script utiliza exclusivamente módulos estándar:

* csv
* ipaddress
* pathlib

No se requiere instalar paquetes adicionales.

#### nmap

Requerido para ejecutar el escaneo de puertos industriales.

Instalación en Ubuntu:

```
sudo apt update
sudo apt install nmap
```

Verificar instalación:

```
nmap --version
```

### 3. Permisos de Ejecución

Asignar permisos de ejecución al script de bash:

```
chmod +x scripts/scan_ics_ports.sh
```

---

## Archivos de Entrada

### xaj-processed.csv

Este archivo contiene rangos de direcciones IPv4 en formato decimal:

Ejemplo:

```
"3187944704","3187944959","GT","Guatemala"
```

Cada línea incluye:

* Rango inicial (decimal)
* Rango final (decimal)
* Código de país
* Descripción

---

## Flujo de Trabajo para Ejecutar el Análisis

A continuación se presenta el procedimiento completo para replicar el análisis desde cero.

---

### Paso 1: Convertir los rangos decimales a direcciones IPv4

Ejecutar el script de conversión:

```
python3 scripts/convert_ranges_to_ips.py
```

Acciones realizadas:

1. Lee los rangos desde `xaj-processed.csv`
2. Convierte cada valor decimal a dirección IPv4
3. Expande cada rango a una lista completa de IPs
4. Genera el archivo:

```
data/targets_ips.txt
```

Este archivo contendrá una IP por línea.

---

### Paso 2: Ejecutar el escaneo de puertos ICS

Una vez generada la lista de direcciones IP, ejecutar:

```
./scripts/scan_ics_ports.sh
```

El script:

1. Lee todas las direcciones desde `data/targets_ips.txt`
2. Ejecuta `nmap` sobre los puertos ICS especificados:

   * 502 (Modbus)
   * 102 (Siemens S7)
   * 44818 (Allen-Bradley)
   * 2222 (Allen-Bradley)
   * 20548 (Schleicher XCX 300)
   * 9600 (Omron PLC)
   * 28784 (Koyo Ethernet)
   * 57176 (GE QuickPanels)
   * 2004 (LS)
   * 3306 (MySQL)
   * 1433 (MSSQL)
   * 445 (Microsoft SMB)
3. Genera un archivo consolidado con todos los resultados:

```
results/scan_ics_all.nmap
```

---

### Paso 3: Interpretación de Resultados

El archivo `scan_ics_all.nmap` contendrá la salida completa del escaneo.
A partir de este archivo se deben identificar:

* Direcciones IP que tienen puertos ICS abiertos
* Servicios detectados por nmap
* Versiones o banners mostrados
* Posibles tipos de dispositivos ICS simulados

La información obtenida se utilizará para complementar el informe ubicado en PDF:

```
report/Informe.pdf
```

---

## Consideraciones Importantes

* Este proyecto está diseñado únicamente para uso en laboratorio.
* No debe ejecutarse en redes reales sin autorización explícita.
* Los datos utilizados son simulados y fueron expuestos con fines académicos.
* Los scripts están diseñados para facilitar la automatización del proceso de evaluación y documentación.

---

## Autores y Créditos

Este proyecto forma parte de la práctica del curso de Fundamentos de IoT.
Incluye creación de scripts, análisis de exposición y elaboración de informe técnico.

Autor: Eriksson Hernández  
Correo: erikssonhernandez25@gmail.com