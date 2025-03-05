import pygame

from constants import *
from helpers import screen


class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self, username, location, description, likes_counter, comments_display_index):
        self.comments_display_index = comments_display_index
        self.comments = []
        self.likes_counter = likes_counter
        self.description = description
        self.location = location
        self.username = username

    def add_like(self):
        self.likes_counter += 1

    def add_comment(self, text):
        self.comments.append(text)

    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        self.username_()
        self.location_()
        self.description_()
        self.likes_counter_()
    def username_(self):
        USER_NAME_X_POS = 0.178 * WINDOW_WIDTH
        USER_NAME_Y_POS = 0.146 * WINDOW_HEIGHT
        font = pygame.font.SysFont('Georgia',
                                   20)
        text = font.render(self.username, True,
                           "black")
        screen.blit(text, (USER_NAME_X_POS, USER_NAME_Y_POS))

    def location_(self):
        LOCATION_TEXT_X_POS = 0.178 * WINDOW_WIDTH
        LOCATION_TEXT_Y_POS = 0.17 * WINDOW_HEIGHT
        font = pygame.font.SysFont('Georgia',
                                   19)
        text = font.render(self.location, True,
                           (50, 50, 50))
        screen.blit(text, [LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS])

    def description_(self):
        DESCRIPTION_TEXT_X_POS = 0.111 * WINDOW_WIDTH
        DESCRIPTION_TEXT_Y_POS = 0.678 * WINDOW_HEIGHT
        font = pygame.font.SysFont('Georgia',
                                   20)
        text = font.render(self.description, True,
                           "black")
        screen.blit(text, [DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS])

    def likes_counter_(self):
        LIKE_TEXT_X_POS = 0.111 * WINDOW_WIDTH
        LIKE_TEXT_Y_POS = 0.658 * WINDOW_HEIGHT
        font = pygame.font.SysFont('Georgia',
                                   20)
        text = font.render(str(self.likes_counter), True,
                           "black")
        screen.blit(text, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))


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

class ImagePost(Post):
    def __init__(self, username, location, description, likes_counter, comments_display_index, image):
        super().__init__(username, location, description, likes_counter, comments_display_index)
        self.image = image

    def display(self):
        super().display()
        POST_WIDTH = 0.87 * WINDOW_WIDTH
        POST_HEIGHT = 0.41 * WINDOW_HEIGHT
        POST_X_POS = 0.064 * WINDOW_WIDTH
        POST_Y_POS = 0.2 * WINDOW_HEIGHT
        img = pygame.transform.scale(self.image,(POST_WIDTH, POST_HEIGHT))
        screen.blit(img, (POST_X_POS, POST_Y_POS))
