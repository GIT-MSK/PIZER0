#!/bin/bash

function write_report {
    echo -ne $1 > /dev/hidg0
}

# H (press shift and H)
write_report "\x08\0\0\0\0\0\0\0"

write_report "\0\0\0\0\0\0\0\0"
