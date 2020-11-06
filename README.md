# disease-simulation
In this assignment, we ask you to write a simplified simulator to compute the strength of a disease after it has been planted in a virtual world and the accumulated disease strength of all the diseases in the world.

Descrição Geral do Problema: Ciência da Computação, Engenharia da Computação e Engenharia de Software são campos que contribuı́ram para avanços em outras disciplinas das ciências e engenharia. Programas de computador são usados para modelar e prever o clima, controlar robôs para aplicações de vigilância, prever interações medicamentosas, prever o crescimento do câncer, prever a propagação de uma determinada doença (por exemplo, vı́rus) em todo o mundo etc. Nesta tarefa, solicitamos que você escreva um simulador simplificado para calcular a força de uma doença, depois de ter sido plantada em um mundo virtual, e a força acumulada de todas as doenças neste mundo.

Por simplicidade, assumimos que a doença não pode se mover, mas fica mais forte após cada unidade de tempo (por exemplo, um dia), quando estiver na região do mundo com a temperatura adequada para o seu crescimento. Inicialmente, a força de uma doença vale 1. Após cada unidade de tempo decorrida, sua força é multiplicada pela sua taxa de crescimento para essa faixa de temperatura (por exemplo, 2 para a temperatura entre, digamos, 15 e 25 unidades de temperatura), se a doença estiver localizada na região do mundo com a temperatura média dentro desse intervalo.

O mundo simulado é dividido em quatro regiões iguais e não sobrepostas (quadrantes), e cada quadrante possui a mesma temperatura média. Em cada unidade de tempo, o programa relata a força acumulada de todas as doenças no mundo simulado. Você deve implementar cinco classes, e a Fig. 1 mostra como essas classes estão relacionadas.

Fig. 1: https://drive.google.com/file/d/1xRQEmnHMoauOGy2ow6tC3T6ZRLPBEbmY/view

Figura 1: Diagrama de classes simplificado, onde as classes são mostradas em retângulos. Interfaces são marcadas com o termo << Interf ace >>. As setas sólidas brancas indicam uma única hierarquia de herança (ou a relação de superclasse-subclasse). As setas sólidas pretas indicam interações entre classes. O Simulador chama os métodos da classe MyWorld e da classe Disease. A classe MyWorld e a classe Disease chamam os métodos uma da outra.

A classe MyWorld é uma subclasse da classe World e também implementa os métodos especificados na interface IWorld 5. Na terminologia Python, isso significa que “MyWorld
deriva de World e de IWorld”. A classe Disease é uma subclasse da classe Actor e implementa os métodos especificados na interface IDisease.

O Simulador possui um método principal que instancia primeiro um Objeto MyWorld, que lê um arquivo de configuração “simulation.config”. Ele instancia objetos Disease e adiciona
esses objetos a locais diferentes no objeto MyWorld. Ele define a temperatura em cada quadrante do seu mundo.

O Simulador entra em loop, chamando o método act() do objeto MyWorld, para relatar a força acumulada das doenças em todo o mundo nessa unidade de tempo e chamando o método act() de cada objeto Disease para calcular a nova força da doença após o término da unidade de tempo.

O Simulador também instancia um objeto World e adiciona dois objetos Actor neste mundo. Em seguida, ele executa uma simulação semelhante. Você pode ver a diferença nos resultados da simulação entre o uso de objetos MyWorld e World. Em seguida, vamos descrever os detalhes de cada classe.
________________________________________________

Para esclarecimentos completos, ler os arquivos AD1-PIG.pdf e AD2-PIG.pdf (essa última com uso de Tkinter, para criação do ambiente gráfico).
