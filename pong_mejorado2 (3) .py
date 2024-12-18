import py5

# Variables globales para el estado del juego
paddle1_y = paddle2_y = 0
paddle_width = 20
paddle1_height = paddle2_height = 100
paddle_speed = 7
ball_size = 20
ball_x = ball_y = ball_dx = ball_dy = 0
player1_score = player2_score = 0
keys = set()

# Colores personalizados
background_color = (135, 206, 250)  # Celeste
paddle_color = (255, 255, 255)  # Blanco
ball_color = (255, 255, 255)

# Configuración inicial de dificultad
def setup():
    global ball_x, ball_y, ball_dx, ball_dy
    global paddle1_y, paddle2_y

    py5.size(800, 400)
    reset_game()

def reset_game():
    global ball_x, ball_y, ball_dx, ball_dy, paddle1_y, paddle2_y
    global player1_score, player2_score, paddle1_height, paddle2_height

    ball_x = py5.width / 2
    ball_y = py5.height / 2
    ball_dx = 5 if py5.random(1) > 0.5 else -5
    ball_dy = py5.random(-3, 3)
    paddle1_y = py5.height / 2 - paddle1_height / 2
    paddle2_y = py5.height / 2 - paddle2_height / 2
    player1_score = 0
    player2_score = 0
    paddle1_height = paddle2_height = 100

def draw():
    global ball_x, ball_y, ball_dx, ball_dy, paddle1_y, paddle2_y

    py5.background(*background_color)

    # Dibujar palas, pelota y marcador
    draw_paddles()
    draw_ball()
    draw_score()

    # Actualizar posición de la pelota
    ball_x += ball_dx
    ball_y += ball_dy

    # Manejo de rebotes
    handle_ball_collisions()

    # Manejo de colisiones con las palas
    handle_paddle_collisions()

    # Actualización del marcador
    update_score()

    # Movimiento de las palas
    move_paddles()

def draw_paddles():
    py5.fill(*paddle_color)
    py5.rect(30, paddle1_y, paddle_width, paddle1_height)
    py5.rect(py5.width - 30 - paddle_width, paddle2_y, paddle_width, paddle2_height)

def draw_ball():
    py5.fill(*ball_color)
    py5.ellipse(ball_x, ball_y, ball_size, ball_size)

def draw_score():
    py5.text_size(32)
    py5.text_align(py5.CENTER)
    py5.fill(*paddle_color)
    py5.text(f"{player1_score} - {player2_score}", py5.width / 2, 40)

def handle_ball_collisions():
    global ball_dy
    if ball_y <= ball_size / 2 or ball_y >= py5.height - ball_size / 2:
        ball_dy *= -1

def handle_paddle_collisions():
    global ball_dx, ball_x
    # Colisión con la pala izquierda
    if ball_x - ball_size / 2 <= 30 + paddle_width:
        if paddle1_y < ball_y < paddle1_y + paddle1_height:
            ball_dx *= -1
            ball_x = 30 + paddle_width + ball_size / 2
    # Colisión con la pala derecha
    if ball_x + ball_size / 2 >= py5.width - 30 - paddle_width:
        if paddle2_y < ball_y < paddle2_y + paddle2_height:
            ball_dx *= -1
            ball_x = py5.width - 30 - paddle_width - ball_size / 2

def update_score():
    global player1_score, player2_score, paddle1_height, paddle2_height
    if ball_x < 0:
        player2_score += 1
        adjust_paddle_sizes(2)
        reset_ball()
    if ball_x > py5.width:
        player1_score += 1
        adjust_paddle_sizes(1)
        reset_ball()

def adjust_paddle_sizes(scoring_player):
    global paddle1_height, paddle2_height
    change = 10  # Incremento/disminución del tamaño
    if scoring_player == 1:
        paddle1_height = min(200, paddle1_height + change)
        paddle2_height = max(50, paddle2_height - change)
    elif scoring_player == 2:
        paddle2_height = min(200, paddle2_height + change)
        paddle1_height = max(50, paddle1_height - change)

def reset_ball():
    global ball_x, ball_y, ball_dx, ball_dy
    ball_x = py5.width / 2
    ball_y = py5.height / 2
    ball_dx *= -1
    ball_dy = py5.random(-3, 3)

def move_paddles():
    global paddle1_y, paddle2_y
    if 'w' in keys and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if 's' in keys and paddle1_y < py5.height - paddle1_height:
        paddle1_y += paddle_speed
    if 'o' in keys and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if 'l' in keys and paddle2_y < py5.height - paddle2_height:
        paddle2_y += paddle_speed

def key_pressed():
    keys.add(py5.key)

def key_released():
    keys.discard(py5.key)

if __name__ == "__main__":
    py5.run_sketch()
