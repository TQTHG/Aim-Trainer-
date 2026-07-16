import pygame
import random
import time

running = True
mouse_click = "NO"
score = 0
miss = 0
time_count_down = 30
end_time = time.time() + 30
end = 0
reaction_time = 0
reaction = []
reaction_start = time.time()
reaction_time_tilte = 0
best_score = 0

# Screen
width = 1200
height = 800
size = 0
current_screen = "MENU"
difficulty_type = "Random"

x = random.randint(0 , width - size)
y = random.randint(0 , height - size)

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Aim Trainer")

# Color
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# Title
Aim_title = "Aim Trainer"
start = "Start Training"
difficulty = "Difficulty"
easy = "easy"
medium = "medium"
hard = "hard"
version = "v1.0"
fps_title = "FPS"
frame_rate = "60"
restart = "Restart"
back_menu = "Go Back To Menu"

# Font
Aim_title_font = pygame.font.Font(
    "d:\Programming\Python\Aims Training\Font\GreatsRacing-BLLM8.ttf",
    100
    )
start_font = pygame.font.Font(
    "d:\Programming\Python\Aims Training\Font\GreatsRacing-BLLM8.ttf",
    70
    )
difficulty_title_font = pygame.font.Font(
    "d:\Programming\Python\Aims Training\Font\SpaceNova-6Rpd1.ttf",
    30
    )
easy_font = pygame.font.Font(
    "d:\Programming\Python\Aims Training\Font\SpaceNova-6Rpd1.ttf",
    30
    )
score_font = pygame.font.Font(
    "d:\Programming\Python\Aims Training\Font\GreatsRacing-BLLM8.ttf",
    30
    )
version_font =  pygame.font.Font(
    "d:\Programming\Python\Aims Training\Font\GreatsRacing-BLLM8.ttf",
    20
    )
fps_font = pygame.font.Font(
     "d:\Programming\Python\Aims Training\Font\MontenegrinGothicOne-Regular.ttf",
    30
    )
result_font = pygame.font.Font(
    "d:\Programming\Python\Aims Training\Font\SpaceNova-6Rpd1.ttf",
    50
    )

