package com.example.rnd;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.constraintlayout.widget.ConstraintSet;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Build;
import android.os.Bundle;
import android.transition.TransitionManager;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
public class MainActivity extends AppCompatActivity {

    private static final String SHOW_BIG_IMAGE = "TAG";
    ConstraintSet small = new ConstraintSet();
    ConstraintSet big = new ConstraintSet();
    ConstraintLayout root;
    boolean mShowBigImage;

    @SuppressLint("ClickableViewAccessibility")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        root = findViewById(R.id.big_one);
        small.clone(root);
        big.load(this, R.layout.big_image_layout);
        if (savedInstanceState != null) {
            boolean previous = savedInstanceState.getBoolean(SHOW_BIG_IMAGE);

            if (previous != mShowBigImage) {
                mShowBigImage = previous;
                applyConfig();
            }
        }

        TextView textView = findViewById(R.id.random_text);
        textView.setOnTouchListener(new OnSwipeMotion(this) {
            @RequiresApi(api = Build.VERSION_CODES.KITKAT)
            @Override
            public void onSwipeUp() {
                TransitionManager.beginDelayedTransition(root);
                mShowBigImage = !mShowBigImage;
                applyConfig();
            }

            @RequiresApi(api = Build.VERSION_CODES.KITKAT)
            @Override
            public void onSwipeDown() {
                TransitionManager.beginDelayedTransition(root);
                mShowBigImage = !mShowBigImage;
                applyConfig();
            }
        });

    }

    @Override
    public void onSaveInstanceState(Bundle outState) {
        super.onSaveInstanceState(outState);
        outState.putBoolean(SHOW_BIG_IMAGE, mShowBigImage);
    }

    @RequiresApi(api = Build.VERSION_CODES.KITKAT)
    public void toggleMode(View v) {
        TransitionManager.beginDelayedTransition(root);
        mShowBigImage = !mShowBigImage;
        applyConfig();
    }

    private void applyConfig() {
        if (mShowBigImage) {
            big.applyTo(root);
        } else {
            small.applyTo(root);
        }
    }

}
