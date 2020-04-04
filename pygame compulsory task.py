# GAME IS AS FOLLOWS:
# PLAYER (YELLOW), MUST RUN AWAY FROM 3 ENEMIES
# WHEN ONE OF THE ENEMIES COMES IN CONTACT WITH PLAYER AND GAME IS OVER
# TO WIN, CHARACTER MUST EAT THE FRUIT AND GAME IS OVER

import pygame             # Runs program using Pygame
import random             # Allows you to use a function that generates random numbers

pygame.init()             # Initials pygame

screen_width = 1300       # Width of window where game progression will be displayed
screen_height = 610       # Height of window where game progression is to be displayed

screen = pygame.display.set_mode((screen_width, screen_height)) #Setting display screen

# Loading Character Images
player = pygame.image.load("player.jpg") 
enemy1 = pygame.image.load("monster.jpg") 
enemy2 = pygame.image.load("enemy4.jpg")  
enemy3 = pygame.image.load("enemy3.jpg")
prize = pygame.image.load("prize.jpg")

# Initial state of Control Keys to be used in the game
keyDown = False
keyRight = False
keyLeft = False
keyUp = False

# Obtaining height and width of every character
# PLAYER CHARACTER
player_height = player.get_height()
player_width = player.get_width()

# ENEMY1 CHARACTER
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()

# ENEMY2 CHARACTER
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

# ENEMY3 CHARACTER
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

# PRIZE CHARACTER
prize_height = prize.get_height()
prize_width = prize.get_width()


# Gives initial X and Y position for each character respectively

playerXposition = 300                                                  # PLAYER CHARACETR
playerYposition = 300

enemy1Xposition = 0 - enemy1_width                                     # ENEMY1
enemy1Yposition = random.randint(0, (screen_height-enemy1_height))

enemy2Xposition = random.randint(0, (screen_width- enemy2_width))      # ENEMY2
enemy2Yposition = 0 -screen_height

enemy3Xposition = screen_width                                         # ENEMY3
enemy3Yposition = random.randint(0, (screen_height- enemy1_height))

prizeYposition = random.randint(0, (screen_height-prize_height))       # ENEMY4
prizeXposition = screen_width

run = True

