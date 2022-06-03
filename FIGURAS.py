
WINDOW.fill(BLACK)

#Linha
startX = 0; startY = 270; endX=WIDTH; endY = 150; width = 5
pygame.draw.line(WINDOW, WHITE, (startX, startY), (endX, endY))


#Retangulo preenchido
X = 100; Y = 120; width=50; height = 30
pygame.draw.rect(WINDOW, WHITE, (X, Y, width, height))


#Retangulo vazio
X=250; Y=240; width=50; height = 30; linewidth = 3
pygame.draw.rect(WINDOW, WHITE, (X, Y, width, height), linewidth)    

#Quadrado Cheio
X = 300; Y=80; width=50;height=50
pygame.draw.rect(WINDOW, WHITE, (X,Y,width, height))

#Circulo cheio
X = 200; Y = 150; radius = 20
pygame.draw.circle(WINDOW, WHITE, (X,Y), radius)

#Circulo Aberto
X = 200; Y = 300; radius = 20; width = 3
pygame.draw.circle(WINDOW, WHITE, (X,Y), radius, width)

#Elipse Cheia
X = 350; Y = 260; width = 60; height = 40
pygame.draw.ellipse(WINDOW, WHITE, (X,Y, width, height))

#Arco mas eliptico
X=100;Y=260; width = 60; height = 40; startAngle=0; endAngle=math.pi/2; linewidth = 5
pygame.draw.arc(WINDOW, WHITE, (X,Y,width,height),startAngle,endAngle,linewidth)

#Triangulo Aberto
X1 = 200; Y1 = 100; X2 = 120; Y2 = 120; X3 = 280; Y3 = 180; width = 5
pygame.draw.polygon(WINDOW, WHITE, [[X1,Y1],[X2,Y2], [X3,Y3]], width)

pygame.display.update()
