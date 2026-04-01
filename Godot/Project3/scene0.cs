using Godot;
using System;

public partial class scene0 : Node2D
{
    PackedScene spriteScene = (PackedScene)GD.Load("res://scene0.tscn");
    //private Sprite2D _sprite;
    //private Button _button0;
    private Button _button1;

  

    // Called when the node enters the scene tree for the first time.
    public override void _Ready()
	{
        _button1 = GetNode<Button>("/root/Node/Button1");
        //_button1.Position = new Vector2(100, 100);

        //PrintTree();
        _ChangeBackColor();

    }

    // Called every frame. 'delta' is the elapsed time since the previous frame.
    public override void _Process(double delta)
	{
	}


    //public void _ChangeBackColor()
    //{
    //    Viewport viewport = GetViewport();
    //    viewport.ClearColor = Colors.Blue;
    //    GD.Print(viewport);
    //}

    //private void PrintTree()
    //{
    //    PrintNodeTree(this);
    //}

    //private void PrintNodeTree(Node node, string prefix = "")
    //{
    //    GD.Print(prefix + node.Name + " (" + node.GetType().Name + ")");
    //    foreach (Node child in node.GetChildren())
    //    {
    //        PrintNodeTree(child, prefix + "  ");
    //    }
    //}



    //public void _ChangeBackColor()
    //{
    //    // Ensure the node path matches your scene's structure
    //    Node node = GetNode("WorldEnvironment");

    //    if (node == null)
    //    {
    //        GD.PrintErr("WorldEnvironment node not found!");
    //        return;
    //    }

    //    GD.Print("Found node: " + node.Name + " of type " + node.GetType().Name);

    //    // Check if the node is of the correct type
    //    if (node is WorldEnvironment worldEnv)
    //    {
    //        // Create a new Godot.Environment resource
    //        Godot.Environment env = new Godot.Environment();

    //        // Set the background mode to Color
    //        env.BackgroundMode = Godot.Environment.BGMode.Color;

    //        // Change the background color to a new color (e.g., blue)
    //        env.BackgroundColor = new Color(0, 0, 1); // RGB values range from 0 to 1

    //        // Assign the Environment resource to the WorldEnvironment
    //        worldEnv.Environment = env;
    //    }
    //    else
    //    {
    //        GD.PrintErr("Node is not of type WorldEnvironment. It is of type " + node.GetType().Name);
    //    }
    //}



    public void _ChangeBackColor()
    {
        // Ensure the node path matches your scene's structure
        Node node = GetNode("WorldEnvironment");

        if (node == null)
        {
            GD.PrintErr("WorldEnvironment node not found!");
            return;
        }

        GD.Print("Found node: " + node.Name + " of type " + node.GetType().Name);

        // Check if the node is of the correct type
        if (node is WorldEnvironment worldEnv)
        {
            // Create a new Godot.Environment resource
            Godot.Environment env = new Godot.Environment();

            // Set the background mode to Color
            env.BackgroundMode = Godot.Environment.BGMode.Color;

            // Change the background color to a new color (e.g., blue)
            env.BackgroundColor = new Color(0, 0, 1); // RGB values range from 0 to 1

            // Assign the Environment resource to the WorldEnvironment
            worldEnv.Environment = env;

            GD.Print("Background color changed to blue.");
        }
        else
        {
            GD.PrintErr("Node is not of type WorldEnvironment. It is of type " + node.GetType().Name);
        }
    }






}
