import pygame
from pygame.locals import *

class Text:
    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = 72
        self.fontcolor = Color('black')
        self.set_font()
        self.render()

    def set_font(self):
        """Set the Font object from name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        """Draw the text image to the screen."""
        App.screen.blit(self.img, self.rect)

class Button:
    def __init__(self, text, pos, size, callback):
        self.text = text
        self.pos = pos
        self.size = size
        self.callback = callback
        self.font = pygame.font.Font(None, 36)
        self.render()

    def render(self):
        """Render the button."""
        self.img = self.font.render(self.text, True, Color('white'))
        self.rect = pygame.Rect(self.pos, self.size)
        self.rect.topleft = self.pos

    def draw(self):
        """Draw the button to the screen."""
        pygame.draw.rect(App.screen, Color('blue'), self.rect)
        App.screen.blit(self.img, self.rect.topleft)

    def handle_event(self, event):
        """Handle button click event."""
        if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.callback()

```python
class Scene:
    def __init__(self, caption=''):
        self.caption = caption
        pygame.display.set_caption(self.caption)

class App:
    """Create a single-window app with multiple scenes."""

    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        flags = RESIZABLE
        App.screen = pygame.display.set_mode((640, 240), flags)
        App.t = Text('Pygame App', pos=(20, 20))
        App.b = Button('Click Me', pos=(20, 100), size=(200, 50), callback=self.on_button_click)

        App.running = True

    def on_button_click(self):
        print("Button clicked!")

    def run(self):
        """Run the main event loop."""
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False
                App.b.handle_event(event)

            App.screen.fill(Color('gray'))
            App.t.draw()
            App.b.draw()
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    App().run()