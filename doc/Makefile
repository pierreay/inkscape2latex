logo.png: ../examples/logo.svg
	inkscape2latex-ng --no-fragments $<
	pdftoppm -png -r 300 $(patsubst %.png,%.pdf,$@) > $@
	rm -f $(patsubst %.png,%.pdf,$@)
