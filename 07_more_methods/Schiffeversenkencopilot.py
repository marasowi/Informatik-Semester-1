
from random import randint

grid = [["~","~","~","~","~","~","~","~","~","~",],
        ["~","~","~","~","~","~","~","~","#","~",],
        ["~","#","~","#","#","#","#","#","~","~",],
        ["~","#","~","~","~","~","~","~","~","~",],
        ["~","#","~","#","#","#","#","~","~","~",],
        ["~","~","~","~","~","~","~","~","~","~",],
        ["~","~","~","#","~","~","~","#","#","~",],
        ["~","~","~","#","~","~","~","~","~","~",],
        ["~","~","~","#","~","~","~","~","~","~",],
        ["~","~","~","~","~","~","~","~","~","~",],]
schiff_getroffen = "X"
wasser_getroffen = "O"
wasser = "~"
schiff = "#"

def render_grid(l_grid):
    for row in l_grid:
        for field in row:
            print(field,end="")
        print()

def check_end_game(l_grid):
    for row in l_grid:
        if schiff in row:
            return False
    return True

def get_neighbors(x, y):
    nachbarn = []
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 10 and 0 <= ny < 10:
            nachbarn.append((nx, ny))
    return nachbarn

def shoot_on_board(l_grid, treffer_liste, geschossen):
    # Wenn es offene Treffer gibt, gezielt weiterschießen
    while treffer_liste:
        tx, ty = treffer_liste[0]
        for nx, ny in get_neighbors(tx, ty):
            if (nx, ny) not in geschossen:
                return nx, ny
        treffer_liste.pop(0)  # Keine offenen Nachbarn mehr, entferne Treffer
    # Sonst zufällig schießen
    while True:
        x = randint(0,9)
        y = randint(0,9)
        if (x, y) not in geschossen:
            return x, y

# ...existing code...

render_grid(grid)
geschossen = set()
treffer_liste = []
versuche = 0  # Zähler für die Anzahl der Versuche


while not check_end_game(grid):
    x, y = shoot_on_board(grid, treffer_liste, geschossen)
    geschossen.add((x, y))
    versuche += 1
    if grid[y][x] == schiff:
        grid[y][x] = schiff_getroffen
        treffer_liste.append((x, y))
    elif grid[y][x] == wasser:
        grid[y][x] = wasser_getroffen
    print("\033[H\033[J", end="")
    render_grid(grid)
    # time.sleep(0.1)  # Optional: kurze Pause zwischen den Zügen

print("Alle Schiffe versenkt!")
print(f"Anzahl der Versuche: {versuche}")



