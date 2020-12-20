
package matopeli.dao;

import java.io.File;
import java.io.FileWriter;
import java.util.List;
import org.junit.After;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;
import org.junit.Rule;
import org.junit.rules.TemporaryFolder;
import matopeli.domain.Stat;

public class FileStatsDaoTest {
    @Rule
    public TemporaryFolder testFolder = new TemporaryFolder();
    
    File statsFile;
    FileStatsDao dao;
    
    @Before
    public void setUp() throws Exception {
        statsFile = testFolder.newFile("testfile_scores.txt");
        dao = new FileStatsDao(statsFile.getAbsolutePath());
        dao.create(new Stat("pelaaja", 100));

        try (FileWriter file = new FileWriter(statsFile.getAbsolutePath())) {
            file.write("1;pelaaja;100\n");
        }
    }
   
    @Test
    public void statsAreReadCorrectlyFromFile() {
        List<Stat> todos = dao.getAll();
        assertEquals(1, todos.size());
    }

    @After
    public void tearDown() {
        statsFile.delete();
    }
    
}
