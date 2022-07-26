#!/bin/bash

# This script builds Python 3.6.3 with OpenSSL and SQLite3

function print_usage {
    echo 'Usage: build-python.sh [-b <build_dir>] [-i <install_dir>] [-S] [-Q] [-h]
    -i <install_dir>    : installation directory, default ./install
    -b <build_dir>      : build directory, default ./build
    -S                  : skip building SSL (if already done)
    -Q                  : skip building SQLITE3 (if already done)
'
    exit
}

here=$PWD
build=build
install=install

while getopts :b:i:SQh opt; do
    case $opt in
        b)  build=$OPTARG ;;
        i)  install=$OPTARG ;;
        S)  skip_ssl=1 ;;
        Q)  skip_sqlite=1 ;;
        h)  print_usage ;;
        \?) echo "Invalid option: -$OPTARG" >&2 ;;
    esac
done

install=$(realpath $install)
mkdir -p $install
build=$(realpath $build)
mkdir -p $build
cd $build

openssl=openssl-1.1.0e
sqlite=sqlite-autoconf-3240000
python=Python-3.7.3

# openssl
[ $skip_ssl = 1 ] || (
    wget https://www.openssl.org/source/old/1.1.0/$openssl.tar.gz
    rm -rf $openssl
    tar -zxf $openssl.tar.gz
    cd openssl-1.1.0e
    ./config --prefix=$install/$openssl
    make
    make install
) |& tee openssl.log

# sqlite3
[ $skip_sqlite = 1 ] || (
    wget https://sqlite.org/2018/$sqlite.tar.gz
    rm -rf $sqlite
    tar -zxvf  $sqlite.tar.gz
    cd $sqlite
    ./configure --prefix=$install/python3.6.3
    make
    make install
) |& tee sqlite3.log

# python3.7.3
(
    wget https://www.python.org/ftp/python/3.7.3/$python.tgz
    rm -rf $python
    tar -zxf $python.tgz
    cd $python
    LDFLAGS="-L $$install/python3.7.3/lib"
    CPPFLAGS="-I $$install/python3.7.3/include"
    export SSL_DIR=$install/$openssl
    patch setup.py $here/setup.py.patch
    ln -s $install/$openssl/include/openssl
    ./configure --prefix=$install/python3.7.3
    make
    make install
) |& tee python.log