from discord.ext.commands import CommandError


class PrefixTooLong(CommandError):
    pass


class PrefixNotFound(CommandError):
    pass


class PrefixDeletionError(CommandError):
    pass


class PrefixAlreadyExists(CommandError):
    pass
