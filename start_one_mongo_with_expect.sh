#!/usr/bin/expect
set CONF_DIR [lindex $argv 0]
spawn sudo mongod -f $CONF_DIR
expect "*alley*"
send "a\r"
# expect "*#*"
# send "mongod -f "$CONF_DIR
expect eof