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
import javafx.scene.text.Font;
import javafx.stage.Stage;

/**
 *
 * @author tuukkala
 */
public class Matopeli extends Application {
    
    ArrayList<Snake> snake = new ArrayList<>();
    public int speed = 5;
    public int tickCall = 0;
    public boolean gameOver = false;
    
    static int viewWidth = 600;
    static int viewHeight = 600;

    public static int gridCell = viewWidth / 30;
    
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
            this.width = gridCell - 2;
            this.height = gridCell - 2;
        }
    }
    
    @Override
    public void start(Stage stage) {

        // Menu set-up
        stage.setTitle("Matopeli");
        GridPane menuGrid = new GridPane();

        // Start screen "logo"
        Label logo = new Label();
        logo.setText("Matopeli");
        menuGrid.addColumn(0, logo);
        menuGrid.setAlignment(Pos.CENTER);
        menuGrid.setGridLinesVisible(false);

        // Start screen start game button
        // Button actions added at the bottom
        Button startBtn = new Button();
        startBtn.setText("Uusi peli");
        menuGrid.addColumn(0, startBtn);
        

        // Game scene set-up
        Group root = new Group();
        Scene gameScene = new Scene(root);
        Canvas canvas = new Canvas(viewWidth, viewHeight);
        root.getChildren().add(canvas);
        GraphicsContext gc = canvas.getGraphicsContext2D();
        
        // To the stats page
        Button statsBtn = new Button();
        statsBtn.setText("Tilastot");
        menuGrid.addColumn(0, statsBtn);
        
        // Stats scene set-up
        GridPane statsGrid = new GridPane();        
        Label statsLogo = new Label();
        statsLogo.setText("Tilastot");
        statsGrid.add(statsLogo, 0, 0);
        statsGrid.setAlignment(Pos.CENTER);
        
        // Table of statistics
        
        Button backBtn = new Button();
        backBtn.setText("Takaisin päävalikkoon");
        statsGrid.add(backBtn, 0, 1);
        statsGrid.setGridLinesVisible(false);
        statsGrid.setHgap(10);
        statsGrid.setVgap(10);
        
        Scene statsScene = new Scene(statsGrid, viewWidth, viewHeight);
        

        // Exit the game
        Button exit = new Button();
        exit.setText("Poistu");
        menuGrid.addColumn(0, exit);

        menuGrid.setHgap(10);
        menuGrid.setVgap(10);

        Scene menuScene = new Scene(menuGrid, viewWidth, viewHeight);
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

                if (currentTime - previousTime > 1_000_000_000L / speed) {
                    previousTime = currentTime;
                    tick(gc);
                    if(gc.getGlobalAlpha() == 6.6){
                        stopTimer(currentTime);
                        stop();
                    }
                }
            }
            
            public void stopTimer(long currentTime){
                System.out.println("Stop called / Game ended");
                stage.setScene(statsScene);
            }
        };
        
        // Render starting snake
        snake.add(new Snake(5 * gridCell + 1, viewHeight / 2 + 1));
        snake.add(new Snake(4 * gridCell + 1, viewHeight / 2 + 1));
        snake.add(new Snake(3 * gridCell + 1, viewHeight / 2 + 1));
        
        stage.show();

        startBtn.setOnAction(e -> {
            System.out.println("Play btn clicked");
            
            keyboardSetUp(gameScene);
            stage.setScene(gameScene);
            
            animTimer.start();
        });
        statsBtn.setOnMouseClicked(e -> {
            System.out.println("Stats btn clicked");
            stage.setScene(statsScene);
        });
        exit.setOnMouseClicked(e -> {
            System.out.println("Exit btn clicked");
            stage.close();
        });
        backBtn.setOnMouseClicked(e -> {
            System.out.println("Back to main menu btn clicked");
            stage.setScene(menuScene);
        });
        
    }
    
    public void tick(GraphicsContext gc) {
        
        //gc.clearRect(0, gridCell, viewWidth, viewHeight-gridCell);
        
        if (gameOver) {
            gc.setGlobalAlpha(6.6);
			gc.setFill(Color.BLACK);
			gc.setFont(new Font("", 20));
			gc.fillText("Peli loppui", (viewWidth/2)-50, (viewHeight/2)-10);
			return;
		}

        for (int i = snake.size() - 1; i >= 1; i--) {            
            snake.get(i).x = snake.get(i - 1).x;
            snake.get(i).y = snake.get(i - 1).y;
        }

        switch (dir) {
            case "RIGHT":
                snake.get(0).x += gridCell;
                if(snake.get(0).x > (viewWidth-gridCell)){
                    gameOver = true;
                }
                break;
            case "LEFT":
                snake.get(0).x -= gridCell;
                if(snake.get(0).x < gridCell){
                    gameOver = true;
                }
                break;
            case "UP":
                snake.get(0).y -= gridCell;
                if(snake.get(0).y < 2*gridCell){
                    gameOver = true;
                }
                break;
            case "DOWN":
                snake.get(0).y += gridCell;
                if(snake.get(0).x > (viewHeight-gridCell)){
                    gameOver = true;
                }
                break;
        }

        // Game area colors
        gc.setFill(Color.BLACK);
        gc.fillRect(0, gridCell, viewWidth, viewHeight - gridCell);

        gc.setFill(Color.WHITE);
        gc.fillRect(gridCell, 2*gridCell, viewWidth - 2*gridCell, viewHeight - 3*gridCell);

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
            //System.out.println("Direction : " + dir);
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
