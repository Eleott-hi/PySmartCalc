
PYBIND11_INCLUDE := $(shell python3 -m pybind11 --includes)

all: run

compile:
	g++ -O3 -Wall -shared -std=c++11 -fPIC $(PYBIND11_INCLUDE) 	example.cpp -o example`python3-config --extension-suffix`

env:
	python3 -m venv env
	echo source env/bin/activate

dev:
	sudo apt install python3-dev

pip:
	pip install --upgrade pip
	pip install -r requirements.txt

py:
	python3 main.py

run: compile py