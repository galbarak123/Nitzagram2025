import pygame

from constants import *
from helpers import screen


class Post:
    """
    A class used to represent post on Nitzagram
    """
    def _init_(self, username, location, description, likes_counter, comments_display_index):
        self.comments_display_index = comments_display_index
        self.comments = []
        self.likes_counter = likes_counter
        self.description = description
        self.location = location
        self.username = username

    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        # TODO: write me!
        def main():
            pygame.init()
            global screen
            screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
            screen = pygame.display.set_mode(screen_size)
            finish = False
            while not finish:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        finish = True
                    if event.type == event_type:
                        #some code
                pygame.display.flip()
            pygame.QUIT

        main()



    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break



