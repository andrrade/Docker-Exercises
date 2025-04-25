#!/bin/bash

PURPLE='\033[0;35m'
DEFAULT='\033[0m'

echo -e "${PURPLE}Atualizando pacotes...${DEFAULT}"
apt update && apt upgrade -y
echo ""

echo -e "${PURPLE}=== Logs do Sistema ===${DEFAULT}"
echo "Data e Hora (Brasil): $(date '+%d/%m/%Y %H:%M:%S')"
echo ""

bash