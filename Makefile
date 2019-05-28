# Makefile for crypot
TEST_PATH=./tests/

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	name '*~' -exec rm --force  {} 

test:
	clean-pyc
	py.test --verbose --color=yes $(TEST_PATH)

# usage guideline: make git m="commit message"
git:
	git status
	git add .
	sleep 2
	git status
	git commit -m "$m"
	git push