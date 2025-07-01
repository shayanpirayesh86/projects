# Android App Starter

Basic Android application skeleton in Java displaying a welcome message.

## Technologies
- Java
- Android Studio

## Usage
1. Create a new project in Android Studio.
2. Replace the default `MainActivity.java` with the following code.
3. Run the app on an emulator or device to see the welcome screen.

## MainActivity.java

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
