-include ../../.makefile_base

# ----------------------------------------------------------------------------
# Database migrations (Alembic)
# ----------------------------------------------------------------------------
migrate-base:
	@poetry run alembic downgrade base

migrate-down:
	@poetry run alembic downgrade -1

migrate-head:
	@poetry run alembic upgrade head

migrate-revision:
	@poetry run alembic revision --autogenerate -m "$(m)"

migrate-up:
	@poetry run alembic upgrade +1

seed-locales:
	@poetry run python -c "from data_store.seed_data import seed_locales; seed_locales()"

help-extra:
	@echo "  migrate-base     🔥  Migrate database to base (empty database) !!"
	@echo "  migrate-down     ➖  Migrate database down one revision"
	@echo "  migrate-up       ➕  Migrate database up one revision"
	@echo "  migrate-head     🚀  Migrate database to latest revision"
	@echo "  migrate-revision 🚧  Create new migration revision with message 'm'"
	@echo "                   Usage: make migrate-revision m='revision_message'"
	@echo "                   Note: make sure new schema are listed in src/data_store/schema/__init__.py"
	@echo "  seed-locales     🌱  Seed locales into database"