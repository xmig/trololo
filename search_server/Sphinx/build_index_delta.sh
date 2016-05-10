#!/usr/bin/env bash
source sphinx_config.sh

sudo $INDEXER --config $CONFIG delta
sudo $INDEXER --config $CONFIG delta_avl


