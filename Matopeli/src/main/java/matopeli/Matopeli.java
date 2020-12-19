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
import matopeli.ui.Snake;
import matopeli.ui.Apple;

/**
 *
 * @author tuukkala
 */
public class Matopeli extends Application {
    
    ArrayList<Snake> snake = new ArrayList<>();
    ArrayList<String> inputs = new ArrayList<>();
    public int speed = 5;
    public int tickCall = 0;
    public boolean gameOver = false;
    public boolean gamePaused = false;
    
    static int viewWidth = 600;
    static int viewHeight = 600;

    public static int gridCell = viewWidth / 30;
    
    // Starting direction
    String dir = "RIGHT";
    
    public static class GameScene {
        Group root;
        Scene gameScene;
        Canvas canvas;
        GraphicsContext gc;
        
        public GameScene() {
            this.root = new Group();
            this.gameScene = new Scene(root);
            this.canvas = new Canvas(viewWidth, viewHeight);
            this.root.getChildren().add(canvas);
        }
        
        public Scene getGameScene() {
            return this.gameScene;
        }
        
        public GraphicsContext getGraphicsContext() {
            return this.canvas.getGraphicsContext2D();
        }
        
        public void newGame() {
            this.root = new Group();
            this.gameScene = new Scene(root);
            this.canvas = new Canvas(viewWidth, viewHeight);
            this.root.getChildren().add(canvas);
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
        GameScene gameScene = new GameScene();
        
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
                if (previousTime == 1) {
                    // Create new game if previousTime equals 0
                    previousTime = currentTime;
                    tick(gameScene.getGraphicsContext());
                    return;
                }

                if (currentTime - previousTime > 1_000_000_000L / speed) {
                    previousTime = currentTime;
                    tick(gameScene.getGraphicsContext());
                    if(gameScene.getGraphicsContext().getGlobalAlpha() == 6.6){
                        stopTimer(currentTime);
                        stop();                        
                    }
                }
            }
            
            public void stopTimer(long currentTime){
                previousTime = 0;
                stage.setScene(statsScene);
            }
        };
        
        stage.show();

        startBtn.setOnAction(e -> {
            gameScene.newGame();
            
            gameOver = false;
            dir = "RIGHT";
            
            // Render starting snake
            snake.clear();
            snake.add(new Snake(5 * gridCell + 1, viewHeight / 2 + 1));
            snake.add(new Snake(4 * gridCell + 1, viewHeight / 2 + 1));
            snake.add(new Snake(3 * gridCell + 1, viewHeight / 2 + 1));
            
            keyboardSetUp(gameScene.getGameScene());
            stage.setScene(gameScene.getGameScene());
            
            animTimer.start();
        });
        statsBtn.setOnMouseClicked(e -> {
            stage.setScene(statsScene);
        });
        exit.setOnMouseClicked(e -> {
            stage.close();
        });
        backBtn.setOnMouseClicked(e -> {
            stage.setScene(menuScene);
        });
    }
    
    public void tick(GraphicsContext gc) {
        
        if (gamePaused) {
            gc.setGlobalAlpha(3.0);
			gc.setFill(Color.BLACK);
			gc.setFont(new Font("", 20));
			gc.fillText("Tauko", (viewWidth / 2) - 50, (viewHeight / 2) - 10);
			return;
        }
        
        if (gameOver) {
            gc.setGlobalAlpha(6.6);
			gc.setFill(Color.BLACK);
			gc.setFont(new Font("", 20));
			gc.fillText("Peli loppui", (viewWidth / 2) - 50, (viewHeight / 2) - 10);
			return;
		}

        for (int i = snake.size() - 1; i >= 1; i--) {            
            snake.get(i).x = snake.get(i - 1).x;
            snake.get(i).y = snake.get(i - 1).y;
        }

        if(!inputs.isEmpty()){
            dir = inputs.remove(0);
        }

        switch (dir) {
            case "RIGHT":
                snake.get(0).x += gridCell;
                if(snake.get(0).x > (viewWidth - gridCell)){
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
                if(snake.get(0).y < 2 * gridCell){
                    gameOver = true;
                }
                break;
            case "DOWN":
                snake.get(0).y += gridCell;
                if(snake.get(0).y > (viewHeight - gridCell)){
                    gameOver = true;
                }
                break;
        }

        // Game area colors
        gc.setFill(Color.BLACK);
        gc.fillRect(0, gridCell, viewWidth, viewHeight - gridCell);

        gc.setFill(Color.WHITE);
        gc.fillRect(gridCell, 2 * gridCell, viewWidth - 2 * gridCell, viewHeight - 3 * gridCell);

        // Draw snake
        for (Snake s : snake) {
            gc.setFill(Color.BLACK);
            gc.fillRect(s.x, s.y, s.width, s.height);
        }


    }
    
    private void keyboardSetUp(Scene scene) {
        scene.setOnKeyPressed((KeyEvent e) -> {
            if(!gamePaused){
                if (e.getCode() == KeyCode.LEFT) {
                    if (dir != "RIGHT") {
                        inputs.add("LEFT");
                    }
                }

                if (e.getCode() == KeyCode.RIGHT) {
                    if (dir != "LEFT") {
                        inputs.add("RIGHT");
                    }
                }

                if (e.getCode() == KeyCode.DOWN) {
                    if (dir != "UP") {
                        inputs.add("DOWN");
                    }
                }

                if (e.getCode() == KeyCode.UP) {
                    if (dir != "DOWN") {
                        inputs.add("UP");
                    }
                }
            }
            
            if (e.getCode() == KeyCode.SPACE || e.getCode() == KeyCode.ESCAPE) {
                if (gamePaused){
                    gamePaused = false;
                } else {
                    gamePaused = true;
                }
            }
        });
    }

    @Override
    public void stop() {
        Platform.exit();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
