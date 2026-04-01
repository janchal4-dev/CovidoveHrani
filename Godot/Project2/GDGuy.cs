using Godot;
using System;

public partial class GDGuy : Sprite2D
{
    [Signal]
    public delegate void MovedWithArgumentEventHandler(float newx, float newy);
    //public delegate void Moved(float newx, float newy); // old method won't work
    //You must append "EventHandler()" or "ArgumentWithEventHandler( args...)" 
    //Depending on if you pass arguments

    public override void _Ready()
    {
        Timer timer = this.GetNode<Timer>("Clock");
        timer.WaitTime = 1;
        //timer.Connect("timeout", this, "on_timeout"); //This is the old scripting method
        timer.Timeout += () => on_timeout();
        timer.Start();

        this.MovedWithArgument += on_moved;
    }



    void on_timeout()
    {
        var screen_size = GetWindow().Size;
        var x_size = screen_size[0];
        var y_size = screen_size[1];
        GD.Print(x_size, y_size);
        float randX = (float)GD.RandRange(-(x_size/2-100), +(x_size/2-100));
        float randY = (float)GD.RandRange(-(y_size/2-100), +(y_size/2-100));
        this.Position = new Vector2 (randX, randY);

        //this.EmitSignal("Moved", randX, randY);
        this.EmitSignal("MovedWithArgument", randX, randY);
    }
    void on_moved(float newx, float newy)
    {
        //GD.Print("moved");
        //GD.Print("X: " + newx);
        //GD.Print("Y: " + newy);
    }
}
