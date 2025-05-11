import pygame

class PygameInterface:
    def __init__(self):
        pygame.init()
        self.screen = None
        self.clock = None

    def open_window(self, resolution):
        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Keräilypeli")

    def draw_inventory(self, inventory_content):
        button_height = 30
        button_width = 200
        inventory_index = 0
        pygame.display.get_window_size()
        for i in range(10):
            button_coordinate = (0, inventory_index*1+inventory_index*button_height)
            pygame.draw.rect(self.screen, "white", pygame.Rect(button_coordinate, (button_width, button_height)))
            inventory_index += 1
        pygame.display.flip()
        self.clock.tick(60)

    def _create_button(self, location, size, text, action):

