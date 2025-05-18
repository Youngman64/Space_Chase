import pygame
import os
import random
import time

pygame.init()

# Constants
WIDTH, HEIGHT = 854, 480
FULLSCREEN_WIDTH, FULLSCREEN_HEIGHT = 1080, 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT_COLOR = (255, 255, 0)
RED = (200, 0, 0)
ORANGE = (255, 165, 0)
GREEN = (0, 155, 155)
FPS = 60

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Space Chase")
clock = pygame.time.Clock()
fullscreen = False

#assets
character_folder = "space_chase_assets"
character_files = ["electro_1.png", "vermus_1.png", "zicro_1.png"]
enemy_file = "zicro_4.png"
background_img = pygame.image.load(os.path.join(character_folder, "background_1.png"))
title_screen_img = pygame.image.load(os.path.join(character_folder, "title_screen.png"))
characters = [pygame.image.load(os.path.join(character_folder, img)) for img in character_files]
enemy_img = pygame.image.load(os.path.join(character_folder, enemy_file))
credit_img = pygame.transform.scale(pygame.image.load(os.path.join(character_folder, "credit.png")), (70, 70))
rocketship_img = pygame.transform.scale(pygame.image.load(os.path.join(character_folder, "rocketship.png")), (100, 100))

# Music and sound
menu_music = os.path.join(character_folder, "menu_music.wav")
game_music = os.path.join(character_folder, "Merth_1.2.wav")
beep_sound = pygame.mixer.Sound(os.path.join(character_folder, "beep.mp3"))

#img resizing
character_scaled = [pygame.transform.scale(char, (200, 200)) for char in characters]
game_character_scaled = [pygame.transform.scale(char, (100, 100)) for char in characters]
enemy_img = pygame.transform.scale(enemy_img, (100, 100))

# Global state for screen navigation
TITLE, HOW_TO_PLAY, CHARACTER_SELECT, GAME = "title", "how_to_play", "character_select", "game"
screen_state = TITLE

