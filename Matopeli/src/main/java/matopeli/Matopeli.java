package matopeli;

import java.util.ArrayList;
import javafx.animation.AnimationTimer;
import javafx.application.Application;
import javafx.application.Platform;
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
import javafx.scene.paint.Color;
import javafx.stage.Stage;

/**
 *
 * @author tuukkala
 */
public class Matopeli extends Application {
    
    ArrayList<Snake> snake = new ArrayList<>();
    int speed = 1;
    int tickCall = 0;
    
    int viewWidth = 600;
    int viewHeight = 600;
    int gridCell = viewWidth / 30;
    
    // Starting direction
    String dir = "RIGHT";
    
    public static class Snake {
        int x;
        int y;
        int width;
        int height;
        
        public Snake(int x, int y) {
            this.x = x;
            this.y = y;
            this.width = 15;
            this.height = 15;
        }
    }
    
    @Override
    public void start(Stage stage) {

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

        AnimationTimer animTimer = new AnimationTimer() {
            private long previousTime = 0;
            
            @Override
            public void handle(long currentTime) {
                
                if (previousTime == 0) {
                    previousTime = currentTime;
                    tick(gc);
                    return;
                }

                if (currentTime - previousTime > 100_000_000L / speed) {
                    previousTime = currentTime;
                    tick(gc);
                }
            }
        };
        
        snake.add(new Snake(5 * gridCell, viewHeight / 2));
        snake.add(new Snake(4 * gridCell, viewHeight / 2));
        snake.add(new Snake(3 * gridCell, viewHeight / 2));

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
    
    public void tick(GraphicsContext gc) {
        
        gc.clearRect(0, 0, viewWidth, viewHeight);

        for (int i = snake.size() - 1; i >= 1; i--) {
            snake.get(i).x = snake.get(i - 1).x;
            snake.get(i).y = snake.get(i - 1).y;
        }

        switch (dir) {
            case "RIGHT":
                snake.get(0).x++;
                break;
            case "LEFT":
                snake.get(0).x--;
                break;
            case "UP":
                snake.get(0).y--;
                break;
            case "DOWN":
                snake.get(0).y++;
                break;
        }

        // Game area colors
        gc.setFill(Color.BLACK);
        gc.fillRect(0, 10, viewWidth, viewHeight - 10);

        gc.setFill(Color.WHITE);
        gc.fillRect(5, 15, viewWidth - 10, viewHeight - 20);

        // Snake color
        for (Snake s : snake) {
            gc.setFill(Color.BLACK);
            gc.fillRect(s.x, s.y, s.width, s.height);
        }
    }
    
    private void keyboardSetUp(Scene scene) {
        scene.setOnKeyPressed((KeyEvent e) -> {
            if (e.getCode() == KeyCode.LEFT) {
                dir = "LEFT";
            }

            if (e.getCode() == KeyCode.RIGHT) {
                dir = "RIGHT";
            }

            if (e.getCode() == KeyCode.DOWN) {
                dir = "DOWN";
            }

            if (e.getCode() == KeyCode.UP) {
                dir = "UP";
            }
            System.out.println("Direction : " + dir);
        });

        // Could be needed in multiplayer version if keyboard 
        // keeps track only couple of keystrokes.
        /*
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
        */
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
