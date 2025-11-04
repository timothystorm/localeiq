#!/usr/bin/env bash

# Generate local .env file for local development

set -e  # Exit on error

ENV_FILE=".env"

echo "🔧 LocaleIQ: First-time setup"
echo "------------------------------------"

# Prompt user with defaults
read -p "Enter pgadmin email [admin@localeiq.com]: " pg_admin_email
pg_admin_email=${pg_admin_email:-admin@localeiq.com}

read -p "Enter pgadmin passord [admin123]: " pg_admin_password
pg_admin_password=${pg_admin_password:-admin123}

read -p "Enter database user [postgres]: " db_user
db_user=${db_user:-postgres}

#read -p "Enter database password [localeiq123]: " db_pass
#db_pass=${db_pass:-localeiq123}

read -p "Enter database name [localeiq]: " db_name
db_name=${db_name:-localeiq}

read -p "Enter database port [5432]: " db_port
db_port=${db_port:-5432}

# Force password prompt without echo
 while true; do
  read -r -s -p "Enter database password (required): " db_pass
  echo
  if [ -n "$db_pass" ]; then
    break
  else
    echo "❌ Password cannot be empty."
  fi
 done

# Write to .env
cat > $ENV_FILE <<EOF
# Auto-generated .env file for LocaleIQ
# Do not share this file publicly.
# Generated on: $(date)

# PostgreSQL Database Configuration
DATABASE_USER=$db_user
DATABASE_PASSWORD=$db_pass
DATABASE_NAME=$db_name
DATABASE_PORT=$db_port

# PGAdmin Credentials
PGADMIN_DEFAULT_EMAIL=$pg_admin_email
PGADMIN_DEFAULT_PASSWORD=$pg_admin_password
EOF

echo "✅ .env file created successfully!"
