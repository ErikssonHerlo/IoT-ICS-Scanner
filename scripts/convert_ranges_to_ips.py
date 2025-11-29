"""
Script: convert_ranges_to_ips.py
Descripción:
  Lee el archivo data/xaj.csv que contiene rangos de direcciones IPv4 en formato decimal
  y genera un archivo data/targets_ips.txt con todas las direcciones IPv4 (una por línea).

Formato esperado de cada línea en xaj-processed.csv
"3187944704","3187944959","GT","Guatemala"
"""

import csv
from ipaddress import IPv4Address
from pathlib import Path

# Rutas de entrada/salida
BASE_DIR = Path(__file__).resolve().parent.parent / "data"
INPUT_FILE = BASE_DIR / "xaj-processed.csv"
OUTPUT_FILE = BASE_DIR / "targets_ips.txt"


def decimal_to_ipv4(dec_value: int) -> str:
    """
    Convierte un entero (ej. 3187944704) a IPv4 (ej. 190.4.45.0).
    """
    return str(IPv4Address(dec_value))


def main() -> None:
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo de entrada: {INPUT_FILE}")

    ranges = []
    with INPUT_FILE.open("r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            try:
                start_dec = int(row[0])
                end_dec = int(row[1])
                ranges.append((start_dec, end_dec))
            except (ValueError, IndexError):
                # Si alguna fila no cumple formato, puedes loguearla o ignorarla
                print(f"Fila inválida o no estándar, se omite: {row}")
                continue

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    total_ips = 0
    with OUTPUT_FILE.open("w") as out:
        for start_dec, end_dec in ranges:
            if end_dec < start_dec:
                print(
                    f"Rango inválido (fin < inicio): {start_dec} - {end_dec}")
                continue

            for dec in range(start_dec, end_dec + 1):
                ip_str = decimal_to_ipv4(dec)
                out.write(ip_str + "\n")
                total_ips += 1

    print(f"Se procesaron {len(ranges)} rangos.")
    print(f"Total de IPs generadas: {total_ips}")
    print(f"Archivo de salida: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
