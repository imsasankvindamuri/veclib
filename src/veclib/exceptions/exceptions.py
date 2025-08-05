"""
    veclib: the `pathlib` for vector arithmatic
    Copyright (C) 2025 imsasankvindamuri; contact me on GitHub at `https://github.com/imsasankvindamuri`

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
    USA
"""
class VectorError(Exception):
    """Ancestor of all the Vector based errors"""
    def __init__(self, *args: object, msg: str | None = "Invalid vector ops.") -> None:
        super().__init__(*args)

class DimensionError(VectorError):
    """Raised when there is an error associated with vector dimensions"""
    def __init__(self, *args: object, msg: str = "Invalid dimensions or dimensional arithmatic.") -> None:
        super().__init__(*args, msg)
