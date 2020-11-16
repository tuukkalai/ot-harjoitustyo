package matopeli.ui;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;

/**
 *
 * @author tuukkala
 */
public class MatopeliUi extends Application {

    /**
     * @param args the command line arguments
     */

    @Override
    public void start(Stage stage) throws Exception {
        stage.setScene(new Scene(new Pane(), 800, 600));
        stage.setTitle("Matopeli");
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
