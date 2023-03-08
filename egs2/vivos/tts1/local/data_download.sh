#!/usr/bin/env bash

# Copyright 2019 Tomoki Hayashi
#  Apache 2.0  (http://www.apache.org/licenses/LICENSE-2.0)

download_dir=$1

# check arguments
if [ $# != 1 ]; then
    echo "Usage: $0 <download_dir>"
    exit 1
fi

set -euo pipefail

cwd=$(pwd)
if [ ! -e "${download_dir}/vivos" ]; then
    mkdir -p "${download_dir}"
    cd "${download_dir}"
    gdown 1SBcglvbrPnuqtm9E2AmxhaTwr6ljEuFw
    unzip ./*.zip
    rm ./*.zip
    cd "${cwd}"
    echo "successfully prepared data."
else
    echo "already exists. skipped."
fi
