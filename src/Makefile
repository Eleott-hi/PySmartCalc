
PYBIND11_INCLUDE := $(shell python3 -m pybind11 --includes)
BUILD_DIR := build

all: run

compile:
	g++ -O3 -Wall -shared -std=c++11 -undefined dynamic_lookup $(PYBIND11_INCLUDE) example.cpp -o example$(python3-config --extension-suffix)

build:
	cmake -S . -B $(BUILD_DIR)
	cmake --build $(BUILD_DIR) -j 2

env:
	python3 -m venv env
	@echo
	@echo source env/bin/activate
	@echo
	@exit 1

dev:
	sudo apt install python3-dev

pip:
	pip install --upgrade pip
#	pip install -r requirements.txt

py:
	python3 main.py

run: build_python py

build_python: env pip
	 python -m pip install .

clean:
	rm -rf $(BUILD_DIR) *.egg-info env/ 

.PHONY: all compile build dev pip
