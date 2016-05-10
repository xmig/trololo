#!/usr/bin/env bash
source sphinx_config.sh

#sudo $INDEXER --config $CONFIG --ALL

sudo $INDEXER --config $CONFIG property
sudo $INDEXER --config $CONFIG availability


