/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package matopeli.ui;

import static matopeli.Matopeli.gridCell;

/**
 *
 * @author tuukkala
 */
public class CellContent {
    public int x;
    public int y;
    public int width;
    public int height;

    public CellContent(int x, int y) {
        this.x = x;
        this.y = y;
        this.width = gridCell - 2;
        this.height = gridCell - 2;
    }
    
    public int getX() {
        return this.x;
    }
    
    public int getY() {
        return this.y;
    }
}
