#!/bin/bash
# This script goes to youtube and plays a video using youtube-dl and mplayer without saving an intermediate file
# or needing to download the entire file first.
# Argument 1 - The video id. (ie: youtube.com/watch?v=<param>)

if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters"
    exit
fi

# Setup venv command if required to access youtube-dl. (May differ based on deployment target.)

MYCROFT_CONF=/etc/mycroft/mycroft.conf
VENV_CMD=
if [[ -f "$MYCROFT_CONF" ]] && grep -q '"platform":.*"mycroft_mark_1"' $MYCROFT_CONF; then
    VENV_CMD=". /opt/venvs/mycroft-core/bin/activate;"
fi

# Execute the script. TBD: make more parameters adjustable.
exec /bin/bash -c "$VENV_CMD exec python3 -m youtube_dl -o - "https://www.youtube.com/watch?v=$1" --quiet -f 'bestaudio[ext=m4a]' | mplayer - -vo xy -volume 20 -really-quiet > /dev/null 2>&1"
