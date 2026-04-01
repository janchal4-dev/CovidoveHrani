using Godot;
using System;

public partial class Sprite2D : Godot.Sprite2D
{
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		//this.Position = new Vector2(300,200);
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
        //Random rnd = new Random();
        //int rand_num = rnd.Next(0, 3);
        //if (rand_num == 0) //W
        //{
        //	this.Position += new Vector2(0,-1);
        //}
        //if (rand_num == 1)  //S
        //{
        //	this.Position += new Vector2(0,1);
        //}
        //if (rand_num == 2) //A
        //{
        //	this.Position += new Vector2(-1,0);
        //}
        //if (rand_num == 3)
        //{
        //	this.Position += new Vector2(1,0);
        //}
        uint randomNumber = GD.Randi() % 4; // 0 - 3
        float AMOUNT = 5;
        if (randomNumber == 0)
        {
            this.Position += new Vector2(0, -AMOUNT);
        }
        if (randomNumber == 1)
        {
            this.Position += new Vector2(0, AMOUNT);
        }
        if (randomNumber == 2)
        {
            this.Position += new Vector2(-AMOUNT, 0);
        }
        if (randomNumber == 3)
        {
            this.Position += new Vector2(AMOUNT, 0);
        }
    }
}
