#!/bin/bash
NOW=$(date +"%Y-%m-%d-%H:%M")
FILE="connectfirst.com.$NOW.tar"
BACKUP_DIR="/home/website/backups"
WWW_DIR="/var/www/html/"
REMOTE_DIR="/home/website/backups"

DB_USER="root"
DB_PASS="redhat"
DB_NAME="cfwpdb_new"
DB_FILE="connectfirst.com.$NOW.sql"

WWW_TRANSFORM='s,^home/username/www/connectfirst.com,www,'
DB_TRANSFORM='s,^home/username/backups,database,'

tar -cvf $BACKUP_DIR/$FILE --transform $WWW_TRANSFORM $WWW_DIR
mysqldump -u$DB_USER -p$DB_PASS $DB_NAME > $BACKUP_DIR/$DB_FILE
tar --append --file=$BACKUP_DIR/$FILE --transform $DB_TRANSFORM $BACKUP_DIR/$DB_FILE
rm $BACKUP_DIR/$DB_FILE
gzip -9 $BACKUP_DIR/$FILE

./copy.sh root redhat 192.168.122.51 $REMOTE_DIR $BACKUP_DIR/*
