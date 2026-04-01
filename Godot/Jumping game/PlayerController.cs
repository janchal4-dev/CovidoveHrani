using Godot;
using System;

public class PlayerController : KinematicBody2D
{
    // Declare member variables here. Examples:
    // private int a = 2;
    // private string b = "text";

    // Called when the node enters the scene tree for the first time.

    public Timer _fallingTimer;
    public Vector2 _velocity;
    public int _moveSize;
    public bool _randValue = false;
    public Timer _jumpingTimer;
    public bool _spacePressed = false;
    public int _count = 0;
    public override void _Ready()
    {
        _fallingTimer= GetNode<Timer>("/root/Node2D/Timer");
        // Set the wait time to 3 seconds (20 times per minute)
        _fallingTimer.WaitTime = 0.0000000005f;
        // Start the Timer
        //_timer.Start();
        //Connect the timeout signal to the OnTimerTimeout method
        _fallingTimer.Connect("timeout", this, nameof(FallTimerOnTimerTimeout));

        _jumpingTimer = GetNode<Timer>("/root/Node2D/Timer2");
        _jumpingTimer.WaitTime = 0.0000000005f;
        _jumpingTimer.Connect("timeout", this, nameof(JumpTimerOnTimerTimeout));
    }

    //  // Called every frame. 'delta' is the elapsed time since the previous frame.
    public override void _Process(float delta)
    {
        _velocity = new Vector2();
        _moveSize = 200;
        
        //GD.Print("ehffieh");
        //Vector2 velocity = new Vector2();
        //int moveSize = 100;

        if (Input.IsActionPressed("ui_space") && _spacePressed == false || Input.IsActionPressed("ui_s"))
        {
            _fallingTimer.Stop();
            //GD.Print("touched");
            if (Input.IsActionJustPressed("ui_space") && _spacePressed == false )
            {
                GD.Print("up");
                //_velocity.y -= _moveSize;
                //_randValue = true;
                _jumpingTimer.Start();
                _count = 0;
                //_spacePressed = true;

            }
            if (Input.IsActionPressed("ui_s"))
            {
                //GD.Print("down");
                _velocity.y += _moveSize;
            }
            if (Input.IsActionPressed("ui_a"))
            {
                //GD.Print("left");
                _velocity.x -= _moveSize;
            }
            if (Input.IsActionPressed("ui_d"))
            {
                //GD.Print("right");
                _velocity.x += _moveSize;
            }


            //GD.Print(_randValue);

        }
        else
        {
            _spacePressed = false;
            if (Input.IsActionPressed("ui_a"))
            {
                //GD.Print("left");
                _velocity.x -= _moveSize;
            }
            if (Input.IsActionPressed("ui_d"))
            {
                //GD.Print("right");
                _velocity.x += _moveSize;
            }



            //GD.Print("not touched");
            //// Start the Timer
            _jumpingTimer.Stop();
            _fallingTimer.Start();
            //velocity.y += moveSize;

            //// Connect the timeout signal to the OnTimerTimeout method


            //// Connect the timeout signal to the OnTimerTimeout method
            //if (!_timer.IsConnected("timeout", this, nameof(OnTimerTimeout)))
            //{
            //    GD.Print("fnhek");
            //    _timer.Connect("timeout", this, nameof(OnTimerTimeout));
            //}

            //void OnTimerTimeout()
            //{
            //    // Function to be called every 3 seconds
            //    GD.Print("Timer timeout, function called.");
            //    PerformFunction();

            //}
            //void PerformFunction()
            //{
            //    velocity.x -= moveSize;
            //}
            //_timer = GetNode<Timer>("/root/Node2D/Timer");

            //// Set the wait time to 3 seconds (20 times per minute)
            //_timer.WaitTime = 1.0f;

            // Start the Timer
            //_timer.Start();
            //_timer.Connect("timeout", this, nameof(OnTimerTimeout));
            //OnTimerTimeout();
        }
        MoveAndSlide(_velocity);
    }

    private void FallTimerOnTimerTimeout()
    {
        // Function to be called every 3 seconds
        //GD.Print("Timer timeout, function called.");
        _velocity.y += 2*300;
        MoveAndSlide(_velocity);
    }
    private void JumpTimerOnTimerTimeout()
    {
        // Function to be called every 3 seconds
        //GD.Print("Timer");
        if (_count < 18)
        {
            _velocity.y -= 2 * 300;
            MoveAndSlide(_velocity);
        }
        else
        {
            _velocity.y += 2 * 300;
            MoveAndSlide(_velocity);
        }
        _count++;        
    }
}