logo.png: ../examples/logo.svg
	scapex --no-fragments $<
	pdftoppm -png -r 300 $(patsubst %.png,%.pdf,$@) > $@
	rm -f $(patsubst %.png,%.pdf,$@)
