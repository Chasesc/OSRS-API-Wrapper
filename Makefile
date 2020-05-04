.PHONY: build clean test_pub pub dev

build:
	make clean
	python3 setup.py sdist bdist_wheel

clean:
	rm -rf __pycache__/
	rm -rf dist
	rm -rf build
	rm -rf python_osrsapi.egg-info/

test_pub:
	pip3 install --upgrade twine
	python3 -m twine upload --repository testpypi dist/*

pub:
	pip3 install --upgrade twine
	python3 -m twine upload dist/*

dev:
	pip3 install -e .