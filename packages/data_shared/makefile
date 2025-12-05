-include ../../makefile

migrate-up:
	@poetry run alembic upgrade head

migrate-down:
	@poetry run alembic downgrade -1

migrate-version:
	@poetry run alembic revision --autogenerate -m "$(m)"

help-extra:
	@echo "  migrate-up       Migrate database to latest revision"
	@echo "  migrate-down     Migrate database down one revision"
	@echo "  migrate-version  Create new migration revision with message 'm'"