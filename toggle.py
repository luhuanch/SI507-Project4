import pygame
import view
import model

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (127, 127, 127)

pygame.init()

screen = pygame.display.set_mode((1200, 800))

pygame.display.set_caption("Election Data Viewer")
pygame.display.update()


ch_party = 'dem'
ch_raw = True
ch_sort_ascending = True


class Button:

    def __init__(self, text, rect):
        self.text = text
        self.rect = rect
        self.chosen = False

    def draw(self, surface):
        if self.chosen:
            button_col = RED
        else:
            button_col = GRAY
        pygame.draw.rect(surface, button_col, self.rect)

        font = pygame.font.Font(None, 36)
        label_view = font.render(self.text, False, BLACK)
        label_pos = label_view.get_rect()
        label_pos.centery = self.rect.centery
        label_pos.centerx = self.rect.centerx
        surface.blit(label_view, label_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            if x >= self.rect.x and x <= self.rect.x + self.rect.width and \
                y >= self.rect.y and y <= self.rect.y + self.rect.height:
                self.on_click(event)

    def on_click(self, event):
        data = model.get_data(ch_party, ch_raw, ch_sort_ascending)

        if ch_raw:
            max_v = 10000000
        else:
            max_v = 1.0

        global bc
        bc = view.BarChart(rect=pygame.Rect(0, 10, screen.get_rect().width*0.8, screen.get_rect().height), values=data, ticks=5,
        plot_area_width_ratio=0.6,
        plot_area_height_ratio=0.9,
        max_val=max_v)
        bc.draw(screen)


class PartyButton(Button):

    def __init__(self, text, rect, party='dem'):
        Button.__init__(self, text, rect)
        self.party = party

    def on_click(self, event):
        global ch_party
        ch_party = self.party
        Button.on_click(self, event)


class OrderButton(Button):

    def __init__(self, text, rect, sort_ascending=True):
        Button.__init__(self, text, rect)
        self.sort_ascending = sort_ascending

    def on_click(self, event):
        global ch_sort_ascending
        ch_sort_ascending = self.sort_ascending
        Button.on_click(self, event)


class TypeButton(Button):

    def __init__(self, text, rect, raw=True):
        Button.__init__(self, text, rect)
        self.raw = raw

    def on_click(self, event):
        global ch_raw
        ch_raw = self.raw
        Button.on_click(self, event)



# Initialize barchart and buttons
data_init = model.get_data()
bc = view.BarChart(rect=pygame.Rect(0, 10, screen.get_rect().width*0.8, screen.get_rect().height), values=data_init, ticks=5,
        plot_area_width_ratio=0.6,
        plot_area_height_ratio=0.9,
        max_val=10000000)

button1 = PartyButton("dem", pygame.Rect(screen.get_rect().width*0.8, screen.get_rect().height*0.1, 100, 50), 'dem')
button1.chosen = True
button2 = PartyButton("gop", pygame.Rect(screen.get_rect().width*0.8, screen.get_rect().height*0.1+50, 100, 50), 'gop')
button3 = OrderButton("up", pygame.Rect(screen.get_rect().width*0.8, screen.get_rect().height*0.3, 100, 50), True)
button3.chosen = True
button4 = OrderButton("down", pygame.Rect(screen.get_rect().width*0.8, screen.get_rect().height*0.3+50, 100, 50), False)
button5 = TypeButton("raw", pygame.Rect(screen.get_rect().width*0.8, screen.get_rect().height*0.5, 100, 50), True)
button5.chosen = True
button6 = TypeButton("%", pygame.Rect(screen.get_rect().width*0.8, screen.get_rect().height*0.5+50, 100, 50), False)

buttons = [button1, button2, button3, button4, button5, button6]



# display loop
done = False
while not done:
    screen.fill(view.BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        else:
            for button in buttons:
                button.handle_event(event)

    bc.draw(screen)

    if ch_party == 'dem':
        button1.chosen = True;
        button2.chosen = False;
    else:
        button1.chosen = False;
        button2.chosen = True;

    if ch_sort_ascending:
        button3.chosen = True;
        button4.chosen = False;
    else:
        button3.chosen = False;
        button4.chosen = True;

    if ch_raw:
        button5.chosen = True;
        button6.chosen = False;
    else:
        button5.chosen = False;
        button6.chosen = True;


    for button in buttons:
        button.draw(screen)
    pygame.display.update()

