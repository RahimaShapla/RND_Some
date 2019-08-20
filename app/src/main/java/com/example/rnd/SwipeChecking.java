package com.example.rnd;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

public class SwipeChecking extends AppCompatActivity {
    @SuppressLint("ClickableViewAccessibility")
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.swipe_checking);
        TextView textView = findViewById(R.id.text);


        textView.setOnTouchListener(new OnSwipeMotion(this){
            @Override
            public void onSwipeUp() {
                Toast.makeText(SwipeChecking.this, "up", Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onSwipeDown() {
                Toast.makeText(SwipeChecking.this, "down", Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onSwipeRight() {
               // super.onSwipeRight();
                Toast.makeText(SwipeChecking.this, "Right", Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onSwipeLeft() {
               // super.onSwipeLeft();
                Toast.makeText(SwipeChecking.this, "left", Toast.LENGTH_SHORT).show();
            }


        });
    }
}
