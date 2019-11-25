# Projeto Go Fish
### FPRO/MIEIC, 2019/20
### Henrique Ribeiro Nunes up201906852@fe.up.pt
### 1MIEIC07 

#### Objetivo

Criar um clone do jogo [Go Fish](http://www.free80sarcade.com/2600_Go_Fish.php) (Atari 2600) em Pygame

#### Descrição

É um jogo para um jogador, que é um peixe, cujo objetivo é comer todos os peixes de tamanho menor ou igual ao próprio e não ser comido pelos peixes maiores. Cada peixe que se come dá pontos que variam de acordo com o tamanho do peixe. Ao longo do jogo o peixe principal vai aumentando de tamanho e tornando-se capaz de se alimentar de peixes maiores.

#### UI

![UI](https://github.com/Rikenunes8/gofish-atari/blob/master/Environment.png) 

#### Pacotes

- Pygame

#### Tarefas

1. ~**FUNDO**~
   1. ~Ciclo desenhar ceu e mar com diferentes tons~
   1. ~Ondas com [elipses]~(https://www.pygame.org/docs/ref/draw.html)
   1. ~Desenhar platon e sol~
1. **JOGADOR**
   1. ~desenhar o peixe~
   1. ~controlar o peixe com as teclas de cursor~
1. **INIMIGOS / COMIDA**
   1. aleatória inicialmente
      * ~lista de posições~
      * lista de direcções 
   1. colisão
      1. se peixe maior / lula => morre
      1. se peixe menor (igual?) => aumenta 1 ponto de "energia"
      1. quando energia chega a certo ponto, aumentar de tamanho
   1. criar peixes às vezes / destruir peixes quando chegam ao canto do ecrã
1. **ANIMAÇÃO / PONTOS / MENU**

18/11/2019
