#!/bin/bash
scp "$1" root@192.168.0.25:/mnt/us/documents/
ssh root@192.168.0.25 "/mnt/us/usbnet/bin/hack-refresh"
