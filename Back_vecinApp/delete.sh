#!/bin/bash

find ./*/migrations/ -name "[0-9]*" -type f -delete
find . -name "*.pyc" -delete