while   run:                                                      # Loop will repeat till run is False
        screen.fill(0)                                            # This section clears the screen

        # In the following sub-section Characters are drawn on specified positions
        screen.blit(player, (playerXposition, playerYposition))   
        screen.blit(enemy1, (enemy1Xposition, enemy1Yposition))
        screen.blit(enemy2, (enemy2Xposition, enemy2Yposition))
        screen.blit(enemy3, (enemy3Xposition, enemy3Yposition))
        screen.blit(prize, (prizeXposition, prizeYposition))

        # Screen update
        pygame.display.flip()


        for event in pygame.event.get():
            # Checks if user quits game, if so Game is ended
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN:         # Checks if key is pressed down

                # If pressed key is the Up key, keyUp changes from False to True
                if event.key == pygame.K_UP:         
                    keyUp = True

                # If pressed key is the Down key, keyDown changes from False to True   
                if event.key == pygame.K_DOWN:
                    keyDown = True
                # If pressed key is the Right key, keyRight changes from False to True    
                if event.key == pygame.K_RIGHT:
                    keyRight = True
                # If pressed key is the Left key, keyLeft changes from False to True    
                if event.key == pygame.K_LEFT:
                    keyLeft = True

            if event.type == pygame.KEYUP:            # Checks if key is released

                # If released key is Right key, keyRight changes back to False
                if event.key == pygame.K_RIGHT:
                    keyRight = False

                # If released key is Left key, keyLeft changes back to False    
                if event.key == pygame.K_LEFT:
                    keyLeft = False

                # If released key is Down key, keyDown changes back to False    
                if event.key == pygame.K_DOWN:
                    keyDown = False

                # If released key is Up key, keyUp changes back to False    
                if event.key == pygame.K_UP:
                    keyUp = False
    
        # THE FOLLOWING SECTION CONTROLS THE PLAYER

        # If up key is pressed and player Y position is greater than zero(Player within screen)
        # Player will move by 1.3 units upwards 
        if (keyUp == True) and (playerYposition > 0):                                        
                playerYposition -= 0.9   

        # If  down key is pressed and player Y position is within condition (Player within screen)
        # Player will move by 1.3 units downwards
        if (keyDown == True) and (playerYposition < (screen_height - player_height)):  
                playerYposition +=0.9

        # If Left key is pressed and player X position is great than zero( Player within screen)
        # Player will move to the left by 1.3 units
        if keyLeft == True and playerXposition > 0:
                playerXposition -= 0.9
                
        # If Right key is pressed and player X position suits if condition ( Player within screen)
        # Player will move to the right by 1.3 units
        if (keyRight == True) and (playerXposition < (screen_width - player_width)):
                playerXposition += 0.9
            
        # THE FOLLOWING SECTION CREATES A RECTANGLE AROUND ALL CHARACTERS RESPECTIVELY
        
        playerBox = pygame.Rect(player.get_rect()) # PLAYER: Creates a bounding box player
        playerBox.top = playerYposition            #        Tracks the X position of player so to keep box around Player 
        playerBox.left = playerXposition           #        Tracks the Y position of player so to keep box around Player

        # NOTE: Whats done on player will be done for every other character
        enemy1Box = pygame.Rect(enemy1.get_rect()) # ENEMY1 
        enemy1Box.top = enemy1Yposition
        enemy1Box.left = enemy1Xposition
    
        enemy2Box = pygame.Rect(enemy2.get_rect()) # ENEMY2
        enemy2Box.top = enemy2Yposition
        enemy2Box.left = enemy2Xposition
   
        enemy3Box = pygame.Rect(enemy3.get_rect()) # ENEMY3
        enemy3Box.top = enemy3Yposition
        enemy3Box.left = enemy3Xposition

        prizeBox = pygame.Rect(prize.get_rect())   # PRIZE
        prizeBox.top = prizeYposition
        prizeBox.left = prizeXposition

        collide = False   # Enables program to have control over following if, elif statements

        # On this if statement, if Player Box collides with any of the Enemy boxes:
        # Player loses and pygame is quited
        if ( playerBox.colliderect(enemy3Box)  or     
             playerBox.colliderect(enemy2Box)  or
             playerBox.colliderect(enemy1Box) ) :
                                    
            print("You lose!!")               # Lose display message to user

            collide = True 
            pygame.quit()                     # Exits game
            exit(0)
                 
        # If Player box did not collide with any enemy but rather collides with Prize first:
        # Player wins and pygame is quited
        elif playerBox.colliderect(prizeBox):
                
            print("You win!")                 # Win display message to user

            collide = True
            pygame.quit()                     # Quits game
            exit(0)

        # If the 2 previous control condition where not met(no collide):
        # Enemies and Prize will continue to move across the screen in search of Player
        elif not collide:

            # ENEMY1
            # This condition moves enemy1 to the right for as long as enemy1 is within the screen   
            if (0-enemy1_width) <= enemy1Xposition <= (screen_width + 150) :       
                enemy1Xposition += 0.8             # (+)Direction and (0.45) Speed at which Enemy moves at
                
            # Once enemy1 is out of screen, program gives new position to restart the approach
            else:
                enemy1Xposition = 0 - enemy1_width
                enemy1Yposition = random.randint(0, (screen_height-enemy1_height))
                

            # ENEMY2        
            # Condition moves enemy2 downwards as long as it is within the screen
            if (0-screen_height) <= enemy2Yposition <= (screen_height + 30):
                    enemy2Yposition += 0.9          # Direction and speed
                    
            # Once Enemy2 is out of screen, new posiyion is given to restart approach        
            else:    
                enemy2Xposition = random.randint(0, (screen_width- enemy2_width))
                enemy2Yposition = 0 -screen_height
                
                
            # ENEMY3
            # Condition moves Enemy3 to the left for as long as its within the screen
            if (0-enemy3_width) <= enemy3Xposition <= screen_width:
                enemy3Xposition -= 0.75             # Direction and speed
                
            # Gives new position once Enemy3 is out of screen
            else:
                enemy3Xposition = screen_width
                enemy3Yposition = random.randint(0, (screen_height- enemy1_height))

                
            # PRIZE
            # When condition is True, Prize character to move across screen for Player to capture 
            if (0-prize_width) <= prizeXposition <= (screen_width):
                prizeXposition -= 0.5  # Direction and speed

            # When Prize goes out of screen, new restart position is given    
            else:
                prizeYposition = random.randint(0, (screen_height-prize_height))
                prizeXposition = screen_width
                    
            # WHILE LOOP WILL REPEAT TILL USER WINS OR LOSES GAME.
