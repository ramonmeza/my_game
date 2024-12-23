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

import datetime
import logging
import os
import sys

from .game import Blackjack


def main() -> int:
    """Entry point to application.

    Returns:
        int: Exit code.
    """
    try:
        # entry-point for application
        Blackjack.init()
        Blackjack.run()

    except KeyboardInterrupt:
        logging.info("User request to shut down application received")

    except Exception as e:      # pylint: disable=broad-exception-caught
        logging.error(str(e))
        return -1

    finally:
        Blackjack.shutdown()

    return 0


if __name__ == "__main__":
    # setup logging
    if not os.path.exists("logs"):
        os.mkdir("logs")
    log_path: str = datetime.datetime.now().strftime('logs/blackjackpy_%Y-%m-%d_%H-%M-%S.log')
    logging.basicConfig(filename=log_path, level=logging.DEBUG)

    # run main
    sys.exit(main())
