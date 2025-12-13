# -----------------------------------------------------------------------------
# Make file for all LocaleIQ Python modules. This file delegates to
# individual module makefiles to perform tasks like testing, linting, and
# setup.
#
# Review the base makefile - ./.makefile_base
# ----------------------------------------------------------------------------
ROOT_DIR := $(shell pwd)
MODULE = $(notdir $(ROOT_DIR))

# ----------------------------------------------------------------------------
# List of all modules in the monorepo (in dependency order)
# ----------------------------------------------------------------------------
MODULE_PATHS = 'packages/utils' 'packages/data_store' 'apps/rest_api' 'apps/cli_tool'

# ----------------------------------------------------------------------------
# Help
#
# Child makefiles can add `help-extra` target to add more help info.
# ----------------------------------------------------------------------------
help:
	@echo "🚑  \033[0;34mLocaleIQ makefile commands:\033[0m"
	@echo "  check       Run lint-check and type-checking"
	@echo "  clean       Clean virtual environments and caches"
	@echo "  lint        Run all linting tasks (type-check, lint-fix, format)"
	@echo "  setup       Lock and install [$(MODULE)] dependencies"
	@echo "  test        Run tests synchronously"
	@echo "  help        Show this help message"

.PHONY: test
test:
	@for mod in $(MODULE_PATHS); do \
  		cd $(ROOT_DIR)/$$mod && make -s test; \
	done

.PHONY: check
check:
	@for mod in $(MODULE_PATHS); do \
  		cd $(ROOT_DIR)/$$mod && make -s check; \
	done

.PHONY: lint
lint:
	@for mod in $(MODULE_PATHS); do \
  		cd $(ROOT_DIR)/$$mod && make -s lint; \
	done

.PHONY: clean
clean:
	@for mod in $(MODULE_PATHS); do \
  		cd $(ROOT_DIR)/$$mod && make -s clean; \
	done

.PHONY: setup
setup:
	@for mod in $(MODULE_PATHS); do \
  		cd $(ROOT_DIR)/$$mod && make -s setup; \
	done
