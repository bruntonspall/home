# github:.bash_profile
# -*- Mode: Bash; tab-width: 4; indent-tabs-mode: nil; -*-
#
#   Anything in this file gets applied only in "login" shells.

# No initialisation code lives in here, it is all stored in ~/etc/bash.
source ~/etc/bash/initialise

source_if_exists ~/etc/bash/login/*

# The next line updates PATH for the Google Cloud SDK.
source_if_exists /Users/michaelbruntonspall/Downloads/google-cloud-sdk/path.bash.inc

# The next line enables bash completion for gcloud.
source_if_exists /Users/michaelbruntonspall/Downloads/google-cloud-sdk/completion.bash.inc
