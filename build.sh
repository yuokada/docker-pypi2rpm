#!/bin/bash

# wget https://pypi.python.org/packages/source/b/boto/boto-2.38.0.tar.gz
# wget https://pypi.python.org/packages/source/s/simplejson/simplejson-3.8.0.tar.gz
# wget https://pypi.python.org/packages/source/m/mrjob/mrjob-0.4.5.tar.gz
# wget https://pypi.python.org/packages/source/f/filechunkio/filechunkio-1.6.tar.gz
# wget https://pypi.python.org/packages/source/P/PyYAML/PyYAML-3.11.tar.gz
#
# mkdir       SOURCES
# mv *.tar.gz SOURCES

for f in `find SPECS -name "*.spec"`;
do
    echo $f
    rpmbuild -bb $f
done