def draw_menu(screen, options, selected_index, y_start):
    font = pygame.font.Font(None, 48)
    for i, text in enumerate(options):
        color = HIGHLIGHT_COLOR if i == selected_index else WHITE
        rendered = font.render(text, True, color)
        rect = rendered.get_rect(center=(screen.get_width() // 2, y_start + i * 60))
        screen.blit(rendered, rect)

#Title Screen
def title_screen():
    global screen_state
    selected = 0
    options = ["Character Select", "How To Play"]
    running = True

    while running and screen_state == TITLE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        screen_state = CHARACTER_SELECT
                        return
                    elif selected == 1:
                        screen_state = HOW_TO_PLAY
                        return

        screen.fill(ORANGE)
        screen.blit(pygame.transform.scale(title_screen_img, screen.get_size()), (0, 0))
        draw_menu(screen, options, selected, y_start=250)
        hint_font = pygame.font.Font(None, 28)
        hint_text = hint_font.render("Hit ENTER to select", True, WHITE)
        screen.blit(hint_text, (screen.get_width() // 2 - hint_text.get_width() // 2, screen.get_height() - 40))

        pygame.display.flip()
        clock.tick(FPS)

#How to play screen
def how_to_play_screen():
    global screen_state
    running = True
    font = pygame.font.Font(None, 32)

    # Pre-render all text surfaces once (not every frame)
    lines = [
        "Objective: Run away from the enemy.",
        "Once you have collected the required amount of credits,",
        "a rocket ship will appear that can take you to the next level.",
        "Try to beat all 10 levels!",
        "",
        "Controls:",
        "Move with arrow keys.",
        "Activate ability with SPACE.",
        "Select with ENTER.",
        "",
        "Press BACKSPACE to return."
    ]
    rendered_lines = [font.render(line, True, WHITE) for line in lines]

    while running and screen_state == HOW_TO_PLAY:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                screen_state = TITLE
                return

        screen.fill(ORANGE)
        for i, rendered in enumerate(rendered_lines):
            screen.blit(rendered, (50, 50 + i * 35))

        pygame.display.flip()
        clock.tick(FPS)
#Background tints
level_colors = [
    (50, 50, 200), (100, 50, 180), (150, 50, 160), (200, 50, 140), (250, 50, 120),
    (250, 100, 100), (250, 150, 80), (250, 200, 60), (250, 250, 40), (200, 250, 60)
]

#function for updating screen size
def update_screen_size():
    global screen, background_img
    if fullscreen:
        screen = pygame.display.set_mode((FULLSCREEN_WIDTH, FULLSCREEN_HEIGHT), pygame.RESIZABLE)
    else:
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    background_img = pygame.transform.scale(pygame.image.load(os.path.join(character_folder, "background_1.png")), screen.get_size())

#function for updating character positions
def update_character_positions():
    global char_positions
    char_positions = [
        (screen.get_width() // 4 - 100, screen.get_height() // 2 - 100),
        (screen.get_width() // 2 - 100, screen.get_height() // 2 - 100),
        (3 * screen.get_width() // 4 - 100, screen.get_height() // 2 - 100)
    ]

update_character_positions()
character_names = ["Electro", "Vermus", "Zicro"]

#Game Over :(
def game_over():
    font = pygame.font.Font(None, 74)
    text = font.render("GAME OVER", True, RED)
    screen.fill(BLACK)
    screen.blit(text, (screen.get_width()//2 - 150, screen.get_height()//2 - 50))
    pygame.display.flip()
    pygame.time.delay(2000)

#Winner Screen
def you_win_screen():
    font = pygame.font.Font(None, 74)
    text = font.render("YOU WIN!", True, GREEN)
    screen.fill(BLACK)
    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() // 2 - 50))
    pygame.display.flip()
    pygame.time.delay(3000)  # Show for 3 seconds

#Main menu
def main_menu():
    global fullscreen, high_score
    font = pygame.font.Font(None, 48)
    small_font = pygame.font.Font(None, 36)
    selected_index = 0
    running = True
    pygame.mixer.music.load(menu_music)
    pygame.mixer.music.play(-1)

    while running:
        screen.fill(ORANGE)
        update_character_positions()

        for i, char in enumerate(character_scaled):
            x, y = char_positions[i]
            screen.blit(char, (x, y))
            text_surface = font.render(character_names[i], True, WHITE)
            screen.blit(text_surface, (x + 50, y - 40))

            if i == selected_index:
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, (x-5, y-5, 210, 210), 5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected_index = (selected_index - 1) % len(characters)
                elif event.key == pygame.K_RIGHT:
                    selected_index = (selected_index + 1) % len(characters)
                elif event.key == pygame.K_RETURN:
                    return selected_index
                elif event.key == pygame.K_f:
                    fullscreen = not fullscreen
                    update_screen_size()
                    update_character_positions()

        pygame.display.flip()
        clock.tick(FPS)

#Game loop with levels
def game_loop(player_index):
    global background_img, high_score
    player_img = game_character_scaled[player_index]
    base_speed = 5
    player_speed = base_speed
    ability_available = True
    ability_cooldown = 15
    ability_duration = 5   
    last_ability_time = 0
    ability_active = False
    ability_start_time = 0
    invincible = False
    level = 1
    enemy_base_speed = 2  # Starting speed
    max_level = 10
    credits_collected = 0
    credits_required = 50

    pygame.mixer.music.load(game_music)
    pygame.mixer.music.play(-1)

    #rainbow invincibility
    rainbow_colors = [(255,0,0), (255,127,0), (255,255,0), (0,255,0), (0,0,255), (75,0,130), (139,0,255)]
    def apply_rainbow_tint(image, frame):
        tint_color = rainbow_colors[frame % len(rainbow_colors)]
        tinted_image = image.copy()
        tint_surface = pygame.Surface(tinted_image.get_size(), pygame.SRCALPHA)
        tint_surface.fill(tint_color + (100,))
        tinted_image.blit(tint_surface, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)
        return tinted_image
    # Magnet effect for Zicro
    MAGNET_RADIUS = 150

    def apply_magnet_effect(player_x, player_y, credit_positions):
        for i, (cx, cy) in enumerate(credit_positions):
            dx = player_x - cx
            dy = player_y - cy
            distance = (dx**2 + dy**2) ** 0.5
            if distance < MAGNET_RADIUS and distance != 0:
                move_x = dx / distance * 5
                move_y = dy / distance * 5
                credit_positions[i] = (cx + move_x, cy + move_y)
        return credit_positions
    def draw_ability_bar(surface, x, y, width, height, fill_ratio):
        background = pygame.Surface((width, height), pygame.SRCALPHA)
        background.fill((50, 50, 50, 180))  # Slightly transparent background
        surface.blit(background, (x, y))
        fill_width = int(width * fill_ratio)
        pygame.draw.rect(surface, GREEN, (x, y, fill_width, height))
        font = pygame.font.Font(None, 24)
        label = font.render("Ability", True, WHITE)
        surface.blit(label, (x, y - 20))

    while level <= max_level:
        player_x, player_y = 50, screen.get_height() - 150  # bottom-left
        enemy_x, enemy_y = screen.get_width() - 150, 50     # top-right
        enemy_speed = min(base_speed - 1, enemy_base_speed + (level - 1) * 0.1)

        credit_positions = [
            (random.randint(0, screen.get_width() - 70), random.randint(0, screen.get_height() - 70))
            for _ in range(5)
        ]
        rocketship_spawned = False
        rocketship_x, rocketship_y = None, None
        background_img = pygame.transform.scale(
            pygame.image.load(os.path.join(character_folder, "background_1.png")), screen.get_size()
        ).copy()
        tint_surface = pygame.Surface(background_img.get_size())
        tint_surface.fill(level_colors[level - 1])
        background_img.blit(tint_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        running = True

        while running:
            screen.fill(BLACK)
            screen.blit(background_img, (0, 0))

            # Ability timer handling for Electro (index 0)
            current_time = time.time()
            if ability_active and current_time - ability_start_time > ability_duration:
                ability_active = False
                last_ability_time = current_time
                if player_index == 0:
                    player_speed = base_speed
                elif player_index == 1:
                    invincible = False

            if not ability_active and not ability_available and current_time - last_ability_time > ability_cooldown:
                ability_available = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]: player_x -= player_speed
            if keys[pygame.K_RIGHT]: player_x += player_speed
            if keys[pygame.K_UP]: player_y -= player_speed
            if keys[pygame.K_DOWN]: player_y += player_speed

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and ability_available:
                        ability_active = True
                        ability_available = False
                        ability_start_time = current_time
                        if player_index == 0:
                            player_speed = base_speed * 2
                        elif player_index == 1:
                            invincible = True

            player_x = max(0, min(screen.get_width() - 100, player_x))
            player_y = max(0, min(screen.get_height() - 100, player_y))

            if enemy_x < player_x: enemy_x += enemy_speed
            if enemy_x > player_x: enemy_x -= enemy_speed
            if enemy_y < player_y: enemy_y += enemy_speed
            if enemy_y > player_y: enemy_y -= enemy_speed

            if player_index == 1 and invincible:
                tinted_img = apply_rainbow_tint(player_img, int(time.time() * 10))
                screen.blit(tinted_img, (player_x, player_y))
            else:
                screen.blit(player_img, (player_x, player_y))
            
            screen.blit(enemy_img, (enemy_x, enemy_y))

            if player_index == 2 and ability_active:
                credit_positions = apply_magnet_effect(player_x, player_y, credit_positions)

            for pos in credit_positions[:]:
                screen.blit(credit_img, pos)
                if credits_collected < credits_required:
                    if abs(player_x - pos[0]) < 40 and abs(player_y - pos[1]) < 40:
                        credit_positions.remove(pos)
                        credits_collected += 5
                        beep_sound.play()
                        credit_positions.append((random.randint(0, screen.get_width() - 70), random.randint(0, screen.get_height() - 70)))

            if credits_collected >= credits_required and not rocketship_spawned:
                rocketship_x = random.randint(0, screen.get_width() - 100)
                rocketship_y = random.randint(0, screen.get_height() - 100)
                rocketship_spawned = True

            if rocketship_spawned:
                screen.blit(rocketship_img, (rocketship_x, rocketship_y))
                if abs(player_x - rocketship_x) < 50 and abs(player_y - rocketship_y) < 50:
                    level += 1
                    credits_collected -= (50 + (level - 2) * 10)
                    credits_required += 10
                    running = False

            if not invincible and abs(player_x - enemy_x) < 50 and abs(player_y - enemy_y) < 50:
                game_over()
                return

            font = pygame.font.Font(None, 36)
            level_text = font.render(f"Level: {level}", True, WHITE)
            credits_text = font.render(f"Credits: {credits_collected}/{credits_required}", True, WHITE)
            screen.blit(level_text, (10, 10))
            screen.blit(credits_text, (10, 50))

            
            # Calculate fill ratio for ability bar
            if ability_active:
                fill_ratio = max(0, 1 - (current_time - ability_start_time) / ability_duration)
            elif not ability_available:
                fill_ratio = min(1, (current_time - last_ability_time) / ability_cooldown)
            else:
                fill_ratio = 1
            # Draw the ability bar in bottom-left corner
            draw_ability_bar(screen, 20, screen.get_height() - 40, 120, 15, fill_ratio)

            pygame.display.flip()
            clock.tick(FPS)
            if level > max_level:
                you_win_screen()


# Entry point with persistent music and screen routing
if __name__ == "__main__":
    pygame.mixer.music.load(menu_music)
    pygame.mixer.music.play(-1)

    while True:
        if screen_state == TITLE:
            title_screen()
        elif screen_state == HOW_TO_PLAY:
            how_to_play_screen()
        elif screen_state == CHARACTER_SELECT:
            selected_character = main_menu()
            if selected_character is not None:
                screen_state = GAME
                game_loop(selected_character)
                screen_state = TITLE
            else:
                screen_state = TITLE
        else:
            break

pygame.quit()
