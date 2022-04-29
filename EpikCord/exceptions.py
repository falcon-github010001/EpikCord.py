class InvalidApplicationCommandType(Exception):
    ...

class InvalidApplicationCommandOptionType(Exception):
    ...

class InvalidOption(Exception):
    ...

class InvalidStatus(Exception):
    ...

class ClosedWebSocketConnection(Exception):
    ...

class MissingClientSetting(Exception):
    ...

class MissingCustomId(Exception):
    ...



class DiscordAPIError(Exception):
    ...


class InvalidData(Exception):
    ...


class InvalidIntents(Exception):
    ...


class ShardingRequired(Exception):
    ...


class InvalidToken(Exception):
    ...


class UnhandledException(Exception):
    ...


class DisallowedIntents(Exception):
    ...


class BadRequest400(Exception):
    ...


class Unauthorized401(Exception):
    ...


class Forbidden403(Exception):
    ...


class NotFound404(Exception):
    ...


class MethodNotAllowed405(Exception):
    ...


class Ratelimited429(Exception):
    ...


class GateawayUnavailable502(Exception):
    ...


class InternalServerError5xx(Exception):
    ...


class TooManyComponents(Exception):
    ...


class InvalidComponentStyle(Exception):
    ...


class CustomIdIsTooBig(Exception):
    ...


class InvalidArgumentType(Exception):
    ...


class TooManySelectMenuOptions(Exception):
    ...


class LabelIsTooBig(Exception):
    ...


class ThreadArchived(Exception):
    ...