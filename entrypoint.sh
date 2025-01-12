#!/bin/bash

# Esperar a que la base de datos esté disponible
echo "Esperando a que la base de datos esté disponible..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "Base de datos disponible!"

# Aplicar migraciones
python manage.py migrate

# Crear superusuario si no existe
python manage.py createsuperuser --noinput || true

# Iniciar Tailwind en segundo plano si es el servicio tailwind
if [ "$1" = "python" ] && [ "$3" = "tailwind" ]; then
    echo "Iniciando Tailwind..."
    exec python manage.py tailwind start
fi

# Ejecutar el comando que se pasa como argumento
exec "$@" 