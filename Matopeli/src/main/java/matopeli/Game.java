/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package matopeli;

import java.util.ArrayList;
import java.util.HashSet;
import javafx.animation.AnimationTimer;
import javafx.event.EventHandler;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.input.KeyEvent;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;

/**
 *
 * @author tuukkala
 */
public class Game {

    private Stage stage;

    static Scene mainScene;
    static GraphicsContext graphicsContext;
    static int WIDTH = 512;
    static int HEIGHT = 256;

    static HashSet<String> currentlyActiveKeys;

    public Game(Stage stage) {
        this.stage = stage;
    }

    public void start() {
        Group root = new Group();
        Scene theScene = new Scene(root);
        stage.setScene(theScene);

        Canvas canvas = new Canvas(800, 800);
        root.getChildren().add(canvas);

        ArrayList<String> input = new ArrayList<String>();

        theScene.setOnKeyPressed(
                new EventHandler<KeyEvent>() {
            public void handle(KeyEvent e) {
                String code = e.getCode().toString();

                // only add once... prevent duplicates
                if (!input.contains(code)) {
                    input.add(code);
                }
            }
        });

        theScene.setOnKeyReleased(
                new EventHandler<KeyEvent>() {
            public void handle(KeyEvent e) {
                String code = e.getCode().toString();
                input.remove(code);
            }
        });

        GraphicsContext gc = canvas.getGraphicsContext2D();

        Rectangle left = new Rectangle();
        left.setX(20);
        left.setY(20);
        left.setWidth(20);
        left.setHeight(20);

        new AnimationTimer() {
            public void handle(long currentNanoTime) {
                gc.clearRect(0, 0, 800, 800);

                if (input.contains("LEFT")) {
                    gc.fillRect(90, 90, 620, 620);
                } else {
                    gc.fillRect(100, 100, 600, 600);
                }
            }
        }.start();

        stage.show();
    }
}
