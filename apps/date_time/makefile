-include ../../.makefile_base

# ----------------------------------------------------------------------------
# Server startup - dev only!
#
# Ensure uvicorn is installed in the module's poetry environment.
# ----------------------------------------------------------------------------
start:
	@echo "\033[0;34m[\033[0;33m$(MODULE)\033[0;34m] Starting development server (Ctrl + C to stop)...\033[0m"
	@poetry run uvicorn date_time.main:app --reload --host 0.0.0.0 --port 8000

help-extra:
	@echo "  start       Start development sever"