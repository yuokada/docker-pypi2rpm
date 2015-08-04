#!/bin/bash

rm ./SOURCES/*

wget https://pypi.python.org/packages/source/n/numpy/numpy-1.9.2.tar.gz           -P ./SOURCES/
wget https://pypi.python.org/packages/source/s/scipy/scipy-0.16.0.tar.gz          -P ./SOURCES/

wget https://pypi.python.org/packages/source/n/nose/nose-1.3.7.tar.gz             -P ./SOURCES/
wget https://pypi.python.org/packages/source/b/boto/boto-2.38.0.tar.gz            -P ./SOURCES/
wget https://pypi.python.org/packages/source/s/simplejson/simplejson-3.8.0.tar.gz -P ./SOURCES/
wget https://pypi.python.org/packages/source/m/mrjob/mrjob-0.4.5.tar.gz           -P ./SOURCES/
wget https://pypi.python.org/packages/source/f/filechunkio/filechunkio-1.6.tar.gz -P ./SOURCES/
wget https://pypi.python.org/packages/source/P/PyYAML/PyYAML-3.11.tar.gz          -P ./SOURCES/

# for f in `find SPECS -name "*.spec"`;
# do
#     echo $f
#     rpmbuild -bb $f
# done
