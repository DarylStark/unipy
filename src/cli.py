""" Module that contains the CLI scripts for the application """

from urllib import request
from unipy import Unipy
from argparse import ArgumentParser


def unipy_cli_main() -> None:
    """ Main function for the unipy_cli """

    # Create a argument parser
    arguments = ArgumentParser('Unipy CLI')

    # Create a object for subparser
    subs = arguments.add_subparsers(
        title='group',
        metavar='group',
        help='Command group',
        dest='group',
        required=True)

    # Add the subparser for authentication
    auth = subs.add_parser('auth', help='Authentication management').add_subparsers(
        title='command', metavar='command', help='Command', required=True)
    auth.add_parser('list', help='List all configured authentications')

    # Parse the arguments
    args = arguments.parse_args()

    print(args.command)


if __name__ == '__main__':
    # When ran as script, start the main function
    unipy_cli_main()
