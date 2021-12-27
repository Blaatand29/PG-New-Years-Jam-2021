__all__ = [
    "DIR",
    "ASSETS",
    "load_image",
    "scale_surf",
    "rotate_surf",
    "clip",
    "clamp",
    "text"
]

import pygame
import pathlib

DIR = pathlib.Path(__file__).parent.parent
ASSETS = DIR / "assets"


def load_image(name, scale: int = 1, alpha: bool = False):
    image = pygame.image.load(ASSETS / f"{name}.png")
    if scale != 1:
        image = scale_surf(image, scale)
    if alpha:
        return image.convert_alpha()
    return image.convert()


def scale_surf(surf: pygame.surface.Surface, scale):
    surf = pygame.transform.scale(surf, (int(surf.get_width() * scale), int(surf.get_height() * scale)))
    return surf


def rotate_surf(surf: pygame.surface.Surface, angle: int):
    surf = pygame.transform.rotate(surf, angle)
    return surf


def clip(surf: pygame.surface.Surface, pos, size):
    handle_surf = surf.copy()
    clip_rect = pygame.Rect(pos, size)
    handle_surf.set_clip(clip_rect)
    image = surf.subsurface(handle_surf.get_clip())
    return image.copy()


def clamp(value, mini, maxi):
    if value < mini:
        return mini
    elif maxi < value:
        return maxi
    else:
        return value


def text(msg):
    return pygame.font.SysFont('system', 50).render(msg, False, (255, 255, 255))
