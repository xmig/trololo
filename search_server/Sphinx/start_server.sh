#!/usr/bin/env bash

source sphinx_config.sh

sudo $SEARCHD --config $CONFIG

echo Indexer using $CONFIG as a config
