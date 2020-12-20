package matopeli.dao;

import java.io.FileWriter;
import java.io.File;
import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

import matopeli.domain.Stat;

public class FileStatsDao {
    public List<Stat> stats;
    private String file;

    public FileStatsDao(String file) throws Exception {
        stats = new ArrayList<>(); 
        this.file = file;
        try {
            Scanner reader = new Scanner(new File(file));
            while (reader.hasNextLine()) {
                String[] cols = reader.nextLine().split(";");
                int id = Integer.parseInt(cols[0]);
                String player = cols[1];
                int score = Integer.parseInt(cols[2]);
                Stat stat = new Stat(id, player, score);
                stats.add(stat);
            }
        } catch (Exception e) {
            FileWriter writer = new FileWriter(new File(file));
            writer.close();
        }
    }
    
    private void save() throws Exception{
        try (FileWriter writer = new FileWriter(new File(file))) {
            for (Stat stat : stats) {
                writer.write(stat.getId() + ";" + stat.getPlayer() + ";" + stat.getScore() + "\n");
            }
        }
    }    
    
    private int generateId() {
        return stats.size() + 1;
    }
    
    public List<Stat> getAll() {
        return stats;
    }

    public Stat create(Stat stat) throws Exception {
        stat.setId(generateId());
        stats.add(stat);
        save();
        return stat;
    }
}