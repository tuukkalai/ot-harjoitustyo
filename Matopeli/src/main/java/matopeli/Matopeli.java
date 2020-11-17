package matopeli;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;

/**
 *
 * @author tuukkala
 */
public class Matopeli extends Application {

    /**
     * @param args the command line arguments
     */
    @Override
    public void start(Stage gameStage) {
        gameStage.setTitle("Matopeli");
        
        //gameStage.setWidth(Screen.getPrimary().getVisualBounds().getWidth());
        //gameStage.setHeight(Screen.getPrimary().getVisualBounds().getHeight());
        gameStage.setScene(new Scene(new Pane()));
        gameStage.show();

        new Menu(gameStage).activate();
    }
    
    public static void main(String[] args) {
        launch(args);
    }
}
