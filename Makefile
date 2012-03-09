clean:
		find . -name "*.pyc" -delete

install:
		python setup.py install --record build/files.txt

uninstall:
		cat build/files.txt
		cat build/files.txt | xargs rm -f
