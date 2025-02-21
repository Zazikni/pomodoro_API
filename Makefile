.DEFAULT_GOAL := help

HOST ?= 0.0.0.0
PORT ?= 8000

run: ## Run the application using uvicorn with provided arguments or defaults
	poetry run uvicorn main:app --host $(HOST) --port $(PORT) --reload --env-file .env

run_pg: ## Run the application using uvicorn with provided arguments or defaults
	docker compose up -d pg

help: ## Show this help message
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands: "
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $1, $2}'