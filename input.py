import pygame
import socket
import sys
import threading

PORT = 5050
SERVER = '10.0.0.27'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(ADDR)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(ADDR)

pygame.init()
width = 100
window = pygame.display.set_mode((width, width))


def main():
    directionf = ''
    directionb = ''
    speed = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_1]:
                    speed = 51
                elif keys[pygame.K_2]:
                    speed = 102
                elif keys[pygame.K_3]:
                    speed = 153
                elif keys[pygame.K_4]:
                    speed = 204
                elif keys[pygame.K_d]:
                    speed = 255

                if keys[pygame.K_d]:
                    directionf = 'r'
                    print(f_wheel_l, f_wheel_r, b_wheel_l, b_wheel_r)
                elif keys[pygame.K_a]:
                    directionf = 'l'
                    print(f_wheel_l, f_wheel_r, b_wheel_l, b_wheel_r)
                elif keys[pygame.K_w]:
                    directionb = 'f'
                    directionf = 'f'
                    print(f_wheel_l, f_wheel_r, b_wheel_l, b_wheel_r)
                elif keys[pygame.K_s]:
                    directionb = 'b'
                    directionf = 'b'
                    print(f_wheel_l, f_wheel_r, b_wheel_l, b_wheel_r)
        
        f_wheel_l = [directionf, speed]
        f_wheel_r = [directionf, speed]
        b_wheel_l = [directionb, speed]
        b_wheel_r = [directionb, speed]
        
        pygame.display.update()


if __name__ == "__main__":
    main()
