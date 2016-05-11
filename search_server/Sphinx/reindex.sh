#!/usr/bin/env bash

source sphinx_config.sh
where=ALL

#sudo $SEARCHD --config $CONFIG --stop
#wait
sudo $INDEXER --config $CONFIG --$where --rotate
#wait
#sudo $SEARCHD --config $CONFIG --rotate

