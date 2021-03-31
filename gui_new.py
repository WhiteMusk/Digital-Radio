import pygame,sys
import pygame_gui

pygame.init()
#music setting
pygame.mixer.init()
#pygame.time.delay(1000) #wait for 1 sec. so that the initialization can be done.

pygame.display.set_caption('Your Digital Raio') #users may rename the GUI caption by themselves.
screen_width=1980
screen_height=1500
window_surface = pygame.display.set_mode([screen_width, screen_height])

background = pygame.Surface([screen_width, screen_height])
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager([screen_width, screen_height])

play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 375), (500, 250)), text='play', manager=manager)
slider_A = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(relative_rect=pygame.Rect((900, 425), (800, 50)),manager=manager,value_range=(0.0,1.0),start_value=0.0)
slider_B = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(relative_rect=pygame.Rect((900, 500), (800, 50)),manager=manager,value_range=(0.0,1.0),start_value=0.0)

#Option List: used if there are more than one sets of soundtracks
button1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 125), (100, 50)), text='Tape 1', manager=manager) #soundtrack set 1
button2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 225), (100, 50)), text='Tape 2', manager=manager) #soundtrack set 2
button3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 325), (100, 50)), text='Tape 3', manager=manager) #soundtrack set 3
button4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 425), (100, 50)), text='Tape 4', manager=manager) #soundtrack set 4
button5 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 525), (100, 50)), text='Tape 5', manager=manager) #soundtrack set 5

#default music: you may fill in your first set of soundtracks
#the format should be .wav files.
music1 = pygame.mixer.Sound('soundtrackFileName')
music2 = pygame.mixer.Sound('soundtrackFileName')


clock = pygame.time.Clock()
is_running = True

while is_running:
    
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                #muisc opt: file names are just for your reference. You may adapt them into the ones you're using.
                if event.ui_element == button1:
                    music1 = pygame.mixer.Sound('campusA.wav')
                    music2 = pygame.mixer.Sound('campusB.wav')
                elif event.ui_element == button2:
                    music1 = pygame.mixer.Sound('dateA.wav')
                    music2 = pygame.mixer.Sound('dateB.wav')
                elif event.ui_element == button3:
                    music1 = pygame.mixer.Sound('officeA.wav')
                    music2 = pygame.mixer.Sound('officeB.wav')
                elif event.ui_element == button4:
                    music1 = pygame.mixer.Sound('eleA.wav')
                    music2 = pygame.mixer.Sound('eleB.wav')
                elif event.ui_element == button5:
                    music1 = pygame.mixer.Sound('tunnelA.wav')
                    music2 = pygame.mixer.Sound('tunnelB.wav')

                #play
                if event.ui_element == play_button:
                    pygame.mixer.Channel(0).play(music1)
                    pygame.mixer.Channel(1).play(music2)
                    music1.set_volume(slider_A.get_current_value())
                    music2.set_volume(slider_B.get_current_value())

            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                #volume: the slide bar for adapting the volumes of the soundtracks separately.
                if event.ui_element == slider_A or  event.ui_element == slider_B:                  
                    music1.set_volume(slider_A.get_current_value())
                    music2.set_volume(slider_B.get_current_value())

        manager.process_events(event)

    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    #window_surface.blit(plate,(0,0))
    pygame.display.update()
