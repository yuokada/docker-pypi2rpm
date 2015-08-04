
SAVE_DIR=SPECS

spec::
	pyp2rpm -n boto        --srpm -d ${SAVE_DIR}
	pyp2rpm -n mrjob       --srpm -d ${SAVE_DIR}
	pyp2rpm -n simplejson  --srpm -d ${SAVE_DIR}
	pyp2rpm -n filechunkio --srpm -d ${SAVE_DIR}
	pyp2rpm -n PyYAML      --srpm -d ${SAVE_DIR}

fetch:
	rm -f ./SOURCES/*.gz
	wget https://pypi.python.org/packages/source/b/boto/boto-2.38.0.tar.gz            -P ./SOURCES/
	wget https://pypi.python.org/packages/source/s/simplejson/simplejson-3.8.0.tar.gz -P ./SOURCES/
	wget https://pypi.python.org/packages/source/m/mrjob/mrjob-0.4.5.tar.gz           -P ./SOURCES/
	wget https://pypi.python.org/packages/source/f/filechunkio/filechunkio-1.6.tar.gz -P ./SOURCES/
	wget https://pypi.python.org/packages/source/P/PyYAML/PyYAML-3.11.tar.gz          -P ./SOURCES/


build::
	find SPECS -name "*.spec" -exec rpmbuild -bb {} \;
