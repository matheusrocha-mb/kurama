ENV_NAME ?= dev
ENVIRONMENT_VARIABLES=$(shell grep -v '^\#' configs/${ENV_NAME}/env | xargs)

envvars: ## envvars: Export envvars from config
	@echo "export ${ENVIRONMENT_VARIABLES}"