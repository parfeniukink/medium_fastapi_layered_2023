
# ************************************************
# ********** piptools **********
# ************************************************

.PHONY: lock  # pin main dependencies
lock:
	python -m piptools compile -o requirements/main.txt


.PHONY: lock.dev  # pin dev dependencies
lock.dev:
	python -m piptools compile --extra dev -o requirements/dev.txt


.PHONY: lock.all  # pin all dependencies
lock.all: lock lock.dev


.PHONY: sync  # sync for main dependencies
sync:
	python -m piptools sync requirements/main.txt


.PHONY: sync.dev  # sync for dev dependencies
sync.dev:
	python -m piptools sync requirements/dev.txt


.PHONY: update  # lock and sync to the latest dev state
update: lock.all sync.dev


.PHONY: upgrade  # upgrade main dependencies. Generate new .txt file
upgrade:
	python -m piptools compile --upgrade -o requirements/main.txt


.PHONY: upgrade.dev  # upgrade dev dependencies. Generate new .txt file
upgrade.dev:
	python -m piptools compile --extra dev --upgrade -o requirements/dev.txt


.PHONY: upgrade.all  # upgrade all dependencies. Generate new .txt files
upgrade.all: upgrade upgrade.dev




# ************************************************
# ********** migrations **********
# ************************************************
.PHONY: migration.revision
migration.revision:
	alembic revision --autogenerate


.PHONY: migration.sync
migration.sync:
	alembic upgrade head




# ************************************************
# ********** application **********
# ************************************************

.PHONY: run  # run the application in a prod mode
run:
	# NOTE:configurable via environment variables
	gunicorn src.main:app --worker-class uvicorn.workers.UvicornWorker


.PHONY: run.dev  # run the application in a dev mode
run.dev:
	# NOTE:configurable via environment variables
	uvicorn src.main




# *************************************************
# ********** code quality **********
# *************************************************

.PHONY: format  # fix formatting / and order imports
format:
	python -m black .
	python -m isort .


.PHONY: check.types  # check type annotations
types:
	python -m mypy --check-untyped-defs .


.PHONY: check  # check everything
check:
	python -m ruff .
	python -m black --check .
	python -m isort --check .
	python -m mypy --check-untyped-defs .
	python -m pytest .



# *************************************************
# ********** tests **********
# *************************************************

.PHONY: tests  # run all tests
tests:
	python -m pytest -vvv -x ./src/tests

.PHONY: tests.unit  # run unit tests
tests.unit:
	python -m pytest -vvv -x ./src/tests/unit

.PHONY: tests.integration  # run integration tests
tests.integration:
	python -m pytest -vvv -x ./src/tests/integration

