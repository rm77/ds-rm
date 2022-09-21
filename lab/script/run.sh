#!/bin/bash
sudo chmod -R a+rwx /home/jovyan
JP="${JPORT:=8888}"
start-notebook.sh --NotebookApp.token='' --NotebookApp.password=''  --NotebookApp.ip='0.0.0.0' --NotebookApp.port=$JP --Notebook.autoreload=True --NotebookApp.notebook_dir=/home/jovyan/work --allow-root
