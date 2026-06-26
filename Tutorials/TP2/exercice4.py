# Fontion fournie ne pas modifier
clearConsole = lambda: print('\n' * 10)

def print_table(table):
    # Dimension 1 = ligne
    # Dimension 2 = colonne
    clearConsole()
    for i, row in enumerate(table):
        row_str = "{:>2}" * len(row)
        row_str = row_str.format(*row)
        print("{:^20}".format(row_str), '\n')

# ________________________________________________________________

# Ajout de quelques constantes utilisées dans le code.
# Types de positions / types de cases
CASE_LIBRE = "_"
JOUEUR = "O"
SORTIE = "X"
MUR = "W"

# Directions
UP = "up"
RIGHT = "right"
DOWN = "down"
LEFT = "left"

# Partie 1
def init_maze(nb_row, nb_col, player_pos, end_pos, walls):
    # TODO Générer un labyrinthe vide -> rempli de "_"
    maze = [[CASE_LIBRE] * nb_col for _ in range(nb_row)]

    # TODO Placer le joueur "O", la sortie "X", les murs "W".
    maze[player_pos[0]][player_pos[1]] = JOUEUR
    maze[end_pos[0]][end_pos[1]] = SORTIE
    for wall in walls:
        maze[wall[0]][wall[1]] = MUR

    return maze


# Partie 2
def validate_move(maze, new_player_pos):
    result = False
    # TODO Vérifier si la position est valide -> dans le labyrinthe et pas sur un mur
    nb_row = len(maze)
    nb_col = len(maze[0])

    # Permet de vérifier que la position est située dans le labyrinthe.
    if (new_player_pos[0] in range(nb_row)) and (new_player_pos[1] in range(nb_col)):
        if maze[new_player_pos[0]][new_player_pos[1]] != MUR:
            result = True
  
    return result


#Partie 3
def move(key_pressed, maze, player_pos):
    # TODO Créer le dictionnaire d'équivalence entre la touche appuyée et la direction ("up", "left", "down", "right")
    conversion_touche_direction = {"w": UP, "a": LEFT, "s": DOWN, "d": RIGHT}
   
    # TODO Vérifier si la touche appuyée est dans le dictionnaire
    if key_pressed in conversion_touche_direction.keys():
    
    # TODO Récupérer la direction du mouvement
        direction = conversion_touche_direction[key_pressed]
       
        # TODO Générer la position potentielle du joueur en fonction de la direction
        position_potentielle = player_pos.copy()
        if direction == UP:
            position_potentielle[0] -= 1
        elif direction == DOWN:
            position_potentielle[0] += 1
        elif direction == LEFT:
            position_potentielle[1] -= 1
        elif direction == RIGHT:
            position_potentielle[1] += 1

        # TODO Changer réellement la position du joueur
        if validate_move(maze, position_potentielle):
            # Vider la position du joueur dans le jeu.
            maze[player_pos[0]][player_pos[1]] = CASE_LIBRE
            # Déplacer le joueur.
            player_pos = position_potentielle
            # Placer le joueur à la nouvelle position, vide.
            maze[player_pos[0]][player_pos[1]] = JOUEUR

    return maze, player_pos


if __name__ == '__main__':
    nb_row = 4
    nb_col = 7
    player_pos = [0, 0]  # TODO Définir la position ligne, colonne sur en haut à gauche
    end_pos = [3, 6]  # TODO Définir la position ligne, colonne sur en bas à droite
    # Coordoné sous la forme (ligne, colone)
    walls = [[0, 1],[1, 1], [1, 2], [1, 3], [1, 5], [2, 1], [2, 5], [3, 3], [3, 5]]
    maze = init_maze(nb_row, nb_col, player_pos, end_pos, walls)

    print_table(maze)

    # TODO Décommenter pour tester votre code en Partie 2

    test_pos = [-1,0] # changez les valeurs pour tester tous les cas possibles
    valid = validate_move(maze, test_pos)
    print(valid)


    # TODO Décommenter pour tester votre code en Partie 3

    while player_pos != end_pos:
        key_pressed = input("mouvement : ")
        maze, player_pos = move(key_pressed, maze, player_pos)
        print_table(maze)

    print("Vous avez gagnez !")
