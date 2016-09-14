"""
dploy script is an attempt at creating a clone of GNU stow that will work on
Windows as well as *nix
"""


import sys
assert sys.version_info >= (3, 3), "Requires Python 3.3 or Greater"
import dploy.main as main


def stow(sources, dest, is_silent=True, is_dry_run=False):
    """
    sub command stow
    """
    main.Stow(sources, dest, is_silent, is_dry_run)

def unstow(sources, dest, is_silent=True, is_dry_run=False):
    """
    sub command unstow
    """
    main.UnStow(sources, dest, is_silent, is_dry_run)


def link(source, dest, is_silent=True, is_dry_run=False):
    """
    sub command link
    """
    main.Link(source, dest, is_silent, is_dry_run)
