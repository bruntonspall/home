#!/bin/bash
# Setup to automatically extract the latest undermine journal data
file=/tmp/TheUndermineJournal.zip

if [[ ! -f $file || $(stat -f %c $file) -le $(( `date +%s` - 7200 )) ]]; then 
curl "https://theunderminejournal.com/TheUndermineJournal.zip?key=okqzVApi4bAbzNW8ndiy6oj1Uv5sZTpE&realms=EUH-Stormrage" -o$file
unzip -o $file -d /Volumes/icklecat/World\ of\ Warcraft/Interface/Addons/
fi

cd /Volumes/icklecat/World\ of\ Warcraft/Interface/Addons/ElvUI.git
git checkout -- .
git pull

/Volumes/icklecat/World\ of\ Warcraft/World\ of\ Warcraft-64.app/Contents/MacOS/World\ of\ Warcraft-64
