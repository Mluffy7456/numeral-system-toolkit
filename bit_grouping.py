from rich.prompt import Prompt
from rich_utils import console, title, error
from language import t
from converter import to_decimal
from validator import validate_base, validate_number_for_base
from representations import group_bits

def bit_grouping_menu():
    title(t("bitgroup.title"))
    try:
        number = Prompt.ask(t("bitgroup.number")).strip().upper()
        base = int(Prompt.ask(t("bitgroup.base")))
        group = int(Prompt.ask(t("bitgroup.size")))
        validate_base(base)
        validate_number_for_base(number, base)
        if group <= 0 or group > 64:
            raise ValueError(t("error.invalid_group"))
        value = to_decimal(number, base)
        if value < 0:
            raise ValueError(t("error.negative_not_supported"))
        bits = format(value, "b")
        console.print(f"[bold cyan]{t('bitgroup.binary')}[/]: {group_bits(bits, group)}")
    except ValueError as e:
        error(str(e))
