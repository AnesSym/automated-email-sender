#!/bin/bash

if [ ! -x "$(command -v ./run_streamlit_app.sh)" ]; then
    chmod +x run_streamlit_app.sh
    echo "Permissions set. Rerun this script."
    exit 1
fi

streamlit run streamlit_app.py
