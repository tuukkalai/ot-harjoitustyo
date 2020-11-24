package matopeli;

import java.util.ArrayList;
import javafx.animation.AnimationTimer;
import javafx.application.Application;
import javafx.application.Platform;
import javafx.event.EventHandler;
import javafx.geometry.Pos;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.GridPane;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;

/**
 *
 * @author tuukkala
 */
public class Matopeli extends Application {

    @Override
    public void start(Stage stage) {

        int viewWidth = 600;
        int viewHeight = 600;
       

        // Menu set-up
        stage.setTitle("Matopeli");
        GridPane grid = new GridPane();

        // Start screen logo
        Label logo = new Label();
        logo.setText("Matopeli");
        grid.addColumn(0, logo);
        grid.setAlignment(Pos.CENTER);
        grid.setGridLinesVisible(false);

        // Start screen start game button
        // Button actions added to the bottom
        Button start = new Button();
        start.setText("Uusi peli");
        grid.addColumn(0, start);
        

        // Game scene set-up
        Group root = new Group();
        Scene gameScene = new Scene(root);
        Canvas canvas = new Canvas(viewWidth, viewHeight);
        root.getChildren().add(canvas);
        GraphicsContext gc = canvas.getGraphicsContext2D();
        
        // list of inputs
        ArrayList<String> inputs = new ArrayList<>();
        
        
        // To the stats page
        Button stats = new Button();
        stats.setText("Tilastot");
        grid.addColumn(0, stats);

        // Exit the game
        Button exit = new Button();
        exit.setText("Poistu");
        grid.addColumn(0, exit);

        grid.setHgap(10);
        grid.setVgap(10);

        Scene menuScene = new Scene(grid, viewWidth, viewHeight);
        stage.setScene(menuScene);

        // Ticker
        AnimationTimer animTimer = new AnimationTimer() {

            private final long startTime = System.nanoTime();
            private long previousTime = System.nanoTime();
            
            @Override
            public void handle(long currentTime) {
                gc.clearRect(0, 0, viewWidth, viewHeight);
                
                if (currentTime - previousTime > 1_000_000_000L){
                    previousTime = currentTime;
                    System.out.println("currentTime " + currentTime);
                    
                }
            }
        };

        stage.show();

        start.setOnAction(e -> {
            System.out.println("Play btn clicked");
            
            keyboardSetUp(gameScene);
            
            stage.setScene(gameScene);
            animTimer.start();
        });
        stats.setOnMouseClicked(e -> {
            System.out.println("Stats btn clicked");
        });
        exit.setOnMouseClicked(e -> {
            System.out.println("Exit btn clicked");
            stage.close();
        });
    }

    private void keyboardSetUp(Scene scene) {
        scene.setOnKeyPressed((KeyEvent e) -> {
            if (e.getCode() == KeyCode.LEFT) {
                System.out.println("LEFT pressed");
            }

            if (e.getCode() == KeyCode.RIGHT) {
                System.out.println("RIGHT pressed");
            }

            if (e.getCode() == KeyCode.DOWN) {
                System.out.println("DOWN pressed");
            }

            if (e.getCode() == KeyCode.UP) {
                System.out.println("UP pressed");
            }
        });

        scene.setOnKeyReleased((KeyEvent e) -> {
            if (e.getCode() == KeyCode.LEFT) {
                System.out.println("LEFT released");
            }

            if (e.getCode() == KeyCode.RIGHT) {
                System.out.println("RIGHT released");
            }

            if (e.getCode() == KeyCode.DOWN) {
                System.out.println("DOWN released");
            }

            if (e.getCode() == KeyCode.UP) {
                System.out.println("UP released");
            }
        });
    }

    @Override
    public void stop() {
        System.out.println("sovellus sulkeutuu");
        Platform.exit();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
