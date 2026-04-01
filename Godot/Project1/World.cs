using Godot;
using System;
using System.Reflection;

public partial class World : Node2D
{
	PackedScene packedScene;

	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		packedScene = (PackedScene)GD.Load("res://sprite_2d.tscn");
        GD.Print("efejmf");
    }

	public override void _Process(double delta)
	{
		
	}

	bool firstPress = true;
	public override void _UnhandledInput(InputEvent @event)
	{
		//GD.Print(firstPress);
		if (@event is InputEventMouseButton mouseEvent)
		{
			//GD.Print(mouseEvent.ButtonIndex);
			Sprite2D sprite_2d = (Sprite2D)packedScene.Instantiate();
			sprite_2d.Position = mouseEvent.Position;
            if (mouseEvent.ButtonIndex != 0)
            {
                if (mouseEvent.ButtonIndex == MouseButton.Left && firstPress)
                {
                    this.AddChild(sprite_2d);
                    //this.RemoveChild(sprite_2d);
                }
                if (mouseEvent.ButtonIndex == MouseButton.Right && firstPress)
                {
                    //this.RemoveChild(sprite_2d);
                    //var this_child = this.FindChild("sprite_2d");
                    var child_count = this.GetChildCount();
                    //GD.Print(child_count);
                    //var this_child = this.GetChild(child_count-1).Name;
                    if (child_count > 0)
                    {
                        Node child = GetChild(child_count - 1);
                        RemoveChild(child);
                    }
                    else
                    {
                        Label label = new Label();
                        label.Text = "No more childs left";
                        label.Position = mouseEvent.Position;
                        AddChild(label);
                    }

                }
                if (firstPress)
                {
                    firstPress = false;
                }
                else
                {
                    firstPress = true;
                }
            }

        }

    }
}