# FPS
clock = pygame.time.Clock()
fps = 60
frame_count = 0
frame_delay = 0

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click = "YES"
    
    if current_screen == "MENU":
        screen.fill(black)

        mousepos = pygame.mouse.get_pos()

        version_text = version_font.render(version , True , white)
        version_rect = version_text.get_rect(bottomright = (width - 10 , 20))
        screen.blit(version_text,version_rect)

        Aim_title_text = Aim_title_font.render(Aim_title , True , white)
        Aim_title_rect = Aim_title_text.get_rect(midtop = (width / 2 , 10))
        screen.blit(Aim_title_text,Aim_title_rect)

        start_text = start_font.render(start , True , white)
        start_rect = start_text.get_rect(center = (width / 2 , height / 2))
        screen.blit(start_text,start_rect)

        difficulty_text = difficulty_title_font.render(f"{difficulty}:{difficulty_type}" , True , white)
        difficulty_rect = difficulty_text.get_rect(midtop = (width / 2, 150))
        screen.blit(difficulty_text,difficulty_rect)

        easy_text = easy_font.render(easy , True , white)
        easy_rect = easy_text.get_rect(center = (width / 2, 220))
        screen.blit(easy_text,easy_rect)

        medium_text = easy_font.render(medium , True , white)
        medium_rect = medium_text.get_rect(center = (width / 2, 260))
        screen.blit(medium_text,medium_rect)

        hard_text = easy_font.render(hard , True , white)
        hard_rect = easy_text.get_rect(center = (width / 2, 300))
        screen.blit(hard_text,hard_rect)

        fps_text = fps_font.render(f"{fps_title}: {frame_rate}" , True , white)
        fps_rect = fps_text.get_rect(center = (width / 2 , height / 2 + 100))
        screen.blit(fps_text,fps_rect)

        frame_rate_text = fps_font.render("60" , True , white)
        frame_rate_rect_1 = frame_rate_text.get_rect(center = (width / 2 - 150 , height / 2 + 150))
        screen.blit(frame_rate_text,frame_rate_rect_1)

        frame_rate_text = fps_font.render("90" , True , white)
        frame_rate_rect_2 = frame_rate_text.get_rect(center = (width / 2 - 100 , height / 2 + 150))
        screen.blit(frame_rate_text,frame_rate_rect_2)

        frame_rate_text = fps_font.render("120" , True , white)
        frame_rate_rect_3 = frame_rate_text.get_rect(center = (width / 2 - 40 , height / 2 + 150))
        screen.blit(frame_rate_text,frame_rate_rect_3)

        frame_rate_text = fps_font.render("144" , True , white)
        frame_rate_rect_4 = frame_rate_text.get_rect(center = (width / 2 + 30 , height / 2 + 150))
        screen.blit(frame_rate_text,frame_rate_rect_4)

        frame_rate_text = fps_font.render("165" , True , white)
        frame_rate_rect_5 = frame_rate_text.get_rect(center = (width / 2 + 100 , height / 2 + 150))
        screen.blit(frame_rate_text,frame_rate_rect_5)

        frame_rate_text = fps_font.render("240" , True , white)
        frame_rate_rect_6 = frame_rate_text.get_rect(center = (width / 2 + 170 , height / 2 + 150))
        screen.blit(frame_rate_text,frame_rate_rect_6)

        time_text = fps_font.render(f"Time out: {time_count_down}" , True , white)
        time_rect = time_text.get_rect(center = (width / 2 , height / 2 + 200))
        screen.blit(time_text,time_rect)

        time_text_1 = fps_font.render("15" , True , white)
        time_rect_1 = time_text_1.get_rect(center = (width / 2 - 50 , height / 2 + 230))
        screen.blit(time_text_1,time_rect_1)

        time_text_2 = fps_font.render("30" , True , white)
        time_rect_2 = time_text_2.get_rect(center = (width / 2  , height / 2 + 230))
        screen.blit(time_text_2,time_rect_2)

        time_text_3 = fps_font.render("60" , True , white)
        time_rect_3 = time_text_3.get_rect(center = (width / 2 + 50 , height / 2 + 230))
        screen.blit(time_text_3,time_rect_3)

        best_text = result_font.render(f"Best score: {best_score}" , True , white)
        best_rect = best_text.get_rect(center = (width / 2 , height /2 + 350))
        screen.blit(best_text,best_rect)

        if time_rect_1.collidepoint(mousepos):
            time_text_1 = fps_font.render("15" , True , red)
            screen.blit(time_text_1,time_rect_1)
            if mouse_click == "YES":
                time_count_down = 15
                end_time = time.time() + 15
                mouse_click = "NO"
        elif not time_rect_1.collidepoint(mousepos):
            if mouse_click == "YES":
                mouse_click == "NO"
        
        if time_rect_2.collidepoint(mousepos):
            time_text_2 = fps_font.render("30" , True , red)
            screen.blit(time_text_2,time_rect_2)
            if mouse_click == "YES":
                time_count_down = 30
                end_time = time.time() + 30
                mouse_click = "NO"
        elif not time_rect_2.collidepoint(mousepos):
            if mouse_click == "YES":
                mouse_click == "NO"

        if time_rect_3.collidepoint(mousepos):
            time_text_3 = fps_font.render("60" , True , red)
            screen.blit(time_text_3,time_rect_3)
            if mouse_click == "YES":
                time_count_down = 60
                end_time = time.time() + 60
                mouse_click = "NO"
        elif not time_rect_3.collidepoint(mousepos):
            if mouse_click == "YES":
                mouse_click == "NO"

        if frame_rate_rect_1.collidepoint(mousepos):
            frame_rate_text = fps_font.render("60" , True , red)
            screen.blit(frame_rate_text,frame_rate_rect_1)
            if mouse_click == "YES":
                frame_rate = "60"
                fps = 60
                mouse_click = "NO"
        elif not frame_rate_rect_1.collidepoint(mousepos):
            if mouse_click == "YES":
                mouse_click == "NO"

        if frame_rate_rect_2.collidepoint(mousepos):
            frame_rate_text = fps_font.render("90" , True , red)
            screen.blit(frame_rate_text,frame_rate_rect_2)
            if mouse_click == "YES":
                frame_rate = "90"
                fps = 90
                mouse_click = "NO"
        elif not frame_rate_rect_2.collidepoint(mousepos):
            if mouse_click == "YES":
                mouse_click == "NO"

        if frame_rate_rect_3.collidepoint(mousepos):
            frame_rate_text = fps_font.render("120" , True , red)
            screen.blit(frame_rate_text,frame_rate_rect_3)
            if mouse_click == "YES":
                frame_rate = "120"
                fps = 120
                mouse_click = "NO"
        elif not frame_rate_rect_3.collidepoint(mousepos):
            if mouse_click == "YES":
                mouse_click == "NO"

        if frame_rate_rect_4.collidepoint(mousepos):
            frame_rate_text = fps_font.render("144" , True , red)
            screen.blit(frame_rate_text,frame_rate_rect_4)
            if mouse_click == "YES":
                frame_rate = "144"
                fps = 144
                mouse_click = "NO"
        elif not frame_rate_rect_4.collidepoint(mousepos):
            if mouse_click == "YES":
                mouse_click == "NO"

        if frame_rate_rect_5.collidepoint(mousepos):
            frame_rate_text = fps_font.render("165" , True , red)
            screen.blit(frame_rate_text,frame_rate_rect_5)
            if mouse_click == "YES":
                frame_rate = "165"
                fps = 165
                mouse_click = "NO"
        elif not frame_rate_rect_5.collidepoint(mousepos):
            if mouse_click == "YES":
                mouse_click == "NO"

        if frame_rate_rect_6.collidepoint(mousepos):
            frame_rate_text = fps_font.render("240" , True , red)
            screen.blit(frame_rate_text,frame_rate_rect_6)
            if mouse_click == "YES":
                frame_rate = "240"
                fps = 240
                mouse_click = "NO"
        elif not frame_rate_rect_6.collidepoint(mousepos):
            if mouse_click == "YES":
                mouse_click == "NO"

        if start_rect.collidepoint(mousepos):
            start_text = start_font.render(start , True , red)
            screen.blit(start_text,start_rect)
            if mouse_click == "YES":
                current_screen = "TRAINING"
                mouse_click = "NO"
        elif not  start_rect.collidepoint(mousepos):
            if mouse_click == "YES":
                mouse_click == "NO"

        if easy_rect.collidepoint(mousepos):
            easy_text = easy_font.render(easy , True , green)
            screen.blit(easy_text,easy_rect)
            if mouse_click == "YES":
                easy_text = easy_font.render(easy , True , red)
                screen.blit(easy_text,easy_rect)
                difficulty_type = "EASY"
                mouse_click = "NO"
        elif not easy_rect.collidepoint(mousepos):
            if mouse_click == "YES":
                mouse_click == "NO"

        if medium_rect.collidepoint(mousepos):
            medium_text = easy_font.render(medium , True , blue)
            screen.blit(medium_text,medium_rect)
            if mouse_click == "YES":
                medium_text = easy_font.render(medium , True , green)
                screen.blit(medium_text,medium_rect)
                difficulty_type = "MEDIUM"
                mouse_click = "NO"
        elif not medium_rect.collidepoint(mousepos):
            if mouse_click == "YES":
                mouse_click == "NO"

        if hard_rect.collidepoint(mousepos):
            hard_text = easy_font.render(hard , True , red)
            screen.blit(hard_text,hard_rect)
            if mouse_click == "YES":
                hard_text = easy_font.render(hard , True , green)
                screen.blit(hard_text,hard_rect)
                difficulty_type = "HARD"
                mouse_click = "NO"
        elif not hard_rect.collidepoint(mousepos):
            if mouse_click == "YES":
                mouse_click == "NO"

    elif current_screen == "TRAINING":
        screen.fill(black)

        mousepos = pygame.mouse.get_pos()

        if difficulty_type == "Random":
            difficulty_type = random.choice(["EASY","MEDIUM","HARD"])
        elif difficulty_type == "EASY":
            frame_delay = fps * 2
            size = 50
        elif difficulty_type == "MEDIUM":
            frame_delay = fps * 1.5
            size = 40
        elif difficulty_type == "HARD":
            frame_delay = fps
            size = 30

        frame_count += 1
        if frame_count == frame_delay:

            x = random.randint(0 , width  - size *3)
            y = random.randint(0 , height - size * 3)

            frame_count = 0

        circle_x = x - size
        circle_y = y - size
        circle_width = size * 2
        circle_height = size * 2
        target = pygame.draw.circle(screen , green , (x , y ) , size)
        target_cir = pygame.Rect(circle_x,circle_y,circle_width,circle_height)

        reaction_end = time.time()
        if target_cir.collidepoint(mousepos):
            target = pygame.draw.circle(screen , red , (x , y ) , size)
            if mouse_click == "YES":
                score += 1
                frame_count = 0
                x = random.randint(0 , width - size*3)
                y = random.randint(0 , height - size*3)
                mouse_click = "NO"
                reaction_time = round((reaction_end - reaction_start),3)
                reaction_time_tilte = reaction_time
                reaction.append(reaction_time)
                reaction_start = time.time()
        elif not target_cir.collidepoint(mousepos):
            if mouse_click == "YES":
                miss += 1
                mouse_click = "NO"
   
        total_shots = score + miss
        if total_shots > 0 :
            Accuracy  = round((score / (score + miss)) * 100,2)
        else:
            Accuracy = 100

        time_left = round(end_time - time.time(),2)
        if time_left <=0:
            current_screen = "RESULT"
        
        score_text = fps_font.render(f"Score: {score}" , True , white)
        score_rect = score_text.get_rect(topleft = (10 , 0))
        screen.blit(score_text,score_rect)

        miss_text = fps_font.render(f"Miss: {miss}" , True , white)
        miss_rect = miss_text.get_rect(topright = (width - 10 , 0))
        screen.blit(miss_text,miss_rect)

        Accuracy_text = fps_font.render(f"Accuracy : {Accuracy}%" , True , white)
        Accuracy_rect = Accuracy_text.get_rect(bottomright = (width - 10 , height))
        screen.blit(Accuracy_text,Accuracy_rect)

        difficulty_text = fps_font.render(f"{difficulty}:{difficulty_type}" , True , white)
        difficulty_rect = difficulty_text.get_rect(bottomleft = (10 , height))
        screen.blit(difficulty_text,difficulty_rect)

        time_text = fps_font.render(f"Time left: {time_left}" , True , white)
        time_rect = time_text.get_rect(midtop = (width / 2 , 0))
        screen.blit(time_text,time_rect)

        reaction_text = fps_font.render(f"Reaction time: {reaction_time_tilte}" , True , white)
        reaction_rect = reaction_text.get_rect(center = (width / 2 , height - 20))
        screen.blit(reaction_text,reaction_rect)

    elif current_screen == "RESULT":
        screen.fill(black)

        mousepos = pygame.mouse.get_pos()

        result_text  = Aim_title_font.render("RESULT" , True , white)
        result_rect = result_text.get_rect(midtop = (width / 2 , 100))
        screen.blit(result_text,result_rect)

        score_text = result_font.render(f"Score: {score}" , True , white)
        score_rect = score_text.get_rect(center = (width / 2 , height / 2 - 150))
        screen.blit(score_text,score_rect)

        miss_text = fps_font.render(f"Miss_click: {miss}" , True , white)
        miss_rect = miss_text.get_rect(center = (width / 2 , height / 2 - 100))
        screen.blit(miss_text,miss_rect)

        Accuracy_text = fps_font.render(f"Accuracy : {Accuracy}%" , True , white)
        Accuracy_rect = Accuracy_text.get_rect(center = (width / 2 , height / 2 - 50))
        screen.blit(Accuracy_text,Accuracy_rect)
        if sum(reaction) > 0:
            reaction_avg = round((sum(reaction) / len(reaction) )  *1000)
        else:
            reaction_avg = "None"
        reaction_text = fps_font.render(f"Reaction time average: {reaction_avg}ms" , True , white)
        reaction_rect = reaction_text.get_rect(center = (width / 2 , height / 2 ))
        screen.blit(reaction_text,reaction_rect)

        restart_text = Aim_title_font.render(restart , True , white)
        restart_rect = restart_text.get_rect(center=(width / 2,height / 2 + 200))
        screen.blit(restart_text,restart_rect)

        back_menu_text = Aim_title_font.render(back_menu , True , white)
        back_menu_rect = back_menu_text.get_rect(center=(width / 2, height / 2 + 300))
        screen.blit(back_menu_text,back_menu_rect)

        if score > best_score:
            best_score = score

        if restart_rect.collidepoint(mousepos):
            restart_text = Aim_title_font.render(restart , True , green)
            screen.blit(restart_text,restart_rect)
            if mouse_click == "YES":
                score = 0
                frame_count = 0
                reaction = []
                reaction_time = 0
                reaction_time_tilte = 0
                miss = 0
                end_time = time.time() + time_count_down
                current_screen = "TRAINING"
                mouse_click = "NO"

        if back_menu_rect.collidepoint(mousepos):
            back_menu_text = Aim_title_font.render(back_menu , True , green)
            screen.blit(back_menu_text,back_menu_rect)
            if mouse_click == "YES":
                current_screen = "MENU"
                score = 0
                frame_count = 0
                reaction = []
                reaction_time = 0
                reaction_time_tilte = 0
                miss = 0
                end_time = time.time() + 3
                mouse_click = "NO"

    clock.tick(fps)
    pygame.display.update()
pygame.quit()