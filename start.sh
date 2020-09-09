#!/bin/bash
/home/tb/.local/bin/gunicorn -w 1 -b 127.0.0.1:5050 app:app
