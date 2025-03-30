import pygame as pg

def main():
    pg.init()
    
    pytorch_logo = pg.image.load("pytorch_logo.png")
    python_logo = pg.image.load("python_logo.png")
    deep_learning = pg.image.load("deep_learning.png")
    
    img_width, img_height = pytorch_logo.get_size()
    spacing = 20
    font_size = 40

    width = 800
    height = 800

    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("Image Equation Display")
    
    font = pg.font.Font(None, font_size)
    plus_text = font.render("+", True, (255, 255, 255))
    equals_text = font.render("=", True, (255, 255, 255))
    
    running = True
    while running:
        screen.fill((0, 0, 0))
    
        x1 = spacing
        x_plus = x1 + img_width + spacing
        x2 = x_plus + plus_text.get_width() + spacing
        x_equals = x2 + img_width + spacing
        x3 = x_equals + equals_text.get_width() + spacing
        y = (height - img_height) // 2
        y_text = (height - font_size) // 2
        
        screen.blit(pytorch_logo, (x1, y))
        screen.blit(plus_text, (x_plus, y_text))
        screen.blit(python_logo, (x2, y))
        screen.blit(equals_text, (x_equals, y_text))
        screen.blit(deep_learning, (x3, y))
        
        pg.display.flip()
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
    
    pg.quit()

if __name__ == "__main__":
    main()
