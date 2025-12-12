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
MODULE_PATHS = 'packages/utils' 'packages/data_shared' 'apps/date_time'

# ----------------------------------------------------------------------------
# Help
#
# Child makefiles can add `help-extra` target to add more help info.
# ----------------------------------------------------------------------------
help:
	@echo "🚑  \033[0;34mLocaleIQ makefile commands:\033[0m"
	@echo "  clean       Clean virtual environments and caches"
	@echo "  lint        Run all linting tasks (type-check, lint-fix, format)"
	@echo "  setup       Lock and install [$(MODULE)] dependencies"
	@echo "  test        Run tests synchronously"
	@echo "  help        Show this help message"

test:
	@for mod in $(MODULE_PATHS); do \
  		cd $(ROOT_DIR)/$$mod && make -s test; \
	done

lint:
	@for mod in $(MODULE_PATHS); do \
  		cd $(ROOT_DIR)/$$mod && make -s lint; \
	done

clean:
	@for mod in $(MODULE_PATHS); do \
  		cd $(ROOT_DIR)/$$mod && make -s clean; \
	done

setup:
	@for mod in $(MODULE_PATHS); do \
  		cd $(ROOT_DIR)/$$mod && make -s setup; \
	done
