#!/usr/bin/env python
#
# Very stripped-down, simplified, feature-less version of gcontacts.py
# by Jim Karsten.
#
# $ GMAIL_USER='x@gmail.com' GMAIL_PASS='x' ./gmail2mutt.py > aliases
#
###

__author__  = "Patrick Brisbin <pbrisbin@gmail.com>"
__version__ = "0.1"

import os
import re
import sys

import netrc
import gdata.contacts
import gdata.contacts.service

CONTACTS_MACRO = 'contacts_account'

def get_email_address():
     """ Get the google email address associated with Google contacts.
     Args:
         None
     Returns:
         email address: myusername@gmail.com
     """
     try:
         net_rc = netrc.netrc()
     except IOError as err:
         LOG.debug('Unable to read $HOME/.netrc file. {reason}'.format(
                     reason=str(err)))
         net_rc = None
     if net_rc:
         try:
             return net_rc.macros[CONTACTS_MACRO][0].strip()
         except KeyError as err:
             msg = ' '.join([
                 'Unable to get contacts account from $HOME/.netrc file.',
                 'A macdefs "{macro}" is not defined.'.format(
                     macro=CONTACTS_MACRO),
                 ])
             LOG.debug(msg)

     # If we are in interactive mode, prompt for password
     psi = os.environ.get('PS1', None)
     if not psi:
         return None
     return raw_input('Email account: ')

def get_password(email_address):
    """ Get google email account password.
    Args:
        email_address: myusername@gmail.com
    Returns:
        password (string)
    Notes:
        If a password is not accessible, the user is prompted for one.
    """
    try:
        net_rc = netrc.netrc()
    except IOError as err:
        LOG.debug('Unable to read $HOME/.netrc file. {reason}'.format(
                    reason=str(err)))
    if net_rc:
        for host in net_rc.hosts.keys():
            if net_rc.authenticators(host)[0] == email_address:
                return net_rc.authenticators(host)[2]

    # If we are in interactive mode, prompt for password
    psi = os.environ.get('PS1', None)
    if not psi:
        return None
    return getpass.getpass()

if __name__ == '__main__':
    client = gdata.contacts.service.ContactsService()

    try:
        client.email    = get_email_address()
        client.password = get_password(client.email)
    except:
        sys.stderr.write("GMAIL_USER or GMAIL_PASS unset\n")
        exit(1)

    client.ProgrammaticLogin()
    filter = None

    if len(sys.argv) > 1:
      filter = sys.argv[1].lower().strip()

    query = gdata.contacts.service.ContactsQuery()
    query.max_results = 9999

    for entry in client.GetContactsFeed(query.ToUri()).entry:
        name = entry.title.text or None

        if name and entry.email:
          if not filter or filter in name.lower() or filter in entry.email[0].address:
            print "{email}\t{name}".format(
                    name  = name,
                    email = entry.email[0].address
                    )
