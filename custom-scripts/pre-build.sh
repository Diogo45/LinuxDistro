#!/bin/sh
  
cp $BASE_DIR/../custom-scripts/S41network-config $BASE_DIR/target/etc/init.d
chmod +x $BASE_DIR/target/etc/init.d/S41network-config

cp $BASE_DIR/../custom-scripts/S50server $BASE_DIR/target/etc/init.d
cp $BASE_DIR/../custom-scripts/simple_http_server.py $BASE_DIR/target/usr/bin
chmod +x $BASE_DIR/target/etc/init.d/S50server

#Compile the syscall_test.c
  BUILDROOT_DIR=$BASE_DIR/..
  COMPILER=$BUILDROOT_DIR/output/host/bin/i686-buildroot-linux-uclibc-gcc
  $COMPILER -o $BUILDROOT_DIR/output/target/bin/syscall_test $BUILDROOT_DIR/custom-scripts/syscall_test.c

make -C $BASE_DIR/../modules/simple_driver/

make -C $BASE_DIR/../modules/sstf-iosched-skeleton/
