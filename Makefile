##
## RENO PROJECT, 2025
## diduenjoy
## File description:
## Makefile
##

NAME	=	diduenjoy

SRC		=	main.py

all: $(NAME)

$(NAME):
	cp $(SRC) $(NAME)
	chmod +x $(NAME)

fclean:
	rm -f $(NAME)
	rm -rf src/parsing/__pycache__

re: fclean all

.PHONY:	re fclean all