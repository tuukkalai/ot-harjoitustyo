package matopeli.domain;

public class Stat {

    private int id;
    private String player;
    private int score;

    public Stat(int id, String player, int score) {
        this.id = id;
        this.player = player;
        this.score = score;
    }

    public Stat(String player, int score) {
        this.player = player;
        this.score = score;
    }

    public int getId() {
        return this.id;
    }

    public String getPlayer() {
        return this.player;
    }

    public int getScore() {
        return this.score;
    }

    public void setId(int id) {
        this.id = id;
    }
}