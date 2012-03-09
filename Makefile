clean:
		find . -name "*.pyc" -delete

install:
		python setup.py install --record installRecords.txt

uninstall:
		cat installRecords.txt
		cat installRecords.txt | xargs rm -f
