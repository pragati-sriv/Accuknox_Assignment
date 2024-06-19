#!/bin/bash

SOURCE_DIR ="C:\Program Files\Notepad++"
DEST_DIR = "C:\Users\kashi\Downloads"
LOG_FILE ="C:\Windows\Logs\WindowsUpdate"

rsync -av --delete $SOURCE_DIR $DEST_DIR
if [ $? -eq 0 ]; then
  echo "$(date) - Backup successful" >> $LOG_FILE
else
  echo "$(date) - Backup failed" >> $LOG_FILE
fi