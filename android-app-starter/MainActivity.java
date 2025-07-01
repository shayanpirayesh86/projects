```java
package com.example.myapp;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        TextView textView = new TextView(this);
        textView.setText("Welcome to Shayan's Android App");
        textView.setTextSize(24);
        textView.setPadding(16, 16, 16, 16);

        setContentView(textView);
    }
}
