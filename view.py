import pygame
import model
import view

BLACK = (0, 0, 0)
WHITE = (255,255,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Bar:
	def __init__(self,color,length,height,padding=0.1):
		self.length = length
		self.color = color
		self.height = height
		self.padding = padding

	def draw(self,surface,x,y):
		padding_height = self.height * self.padding
		adjusted_height = self.height - 2 * padding_height
		pygame.draw.rect(surface, self.color,[x,y+padding_height,self.length,adjusted_height])
# a class to display a horizontal bar chart in pygame
class BarChart:

	# rect: a pygame.rect encoding size and position
	def __init__(self, rect=pygame.Rect(0,0,600,400), values=[], ticks=10,
		plot_area_width_ratio=0.8, plot_area_height_ratio=0.8, bar_color=GREEN,
		max_val=0):
		self.rect = rect
		self.values = values
		self.ticks = ticks
		self.plot_area_width_ratio = plot_area_width_ratio
		self.plot_area_height_ratio = plot_area_height_ratio
		self.max_val = max_val
		self.bar_color = bar_color

		self.label_area_width_ratio = 0.2
		self.scale_area_height_ratio = 0.2

		self.scale_area = pygame.Rect(
            rect.x + rect.width * self.label_area_width_ratio,
            rect.y + rect.height * self.plot_area_height_ratio,
            rect.width * self.plot_area_width_ratio,
            rect.height * self.scale_area_height_ratio
        )

		self.label_area = pygame.Rect(
			rect.x,
            rect.y,
            rect.width * self.label_area_width_ratio,
            rect.height * self.plot_area_height_ratio
        )

		self.plot_area = pygame.Rect(
            rect.x + self.label_area.width,
            rect.y,
            rect.width * self.plot_area_width_ratio,
            rect.height * self.plot_area_height_ratio
        )

		self.set_values(values)

	def set_values(self, values):
		self.values = values

        # figure out max value
		max_val = self.max_val
		for v in values:
			if v[1] > max_val:
				max_val = v[1]
		self.max_val = max_val

	def get_bar_height(self):
		return self.plot_area.height / len(self.values)

	def draw_labels(self, surface):
		bar_num = 0
		for v in self.values:
			label_text = v[0]

			font = pygame.font.Font(None, 25)
			label_view = font.render(label_text, False, WHITE)
			label_pos = label_view.get_rect()
			label_pos.centery = self.rect.y + self.get_bar_height() * bar_num + self.get_bar_height() / 2
			label_pos.x = self.rect.x + 20
			surface.blit(label_view, label_pos)
			bar_num += 1

	def draw_scale(self, surface):
		scale_label_spacing = self.scale_area.width / (self.ticks - 1)
		interval = self.max_val/(self.ticks - 1)

		for i in range(self.ticks):
			font = pygame.font.Font(None, 25)
			if interval > 1:
				scale_label_view = font.render(str(int(i * interval)), False, WHITE)
			else:
				scale_label_view = font.render(str(float(i * interval)), False, WHITE)
			scale_label_pos = scale_label_view.get_rect()
			scale_label_pos.y = self.scale_area.y + 10
			scale_label_pos.x = self.scale_area.x + i * int(scale_label_spacing)
			surface.blit(scale_label_view, scale_label_pos)

	def draw_bars(self, surface):
		bar_num = 0
		for v in self.values:
			bar_length = self.plot_area.width * v[1] / self.max_val
			b = Bar(self.bar_color,
					bar_length,
					self.plot_area.height / len(self.values))
			y_pos = self.plot_area.y + bar_num * b.height
			bar_num += 1
			b.draw(surface, self.plot_area.x, y_pos)

	def draw(self, surface):
		self.draw_bars(surface)
		self.draw_labels(surface)
		self.draw_scale(surface)

# SELF-TESTING MAIN
if __name__ == "__main__":

	pygame.init()

	screen = pygame.display.set_mode((1000,700))

	pygame.display.set_caption("Bar Chart Test")
	pygame.display.update()

	data =	[
	 		("apples", 6),
	 		("bananas", 7),
 			("grapes", 4),
  			("pineapple", 1),
  			("cherries", 15)
        	]

	# display using default values
	bc = BarChart(values=data)

	data2 = [
			('Jenny', 80),
			('Stanley', 90),
			('Timothy', 92)
			]

	# override all of the defaults
	bc2 = BarChart(
		rect=pygame.Rect(0,400,800,150),
		values=data2,
		ticks=5,
		plot_area_width_ratio=0.85,
		plot_area_height_ratio=0.9,
		bar_color=RED,
		max_val=100
		)

	# display loop
	done = False
	while not done:
		screen.fill(BLACK)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		bc.draw(screen)
		bc2.draw(screen)
		pygame.display.update()
# class Button:
#
#     def __init__(self, text, rect):
#         self.text = text
#         self.rect = rect
#         self.chosen = False
#
#     def draw(self, surface):
#         if self.chosen:
#             button_col = RED
#         else:
#             button_col = GRAY
#         pygame.draw.rect(surface, button_col, self.rect)
#
#         font = pygame.font.Font(None, 36)
#         label_view = font.render(self.text, False, BLACK)
#         label_pos = label_view.get_rect()
#         label_pos.centery = self.rect.centery
#         label_pos.centerx = self.rect.centerx
#         surface.blit(label_view, label_pos)
#
#     def handle_event(self, event):
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             (x, y) = pygame.mouse.get_pos()
#             if x >= self.rect.x and x <= self.rect.x + self.rect.width and \
#                 y >= self.rect.y and y <= self.rect.y + self.rect.height:
#                 self.on_click(event)
#
#     def on_click(self, event):
#         data = model.get_data(ch_party, ch_raw, ch_sort_ascending)
#
#         if ch_raw:
#             max_v = 10000000
#         else:
#             max_v = 1.0
#
#         global bc
#         bc = view.BarChart(rect=pygame.Rect(0, 10, screen.get_rect().width*0.8, screen.get_rect().height), values=data, ticks=5,
#         plot_area_width_ratio=0.6,
#         plot_area_height_ratio=0.9,
#         max_val=max_v)
#         bc.draw(screen)
#
#
# class PartyButton(Button):
#
#     def __init__(self, text, rect, party='dem'):
#         Button.__init__(self, text, rect)
#         self.party = party
#
#     def on_click(self, event):
#         global ch_party
#         ch_party = self.party
#         Button.on_click(self, event)
#
#
# class OrderButton(Button):
#
#     def __init__(self, text, rect, sort_ascending=True):
#         Button.__init__(self, text, rect)
#         self.sort_ascending = sort_ascending
#
#     def on_click(self, event):
#         global ch_sort_ascending
#         ch_sort_ascending = self.sort_ascending
#         Button.on_click(self, event)
#
#
# class TypeButton(Button):
#
#     def __init__(self, text, rect, raw=True):
#         Button.__init__(self, text, rect)
#         self.raw = raw
#
#     def on_click(self, event):
#         global ch_raw
#         ch_raw = self.raw
#         Button.on_click(self, event)
#
#
#
# # Initialize barchart and buttons
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GRAY = (127, 127, 127)
#
# pygame.init()
#
# screen = pygame.display.set_mode((1200, 800))
#
# pygame.display.set_caption("Election Data Viewer")
# pygame.display.update()
#
#
# ch_party = 'dem'
# ch_raw = True
# ch_sort_ascending = True
# data_init = model.get_data()
# bc = view.BarChart(rect=pygame.Rect(0, 10, screen.get_rect().width*0.8, screen.get_rect().height), values=data_init, ticks=5,
#         plot_area_width_ratio=0.6,
#         plot_area_height_ratio=0.9,
#         max_val=10000000)
#
# button1 = PartyButton("dem", pygame.Rect(screen.get_rect().width*0.8, screen.get_rect().height*0.1, 100, 50), 'dem')
# button1.chosen = True
# button2 = PartyButton("gop", pygame.Rect(screen.get_rect().width*0.8, screen.get_rect().height*0.1+50, 100, 50), 'gop')
# button3 = OrderButton("up", pygame.Rect(screen.get_rect().width*0.8, screen.get_rect().height*0.3, 100, 50), True)
# button3.chosen = True
# button4 = OrderButton("down", pygame.Rect(screen.get_rect().width*0.8, screen.get_rect().height*0.3+50, 100, 50), False)
# button5 = TypeButton("raw", pygame.Rect(screen.get_rect().width*0.8, screen.get_rect().height*0.5, 100, 50), True)
# button5.chosen = True
# button6 = TypeButton("%", pygame.Rect(screen.get_rect().width*0.8, screen.get_rect().height*0.5+50, 100, 50), False)
#
# buttons = [button1, button2, button3, button4, button5, button6]
#
#
#
# # display loop
# done = False
# while not done:
#     screen.fill(view.BLACK)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#         else:
#             for button in buttons:
#                 button.handle_event(event)
#
#     bc.draw(screen)
#
#     if ch_party == 'dem':
#         button1.chosen = True;
#         button2.chosen = False;
#     else:
#         button1.chosen = False;
#         button2.chosen = True;
#
#     if ch_sort_ascending:
#         button3.chosen = True;
#         button4.chosen = False;
#     else:
#         button3.chosen = False;
#         button4.chosen = True;
#
#     if ch_raw:
#         button5.chosen = True;
#         button6.chosen = False;
#     else:
#         button5.chosen = False;
#         button6.chosen = True;
#
#
#     for button in buttons:
#         button.draw(screen)
#     pygame.display.update()
