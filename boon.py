#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: PtJung
@date: 2020-04-28 02:02:54
@version: 1.0
"""

import discord
import random
import traceback
from typing import NewType
from typing import Final
from typing import List
from typing import NoReturn

class HelperMethods(object):
    """ This static class offers miscellaneous methods for cleaner and easier interactions with the Boon class
    """

    def get_first_ping(text : str, FULL_PING_LENGTH = 22) -> str:
        """
        Returns the first single-target ping from a Discord message as text if possible, otherwise, an empty string is returned.

        ===== doctest =====
        >>> HelperMethods.get_first_ping("")
        ''
        >>> HelperMethods.get_first_ping("<@!1234567878><@>")
        ''
        >>> HelperMethods.get_first_ping("-==-21     =30811=512-=     2123jksifof  nkj4f3     ;3=-<@!123456789012345678")
        ''
        >>> HelperMethods.get_first_ping("<@<@!123456789012345678>")
        '<@!123456789012345678>'
        >>> HelperMethods.get_first_ping(";;  123 --# #<@!876543210987654321>??```<@!123456789012345678>   ```")
        '<@!876543210987654321>'
        >>> HelperMethods.get_first_ping("<@$123456789012345678><@!123456789012345678>")
        '<@!123456789012345678>'
        """
        index_init = text.find('<@!')
        index_finl = text.find('>', index_init + 1) + 1
        if (index_finl - index_init) == FULL_PING_LENGTH:
            return text[index_init:index_finl]
        return ""

    def run_file_token(directory : str, boon) -> NoReturn:
        """
        Runs the Boon instance with a token from the first line in a given directory.
        Throws FileNotFoundError if the given directory is not found.
        """
        with open(directory, 'r') as token_content:
            boon.run(token_content.readline())

    def get_file_strlist(directory : str) -> List[str]:
        """
        Extracts a list of strings from a given directory, with the list delimited by new-line, and returned.
        If the given directory is not found, a list of length 0 is returned.
        """
        try:
            with open(directory, 'r') as file_content:
                return file_content.read().split('\n')
        except FileNotFoundError as error:
            traceback.print_exc()
            return []



class Boon(discord.Client):
    """ This class functions asynchronously with the Discord client to deliver message interactions with user mentions

    ===== Attributes =====
    main_id: a string representation of the Boon instance's user ID
    """

    main_id: str = ""

    async def on_ready(self) -> NoReturn:
        """
        Boon: Initialize
        """

        self.main_id = str(self.user.id)
        print(f"START SUCCESS: {type(self).__name__}[name = \"{self.user.name}\"][id = \"{self.main_id}\"]")

    async def on_message(self, message) -> NoReturn:
        """
        Boon: Interacts with the newest Discord message
        """
        if (message.author.id == self.user.id) or (message.channel.id not in ALLOWED_CHANNELS):
            # Disable listening to Discord messages from itself, ensure the channel ID is allowed
            return

        # Retrieve newest message
        message_text = message.content
        first_ping_tag = HelperMethods.get_first_ping(message_text)

        # Interacts with the message
        if (MSG_PING_BOON not in [[], ['']]) and (self.main_id in first_ping_tag):
            # With a member pinging this Boon instance
            await message.channel.send(random.choice(MSG_PING_BOON))

        elif (MSG_PING_OTHER not in [[], ['']]) and first_ping_tag:
            # With a member pinging another member
            await message.channel.send(first_ping_tag + " " + random.choice(MSG_PING_OTHER))



if __name__ == "__main__":
    import doctest
    doctest.testmod()

    MSG_PING_BOON: Final[List[str]] = HelperMethods.get_file_strlist("mentions_boon.txt")
    MSG_PING_OTHER: Final[List[str]] = HelperMethods.get_file_strlist("mentions_other.txt")
    ALLOWED_CHANNELS: Final[List[str]] = list(map(int, HelperMethods.get_file_strlist("allowed_channels.txt")))

    try:
        HelperMethods.run_file_token('token.txt', Boon())
    except FileNotFoundError as error:
        traceback.print_exc()