all: package

clean:
		find . -name "*.pyc" -delete
		rm fu

install:
		python setup.py install --record installRecords.txt
		rm -f src/fu

uninstall:
		cat installRecords.txt
		cat installRecords.txt | xargs rm -f

package:
		cd src && zip ../fu.zip fu.py lib/*.py
		cat src/fu.head fu.zip > fu
		chmod +x fu
		rm fu.zip
