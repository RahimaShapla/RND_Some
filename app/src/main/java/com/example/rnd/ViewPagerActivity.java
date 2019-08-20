package com.example.rnd;

import android.os.Bundle;
import android.view.Menu;
import android.view.View;
import android.view.animation.Animation;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

public class ViewPagerActivity extends AppCompatActivity {
    TextView move,one,two,three;
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_pager);
        Animation transitionLeft, transitionRight;
        move = findViewById(R.id.move);
        one = findViewById(R.id.one);
        two =  findViewById(R.id.two);
        three =  findViewById(R.id.three);

        one.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
               // move.
            }
        });
    }

}
