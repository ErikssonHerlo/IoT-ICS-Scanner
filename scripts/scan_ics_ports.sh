#!/usr/bin/env bash
# Script: scan_ics_ports.sh
# Descripción:
#   Lee la lista de IPs desde results/targets_ips.txt y ejecuta nmap
#   contra los puertos ICS definidos para identificar servicios expuestos.

set -euo pipefail

# Resolver rutas relativas al directorio raíz del proyecto
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGETS_FILE="$BASE_DIR/results/targets_ips.txt"
RESULTS_DIR="$BASE_DIR/results"
OUTPUT_FILE="$RESULTS_DIR/scan_ics_all.nmap"

# Puertos a escanear (ICS + servicios relacionados)
PORTS="502,102,44818,2222,20548,9600,28784,57176,2004,3306,1433,445"

# Verificaciones básicas
if [[ ! -f "$TARGETS_FILE" ]]; then
  echo "No se encontró el archivo de targets: $TARGETS_FILE"
  echo "Primero ejecuta el script convert_ranges_to_ips.py"
  exit 1
fi

mkdir -p "$RESULTS_DIR"

echo "Iniciando escaneo Nmap..."
echo "Targets: $TARGETS_FILE"
echo "Puertos: $PORTS"
echo "Salida:  $OUTPUT_FILE"
echo

# Comando nmap:
# -sV : detección de versión de servicio
# -Pn : no hacer ping previo (asume host up / evita que algunos no respondan)
# -n  : no resolver DNS (más rápido)
# -p  : lista de puertos
# -iL : archivo con lista de IPs
# -oN : salida en formato normal de nmap
nmap -sV -Pn -n -p "$PORTS" -iL "$TARGETS_FILE" -oN "$OUTPUT_FILE"

echo
echo "Escaneo finalizado."
echo "Revisa el archivo de resultados: $OUTPUT_FILE"
