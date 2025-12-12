#!/usr/bin/env bash

set -e  # Exit on error

ENV_FILE=".env"

# If .env exists, warn and ask user whether to overwrite
if [ -f "$ENV_FILE" ]; then
  echo "⚠️  $ENV_FILE already exists and will be overwritten."
  while true; do
    read -rp "Overwrite [y/N]: " answer
    answer=${answer:-N}
    case "$answer" in
      [Yy]* )
        backup="${ENV_FILE}.backup.$(date +%Y%m%d%H%M%S)"
        if cp "$ENV_FILE" "$backup"; then
          echo "Backup created at \`$backup\`"
        else
          echo "Warning: failed to create backup; proceeding with overwrite."
        fi
        break
        ;;
      [Nn]*|"" )
        echo "Aborted. Existing $ENV_FILE preserved."
        exit 0
        ;;
      * )
        echo "Please answer Y or N."
        ;;
    esac
  done
fi

echo "🔧 LocaleIQ: First-time setup"
echo "------------------------------------"

# Prompt user with defaults
read -p "Enter pg-admin email [admin@localeiq.com]: " pg_admin_email
pg_admin_email=${pg_admin_email:-admin@localeiq.com}

read -p "Enter pg-admin password [admin123]: " pg_admin_password
pg_admin_password=${pg_admin_password:-admin123}

read -p "Enter database user [localeiq_user]: " db_user
db_user=${db_user:-localeiq_user}

read -p "Enter database password [localeiq_pass]: " db_pass
db_pass=${db_pass:-localeiq_pass}

read -p "Enter database name [localeiq]: " db_name
db_name=${db_name:-localeiq}

read -p "Enter database host [localhost]: " db_host
db_host=${db_host:-localhost}

read -p "Enter database port [5432]: " db_port
db_port=${db_port:-5432}

# Write to .en
cat > "$ENV_FILE" <<EOF
DB_USER=$db_user
DB_PASSWORD=$db_pass
DB_NAME=$db_name
DB_HOST=$db_host
DB_PORT=$db_port
DB_URL="postgresql://\${DB_USER}:\${DB_PASSWORD}@\${DB_HOST}:\${DB_PORT}/\${DB_NAME}"
PGADMIN_EMAIL=$pg_admin_email
PGADMIN_PASSWORD=$pg_admin_password
EOF

echo "✅ .env file created successfully!"
