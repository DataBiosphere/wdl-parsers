all: generate clean-extras

generate:
	python generate.py -v all

# clean everything except the generated files.
clean-extras:
	find . -type f \( -name '*.jar' \) -delete
	find . -type f \( -name '*.g4' -or -name '*.hgr' \) -delete
	find . -type f \( -name '*.interp' -or -name '*.tokens' \) -delete

# clean everything including the generated files
clean: clean-extras
	cd wdlparse && find . -type f \( -name 'Wdl*.py' -or -name 'wdl_parser.py' \) -delete
