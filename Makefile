PROJECTNAME=transnb
SRCPATH := $(CURDIR)/src
BUILDPATH := $(CURDIR)/_build
COVERAGEPATH := $(BUILDPATH)/coverage
REQUIREMENTS_RESULT := $(BUILDPATH)/requirements.txt


.PHONY: clean
clean:
	rm -rf $(BUILDPATH)
	find $(SRCPATH) -name "*.pyc" -delete
	find $(SRCPATH) -type d -name __pycache__ -delete


.PHONY: build_dirs
build_dirs: $(BUILDPATH)

$(BUILDPATH):
	mkdir -p $(BUILDPATH)
	# Also need to make the coverage path as coverage complains if it doesnt exist already
	mkdir -p $(COVERAGEPATH)


# --- Setup ---
.PHONY: requirements
requirements: $(REQUIREMENTS_RESULT)

$(REQUIREMENTS_RESULT): setup.py $(SRCPATH)/requirements/*.txt | build_dirs
	pip install -U pip wheel setuptools
	pip install --upgrade --requirement $(SRCPATH)/requirements/development.txt
	pip freeze > $@


.PHONY: setup
setup: clean requirements


.PHONY: install-git-hooks
install-git-hooks: $(CURDIR)/.git/hooks/pre-commit


$(CURDIR)/.git/hooks/%: $(CURDIR)/git_hooks/%
	ln -s "$<" "$@"


# --- Formatting ---
.PHONY: lint
lint: requirements
	flake8 $(SRCPATH) --tee --output $(BUILDPATH)/lint.txt


.PHONY: check-format
check-format: requirements
	isort -c $(SRCPATH)
	black --check $(SRCPATH)


.PHONY: format
format: requirements
	isort $(SRCPATH)
	black $(SRCPATH)


# --- Testing ---
.PHONY: test
test: requirements lint check-format unittest inttest


.PHONY: unittest
unittest: requirements
	pytest $(SRCPATH) --ignore=$(SRCPATH)/transnb/tests/test_integration.py


.PHONY: inttest
inttest: requirements
	pytest $(SRCPATH)/transnb/tests/test_integration.py


# --- Other stuff ---
.PHONY: messages
messages: requirements
	transnb-all > src/transnb/tests/expected_message_list.txt
