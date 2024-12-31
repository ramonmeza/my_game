"""
My journey toward learning game development using Python. 
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

import pathlib

from typing import Dict
from xml.etree import ElementTree

import pygame


class AssetManager:
    """Manages assets such as texture and sounds."""

    textures: Dict[str, pygame.Surface]

    def __init__(self) -> None:
        self.textures = {}

    def load_spritesheet(self, path: str) -> None:
        """Load textures from an XML spritesheet.

        Follows Kenney's assets spritesheet format:

        ```xml
        <TextureAtlas imagePath="./relative/path/to/texture.png">
            <SubTexture name="textureID" x="0" y="0" width="100" height="200" />
            ...
        </TextureAtlas>
        ```

        Args:
            path (str): Path to the XML spritesheet.
        """
        xml = ElementTree.parse(path)
        root = xml.getroot()

        image_path = pathlib.Path(path).parent / root.attrib["imagePath"]
        atlas_surf = pygame.image.load(image_path)

        for child in root:
            name = child.attrib["name"]
            rect = pygame.Rect(
                int(child.attrib["x"]),
                int(child.attrib["y"]),
                int(child.attrib["width"]),
                int(child.attrib["height"]),
            )
            sprite_surf = atlas_surf.subsurface(rect)
            self.add_texture(name, sprite_surf)

    def add_texture(self, name: str, surface: pygame.Surface) -> None:
        """Add a texture to the AssetManager.

        Args:
            name (str): Name of the texture. Used to reference the texture.
            surface (pygame.Surface): Surface containing the texture.
        """
        self.textures[name] = surface

    def get_texture(self, name: str) -> pygame.Surface:
        """Get a loaded texture by name.

        Args:
            name (str): Name of the texture.

        Returns:
            pygame.Surface: The requested texture surface.
        """
        return self.textures[name]
