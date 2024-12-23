"""
The classic card game Blackjack, implemented in Python. 
Copyright (C) 2024  Ramon Meza

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import logging


class ApplicationError(Exception):
    """
    Exception thrown by application containing error message and error code.
    """

    _error_code: int

    def __init__(self, msg: str, error_code: int) -> None:
        logging.error("%s (code: %i)", msg, error_code)
        self._error_code = error_code

    @property
    def error_code(self) -> int:
        """Error code related to this ApplicationError instance.

        Returns:
            int: Error code.
        """
        return self._error_code
