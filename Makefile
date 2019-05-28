# Makefile for crypot
TEST_PATH=./tests/

## Default commit message
m='Update crypot'


help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "		clean-pyc		to remove the object files"
	@echo "		test			to pyTest the unittest"
	@echo "		git				m="commit message"; add *, commit with m and push
	@echo "		status			git status"	

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	name '*~' -exec rm --force  {} 

test:
	clean-pyc
	py.test --verbose --color=yes $(TEST_PATH)

test -setup:
	clean-pyc
 
# usage guideline: make git m="commit message"
git: 
	@git status
	git add .
	sleep 2
	@git status
	git commit -m "$m"
	git push

status:
	@git status