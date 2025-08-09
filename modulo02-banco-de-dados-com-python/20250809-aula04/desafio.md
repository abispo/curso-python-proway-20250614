# Desafio 01 - Implementar um sistema de leitura e de alarme

1. Você deve implementar uma classe que representa um sensor de gás. A cada vez que esse sensor é lido, ele gera um valor. Esse valor é lido a partir do método ler(). Esse valor será um valor randômico entre 0 e 100. O valor inicial do sensor será de 0. BONUS: O valor lido não pode estar fora da faixa entre +3 e menos -3 em relação ao valor gerado anteriormente. Exemplo. Se o valor lido anteriormente foi de 60, o novo valor do sensor deve ficar entre 57 e 63. O valor gerado e que será lido pelo sensor não deve ser menor do que 0 nem maior do que 100.

2. Você deve implementar uma classe que irá representar um alarme. Essa classe terá um estado que representa o alarme ligado ou desligado, e 2 métodos: ligar e desligar. Esses métodos irão alterar o valor desse atributo.

O desafio será "ligar" o sensor com o alarme. O alarme terá um valor máximo de leitura do sensor. Caso o valor lido do sensor seja maior que esse valor máximo permitito, o alarme irá disparar. Mesmo com o alarme ligado, ele irá continuar lendo valores do sensor. Caso o valor fique igual ou abaixo do máximo, o alarme irá parar.

Dica de implementação: Esses objetos estarão dentro de um loop, esse valor randômico será gerado nesse loop e passado para o método ler() da classe Sensor. O alarme irá ler o valor do sensor, e fazer a verificação mencionada acima. Utilize a função sleep() do módulo time para definir um intervalo de leitura.
