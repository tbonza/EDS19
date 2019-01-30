""" Parses and implements playbook commands. Similar to Ansible

References:
  https://docs.ansible.com/
"""
from yaml import load, Loader

def parse_playbook(filepath: str):
    """ Parse Okra Playbook in YAML format. """
    with open(filepath, "r") as infile:
        data = load(infile, Loader=Loader)
    return data
