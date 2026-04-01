using Godot;
using System;

public partial class ButtonCode : Godot.Button
{
    // Called when the node enters the scene tree for the first time.
    private Button _button0;
    private Button _button1;
    private Button _CheckButton0;
    private SpriteCode _sprite;

    public override void _Ready()
    {
        ////this.Connect("pressed", this, "OnPressed");
        _button0 = GetNode<Button>("/root/Node/Button0");
        //_button0 = this as Button;
        _button0.Pressed += OnPressed0;

        _button1 = GetNode<Button>("/root/Node/Button1");
        //_button1 = this as Button;
        _button1.Pressed += OnPressed1;

        _CheckButton0 = GetNode<Button>("/root/Node/CheckButton");

        _sprite = GetNode<SpriteCode>("/root/Node/Sprite");
    }
    void OnPressed0()
    {
        GD.Print("Sprite left");
        //_sprite._PosititonChanger(new Vector2(100, 100));
        //_sprite.RotateByDegrees(45);
        _sprite.Rotation += Mathf.DegToRad(360-45);
    }
    void OnPressed1()
    {
        GD.Print("Sprite right");
        _sprite.Rotation += Mathf.DegToRad(45);
    }

    // Called every frame. 'delta' is the elapsed time since the previous frame.
    public override void _Process(double delta)
    {
    }

}