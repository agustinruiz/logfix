# Makefile

# Main variables
MAIN_SCRIPT = src/logfix.py
TEST_SCRIPT = tests/logfix_test.py

default: run

run:
	python3 $(MAIN_SCRIPT)

test:
	python3 $(TEST_SCRIPT)