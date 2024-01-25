#!/bin/bash

# server IPs & username
server1="54.175.44.151"
server2="54.90.16.62"
load_balancer="35.153.193.194"
username="ubuntu"

# prompt to select server to use
echo "select server to login:"
echo "-----------------------"
echo "1. Server 1 -> {$server1}"
echo "2. Server 2 -> {$server2}"
echo "3. Load Balancer -> {$load_balancer}"
echo

read -p "Enter choice (1/2/3): " choice
echo

case $choice in
	1)
		echo "connecting to web-01 ($server1)"
		;;
	2)
		echo "connecting to web-02 ($server2)"
		;;
	3)
		echo "connecting to Load Balancer ($load_balancer)"
		;;
	*)
		echo "invalid option"
		exit 1
		;;
esac
echo

# login based on selected choice
case $choice in
	1)
		ssh "$username@$server1"
		;;
	2)
		ssh "$username@$server2"
		;;
	3)
		ssh "$username@$load_balancer"
		;;
esac
