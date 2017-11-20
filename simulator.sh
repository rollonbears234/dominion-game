#!/bin/sh
for i in `seq 1 1000`;
        do
                python play.py < commands.in
        done
