import pygame, math

WIDTH = 1280
HEIGHT = 720
FPS = 60
TITLE = "Shapes"
BACKGROUND_COLOR = (30,30,40)
POINT_COLOR = (255,255,255)
SHAPE_COLOR = (255,180,180)
points = []
dragging_index = None

def handle_events():
    global dragging_index
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            grabbed = False
            for i in range(len(points)):
                x = points[i][0]
                y = points[i][1]

                deadzone = 20

                if math.dist(pos,(x,y)) <= deadzone:
                    dragging_index = i
                    print(dragging_index)
                    grabbed = True
                    break
            
            if not grabbed:
                points.append([pos[0], pos[1]])
                
            
        
        if event.type == pygame.MOUSEBUTTONUP:
            dragging_index = None

    return True


def update(dt):
    global dragging_index
    pos = pygame.mouse.get_pos()
    if dragging_index is not None:
        points[dragging_index] = [pos[0], pos[1]]
    


def draw(screen):
    screen.fill(BACKGROUND_COLOR)

    # Draw game objects here.
    for point in points:
        pygame.draw.circle(screen, POINT_COLOR, point, 3)
        

    if len(points) > 2:
        hull = generate_convex_hull()
        pygame.draw.polygon(screen, SHAPE_COLOR, hull)


    pygame.display.flip()

def cross_product(a, b, c):
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        - (b[1] - a[1]) * (c[0] - a[0])
    )

def generate_convex_hull():
    ltr_points = sorted(points, key=get_pos)
    lower = []

    for point in ltr_points:
        lower.append(point)

        while len(lower) >= 3 and cross_product(lower[-3], lower[-2], lower[-1]) <= 0:
            lower.remove(lower[-2])


    rtl_points = sorted(points, key=get_pos, reverse=True)
    upper = []
    for point in rtl_points:
        upper.append(point)

        while len(upper) >= 3 and cross_product(upper[-3], upper[-2], upper[-1]) <= 0:
            upper.remove(upper[-2])
    

    return lower[:-1] + upper[:-1]


def get_pos(point):
    return point[0], point[1]

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame Boilerplate")

    clock = pygame.time.Clock()
    running = True

    while running:
        dt = clock.tick(FPS) / 1000.0
        running = handle_events()
        update(dt)
        draw(screen)

    pygame.quit()


if __name__ == "__main__":
    main()
