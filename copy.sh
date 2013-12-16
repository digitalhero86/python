#!/usr/bin/expect
set timeout 99999
set username [lindex $argv 0]
set password [lindex $argv 1]
set hostname [lindex $argv 2]
set dir [lindex $argv 3]
set file [lindex $argv 4]

send_user "\n#########################\n# $hostname\n#########################\n
"
spawn scp $file $username@$hostname:$dir

expect {
  timeout { send_user "\nFailed to get password prompt\n"; exit 1 }
  eof { send_user "\nSSH failure for $hostname\n"; exit 1 }
  "*assword"
}

send "$password\r"

expect {
  timeout { send_user "\nLogin failed. Password incorrect.\n"; exit 1}
  "*\# "
}

