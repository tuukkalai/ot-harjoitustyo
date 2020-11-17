/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package matopeli;

import javafx.geometry.Pos;
import javafx.scene.Parent;
import javafx.scene.control.Button;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Paint;
import javafx.scene.text.Text;
import javafx.stage.Stage;

/**
 *
 * @author tuukkala
 */
public class Menu {
    private Stage stage;

    public Menu(Stage stage) {
        this.stage = stage;
    }

    public void activate() {
        stage.setWidth(800);
        stage.setHeight(800);
        stage.setResizable(false);
        stage.getScene().setRoot(buildScene());

        stage.setFullScreen(false);
    }

    public Parent buildScene() {
        GridPane pane = new GridPane();
        pane.setVgap(5);
        pane.setAlignment(Pos.CENTER);
        
        Text logo = new Text();
        logo.setRotate(5);
        logo.setScaleX(3);
        logo.setScaleX(2.8);
        logo.setText("Matopeli");
        
        pane.add(logo, 0, 0);

        Button playButton = new Button("Pelaa");
        // Button statsButton = new Button("Tilastot");

        playButton.setOnMouseClicked(e -> new Game(stage).start());
        // statsButton.setOnMouseClicked(e -> new StatisticsScreen(stage).activate());

        pane.add(playButton, 0, 1);
        // pane.add(statsButton, 0, 2);

        return pane;
    }    
}
