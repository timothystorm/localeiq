# -----------------------------------------------------------------------------
# Make file for all LocaleIQ Python modules.
# ----------------------------------------------------------------------------
ROOT_DIR := $(shell pwd)
MODULE = $(notdir $(ROOT_DIR))

# ----------------------------------------------------------------------------
# List of all modules in the monorepo (in dependency order)
# ----------------------------------------------------------------------------
MODULE_PATHS = 'packages/utils' 'packages/data_shared' 'apps/date_time'

# ----------------------------------------------------------------------------
# Help
#
# Child makefiles can add `help-extra` target to add more help info.
# ----------------------------------------------------------------------------
help:
	@echo "\033[0;34m\033[0;34m[\033[0;33m$(MODULE)\033[0;34m] LocaleIQ makefile commands:\033[0m"
	@echo "  clean       Clean virtual environments and caches"
	@echo "  lint        Run all linting tasks (type-check, lint-fix, format)"
	@echo "  setup       Lock and install [$(MODULE)] dependencies"
	@echo "  test        Run tests synchronously"
	@echo "  help        Show this help message"

test:
	@for mod in $(MODULE_PATHS); do \
  		echo "\033[0;34mtest: \033[0;33m$$mod\033[0;34m...\033[0m"; \
  		cd $(ROOT_DIR)/$$mod && make test; \
	done

lint:
	@for mod in $(MODULE_PATHS); do \
  		echo "\033[0;34mlint: \033[0;33m$$mod\033[0;34m...\033[0m"; \
  		cd $(ROOT_DIR)/$$mod && make lint; \
	done

clean:
	@for mod in $(MODULE_PATHS); do \
  		echo "\033[0;34mclean: \033[0;33m$$mod\033[0;34m...\033[0m"; \
  		cd $(ROOT_DIR)/$$mod && make clean; \
	done

setup:
	@for mod in $(MODULE_PATHS); do \
		echo "\033[0;34msetup: \033[0;33m$$mod\033[0;34m...\033[0m"; \
  		cd $(ROOT_DIR)/$$mod && make setup; \
	done
