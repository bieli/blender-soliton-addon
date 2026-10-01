# Soliton Wave Generator

A Blender add-on that generates and animates a mathematical soliton wave (based on the Korteweg-de Vries equation) on a dense mesh grid. 

## Features
* **Custom Mesh Generation:** One-click generation of a subdivided grid optimized for wave propagation.
* **Real-time Animation:** Automatically calculates vertex displacements on the Z-axis based on the current frame.
* **Interactive UI:** Control the wave's Amplitude, Velocity, and Width directly from the 3D Viewport sidebar.

## Installation

1. Download the `blender_soliton.py` script to your computer.
2. Open Blender (version 3.0 or later recommended).
3. Go to the top menu and select **Edit > Preferences**.
4. Switch to the **Add-ons** tab on the left.
5. Click the **Install...** button in the top right corner.
6. Navigate to the folder where you saved `blender_soliton.py`, select the file, and click **Install Add-on**.
7. In the add-ons list, search for "Soliton" and check the box next to **Add Mesh: Soliton Wave Generator** to enable it.

## How to Use

1. Open the **3D Viewport** in Blender.
2. Press `N` on your keyboard to open the Sidebar (N-Panel).
3. Click on the new **Soliton** tab on the right side of the screen.
4. Click the **Add Soliton Grid** button to spawn the base mesh (`Soliton_Grid`).
5. Press the **Spacebar** to play the timeline animation. You will see the wave start moving along the X-axis.
6. Adjust the **Amplitude**, **Velocity**, and **Width** sliders in the panel to see the wave change in real-time.

## Running Unit Tests (For Developers)

The mathematical logic is separated from the Blender API to allow standalone testing. 

To run the tests outside of Blender using a standard Python environment:
```bash
python test_soliton.py
```

To run tests that require the bpy module, use Blender's headless mode:
```bash
blender --background --python test_soliton.py
```
