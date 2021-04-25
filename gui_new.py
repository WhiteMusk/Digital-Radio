import pygame,sys
import pygame_gui

pygame.init()
#music setting
pygame.mixer.init()
#pygame.time.delay(1000)#等待1秒讓mixer完成初始化

pygame.display.set_caption('Your Theme Name')
screen_width=1980
screen_height=1500
window_surface = pygame.display.set_mode([screen_width, screen_height])

background = pygame.Surface([screen_width, screen_height])
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager([screen_width, screen_height])

play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 225), (100, 50)), text='play', manager=manager)
slider_A = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(relative_rect=pygame.Rect((500, 325), (800, 50)),manager=manager,value_range=(0.0,1.0),start_value=0.0)
slider_B = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(relative_rect=pygame.Rect((500, 425), (800, 50)),manager=manager,value_range=(0.0,1.0),start_value=0.0)

#Option List
button1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 125), (100, 50)), text='Tape 1', manager=manager) 
button2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 225), (100, 50)), text='Tape 2', manager=manager)
button3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 325), (100, 50)), text='Tape 3', manager=manager) 
button4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 425), (100, 50)), text='Tape 4', manager=manager) 
button5 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 525), (100, 50)), text='Tape 5', manager=manager) 

music1 = pygame.mixer.Sound('Your Default Music file 1')
music2 = pygame.mixer.Sound('Your Default Music file 2')


clock = pygame.time.Clock()
is_running = True

while is_running:
    
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                #muisc opt
                if event.ui_element == button1:
                    music1 = pygame.mixer.Sound('tape 1_A')
                    music2 = pygame.mixer.Sound('tape 1_B')
                elif event.ui_element == button2:
                    music1 = pygame.mixer.Sound('tape 2_A')
                    music2 = pygame.mixer.Sound('tape 2_B')
                elif event.ui_element == button3:
                    music1 = pygame.mixer.Sound('tape 3_A')
                    music2 = pygame.mixer.Sound('tape 3_B')
                elif event.ui_element == button4:
                    music1 = pygame.mixer.Sound('tape 4_A')
                    music2 = pygame.mixer.Sound('tape 4_B')
                elif event.ui_element == button5:
                    music1 = pygame.mixer.Sound('tape 5_A')
                    music2 = pygame.mixer.Sound('tape 5_B')

                #play
                if event.ui_element == play_button:
                    pygame.mixer.Channel(0).play(music1)
                    pygame.mixer.Channel(1).play(music2)
                    music1.set_volume(slider_A.get_current_value())
                    music2.set_volume(slider_B.get_current_value())

            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                #volume
                if event.ui_element == slider_A or  event.ui_element == slider_B:                  
                    music1.set_volume(slider_A.get_current_value())
                    music2.set_volume(slider_B.get_current_value())

        manager.process_events(event)

    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    #window_surface.blit(plate,(0,0))
    pygame.display.update()
