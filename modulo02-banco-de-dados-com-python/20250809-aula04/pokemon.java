// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class Pokemon
{
    private String nome;
    private String tipo;
    private int saude;
    
    // método construtor
    public Pokemon(String nome, String tipo, int saude) {
        this.nome = nome;
        this.tipo = tipo;
        this.saude = saude;
    }
    
    public int getSaude() {
        return this.saude;
    }
    
    public void setSaude(int saude) {
        this.saude = saude;
    }
}

class Main {
    public static void main(String[] args) {
        Pokemon pikachu = new Pokemon("Pikachu", "Elétrico", 60);
        Pokemon bulbasauro = new Pokemon("Bulbasauro", "Planta", 100);
        
        pikachu.setSaude(50);
        System.out.println(pikachu.getSaude());
    }
}