using Godot;
using Godot.NativeInterop;
using System;

public partial class EnvironmentScript : Node
{
    public WorldEnvironment _worldEnv;
    //public Button _worldEnv;
    public override void _Ready()
    {
        Godot.Environment env = new Godot.Environment();

        // Set the background mode to Color
        env.BackgroundMode = Godot.Environment.BGMode.Color;

        // Change the background color to a new color (e.g., blue)
        env.BackgroundColor = new Color(0, 0, 1); // RGB values range from 0 to 1

        GD.Print(env.BackgroundColor);
        //Get the WorldEnvironment node and set its environment
        Node node = GetNode("/root/Node/WorldEnvironment");
        GD.Print(node.Name);
        //var realmad = GetNode<WorldEnvironment>("/root/Node/WorldEnvironment");
        //GD.Print(realmad);
        //env = GetNode("/root/Node/WorldEnvironment");

        //_worldEnv = GetNode<Button>("/root/Node/Button1");


        //Node node = GetNode("/root/Node/Button1");
        //GD.Print(node.GetType().Name);



        //var worldEnv = 0;
        //GD.Print(_worldEnv);
        //worldEnv.Environment = env;


        // Get the WorldEnvironment node
        WorldEnvironment worldEnv = GetNode<WorldEnvironment>("/root/Node/WorldEnvironment");
        //GD.Print(worldEnv);
        //// Create a new Godot.Environment resource
        //Godot.Environment env = new Godot.Environment();
        //// Set the background mode to Color
        //env.BackgroundMode = Godot.Environment.BGMode.Color;

        //// Change the background color to a new color (e.g., blue)
        //env.BackgroundColor = new Color(0, 0, 1); // RGB values range from 0 to 1

        //// Assign the Environment resource to the WorldEnvironment
        //worldEnv.Environment = env;
    }
}