import pendulum


def get_current_time(tz_name: str) -> dict:
    """
    Returns the current time information for the given timezone.
    """
    now = pendulum.now(tz=tz_name)
    return {
        "iso_8601": now.to_iso8601_string(),
        "dst": now.is_dst()
    }