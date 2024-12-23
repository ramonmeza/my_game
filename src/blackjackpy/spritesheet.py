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

import collections
import logging
import os

from xml.etree import ElementTree
from xml.etree.ElementTree import Element

import pygame


SpriteInfo = collections.namedtuple("SpriteInfo", ["x", "y", "width", "height"])


class Spritesheet:
    """Provides access to Surface objects loaded from an XML spritesheet.
    """

    sheet: pygame.Surface
    sprites_info: dict[str, dict[str, int]]

    def __init__(self, xml_path: str) -> None:
        logging.info("Loading spritesheet XML (%s)", xml_path)
        data: ElementTree = ElementTree.parse(xml_path)
        atlas: Element = data.getroot()

        # validate root
        if atlas.tag != "TextureAtlas":
            logging.error("Spritesheet XML parsing error: Root element must be "
                          "TextureAtlas. (xml_path: %s)", xml_path)
            raise RuntimeError("Spritesheet XML parsing error")

        if "imagePath" not in atlas.attrib.keys():
            logging.error("imagePath attribute required on TextureAtlas for "
                          "spritesheet XML (xml_path: %s)", xml_path)
            raise RuntimeError("Spritesheet XML parsing error")

        # load image
        rel_dir, _ = os.path.split(xml_path)
        image_path: str = f"{rel_dir}/{atlas.attrib['imagePath']}"
        self.sheet = pygame.image.load(image_path)

        self.sprites_info = {}
        for child in atlas:
            # validate
            if child.tag != "SubTexture":
                logging.warning("Unsupported tag (%s) found in spritesheet XML "
                                "(xml_path: %s)", child.tag, xml_path)
                continue

            if (
                    "name" not in child.attrib and
                    "x" not in child.attrib and
                    "y" not in child.attrib and
                    "width" not in child.attrib and
                    "height" not in child.attrib
                ):
                logging.warning("Required attributes within SubTexture not "
                                "found in spritesheet XML (xml_path: %s)", xml_path)
                continue

            # get data
            name: str = str(child.attrib["name"])
            x: int = int(child.attrib["x"])
            y: int = int(child.attrib["y"])
            width: int = int(child.attrib["width"])
            height: int = int(child.attrib["height"])

            self.sprites_info[name] = SpriteInfo(x, y, width, height)

    def get(self, name: str) -> pygame.Surface:
        """Get a specific sprite.

        Args:
            name (str): Name of the sprite to get.

        Returns:
            pygame.Surface: The Surface sprite.
        """
        if name not in self.sprites_info:
            logging.error("Sprite error: Failed to receive sprite by name (%s)",
                          name)
            raise RuntimeError("Sprite error: Failed to receive sprite by name ",
                               name)

        info: SpriteInfo = self.sprites_info[name]

        return self.sheet.subsurface(
            (info.x, info.y),
            (info.width, info.height)
        )
