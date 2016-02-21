# dockerfile-pypi2rpmbuild


## get results

```
$ sudo docker cp <container id>:/rpmbuild/RPMS/ results
```


```
 rpmbuild SPECS/python-mrjob.spec
sh: 1: TODO:: not found
sh: 1: TODO:: not found
error: File /root/rpmbuild/SOURCES/mrjob-0.4.5.tar.gz: No such file or directory
```


docker-running
--------------

こんな感じでコンテナを起動してexecで侵入。

```
$ cd fpm
$ docker build -t fpm_dev .
$ docker run -v `pwd`/..:/root/data -d -it fpm_dev
269ded7604fd1173de218d8ff7fb90d8c3b4cb277b6972e1756b3e6133d812c9
$ docker exec  -it $(docker ps  -l -q) /bin/bash
$ docker commit $(docker ps  -l -q) fpm_dev
$ docker images |grep fpm
fpm_dev                   latest              54a2df12fb18        31 minutes ago      593.2 MB
```


Link
-----

- [Docker 虎の巻](https://gist.github.com/tcnksm/7700047 "Docker 虎の巻")
