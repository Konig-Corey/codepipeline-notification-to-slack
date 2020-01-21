#!/bin/bash
# bash script to test functionality of lambda locally
# python-lambda-local -f lambda_handler lambda_function.py event.json
python-lambda-local -f $1 $2 $3