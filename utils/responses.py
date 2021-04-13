from enum import Enum
from discord_slash.context import SlashContext

class ResponseType(Enum):
    NONE        = None
    WARN        = ':warning:'
    ERR         = ':x:'
    FORB        = ':no_entry_sign:'
    
    SUCCESS     = ':white_check_mark:'
    INFO        = ':grey_exclamation:'

    def __str__(self):
        return self.value


class BotContext():
    def __init__(self, slash_context: SlashContext):
        self.sc = slash_context
        
        # A bit of a workaround to make the send method more accessable, not best way ik.
        # TODO: Find a better way to do this.
        self.send = slash_context.send

        self.author = slash_context.author
        self.bot  = slash_context.bot
        self.channel = slash_context.channel

    async def respond(self, response: str, type: ResponseType = ResponseType.NONE):
        if not type:
            await self.sc.send(response, hidden=True)
        else:
            conc_str = f'{type}  **|**  {response}'
            await self.sc.send(conc_str, hidden=True)