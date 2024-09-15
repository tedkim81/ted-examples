# Launch Mode Tester

This project is an Android application designed to help users understand and test the different launch modes available in Android applications.

## Purpose

The Launch Mode Tester app allows you to observe how various launch modes behave when applied to activities in an Android app. Launch modes control how activities are launched, either through configuration in the `AndroidManifest.xml` or dynamically through an `Intent`.

## Features

- Launch Modes can be set both in the `AndroidManifest.xml` and dynamically through `Intent`.
- The app provides buttons to choose activities declared in the `AndroidManifest.xml` with specific launch modes.
- Checkboxes allow users to specify which launch mode to apply when starting an activity via `Intent`.

## Usage

1. Use the **buttons** on the screen to select an activity defined in the `AndroidManifest.xml` with a particular launch mode.
2. Use the **checkboxes** to dynamically set the launch mode that will be applied via `Intent` when launching the activity.
3. To view the status of tasks and activities in the system, execute one of the following `adb` commands in your terminal:
   - `adb shell dumpsys activity recents`
   - `adb shell dumpsys activity activities`
   - `adb shell dumpsys activity activities | grep -i Hist`
   - These commands will allow you to observe how tasks and activities are managed under different launch modes.

## Launch Modes in Android

Launch modes can be specified in two ways:

- **Statically**, by declaring the `launchMode` attribute in the `<Activity>` element of the `AndroidManifest.xml`.
- **Dynamically**, by specifying the launch mode when creating an `Intent`.