#!/bin/bash

for f in `find SPECS -name "*.spec"`;
do
    echo $f
    rpmbuild -ba $f
done
