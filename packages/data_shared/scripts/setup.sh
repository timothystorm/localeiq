#!/usr/bin/env bash

set -e  # Exit on error

ENV_FILE=".env"

echo "🔧 LocaleIQ: First-time setup"
echo "------------------------------------"

# Prompt user with defaults
read -p "Enter pg-admin email [admin@localeiq.com]: " pg_admin_email
pg_admin_email=${pg_admin_email:-admin@localeiq.com}

read -p "Enter pg-admin passord [admin123]: " pg_admin_password
pg_admin_password=${pg_admin_password:-admin123}

read -p "Enter database user [localeiq_user]: " db_user
db_user=${db_user:-localeiq_user}

read -p "Enter database password [localeiq_pass]: " db_pass
db_pass=${db_pass:-localeiq_pass}

read -p "Enter database name [localeiq]: " db_name
db_name=${db_name:-localeiq}

read -p "Enter database port [5432]: " db_port
db_port=${db_port:-5432}

# Force password prompt without echo
# while true; do
#  read -s -p "Enter database password (required): " db_pass
#  echo
#  if [ -n "$db_pass" ]; then
#    break
#  else
#    echo "❌ Password cannot be empty."
#  fi
# done

# Write to .env.docker
cat > $ENV_FILE <<EOF
DATABASE_USER=$db_user
DATABASE_PASSWORD=$db_pass
DATABASE_NAME=$db_name
DATABASE_PORT=$db_port

PGADMIN_DEFAULT_EMAIL=$pg_admin_email
PGADMIN_DEFAULT_PASSWORD=$pg_admin_password
EOF

echo "✅ .env file created successfully!"