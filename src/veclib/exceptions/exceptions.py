class VectorError(Exception):
    """Ancestor of all the Vector based errors"""
    def __init__(self, *args: object, msg: str | None = "Invalid vector ops.") -> None:
        super().__init__(*args)

class DimensionError(VectorError):
    """Raised when there is an error associated with vector dimensions"""
    def __init__(self, *args: object, msg: str = "Invalid dimensions or dimensional arithmatic.") -> None:
        super().__init__(*args, msg)
