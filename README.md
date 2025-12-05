# 🎛 Zura’s HackPad  
A fully custom macropad built for my Linux workflow: 4 hotkeys, a rotary encoder with a push switch, RGB underglow, and a 0.91" I²C OLED display — all powered by a Seeed XIAO RP2040.  
Designed, modeled, and PCB-routed as a Hack Club *Blueprint* submission.

---

## ✨ Features

### 🧷 4 Custom Macro Keys
| Key | Name | Behavior |
|-----|------|----------|
| **CP** | Smart Copy/Paste | First press → copy; second press → paste; if nothing is selected, paste directly. |
| **FC** | Folder Create | Instantly creates a new folder in the currently highlighted directory. |
| **OT** | Open Terminal | Opens a terminal window in the current file explorer folder. |
| **LFN** | Fn Lock | Toggles laptop F1–F12 keys to work without holding Fn (software-based toggle). |

### 🎚 Rotary Encoder (With Push Switch)
- Rotate: Volume up/down (or Brightness, Media, Scroll depending on mode).  
- Press: Cycle between modes (Volume → Brightness → Media → Custom).

### 🖥 OLED Display
- Shows whether something is currently copied (CP state).  
- Displays Volume, Brightness, Battery %, and Time.  
- Overheat / high-temperature warning indicator.  
- Optional animations or mode indicators.

### 🌈 RGB Underglow
- 2× SK6812 MINI addressable LEDs  
- Mode colors, warning colors, and idle glow effects.

### 🧩 Fully 3D-Printed Enclosure
- Top plate with switch cutouts  
- Encoder hole  
- OLED window  
- Rear USB-C tunnel  
- Bottom shell with heat-set inserts  
- Smooth fillets for comfort and a clean look

---

## 🧱 Bill of Materials (BOM)

| # | Component | Qty | Notes |
|---|-----------|-----|-------|
| 1 | Seeed XIAO RP2040 (TH) | 1 | Main MCU, USB-C |
| 2 | MX Mechanical Switches | 4 | Any Cherry MX-compatible |
| 3 | EC11 Rotary Encoder w/ Switch | 1 | A/B/C + S1/S2 pins |
| 4 | SK6812 MINI LEDs | 2 | DIN → DOUT chained |
| 5 | 0.91" I²C OLED Display | 1 | Pins: GND / VCC / SCL / SDA |
| 6 | 4-pin Female Header | 1 | For OLED mounting |
| 7 | Keycaps | 4 | MX-compatible |
| 8 | M3 screws + heat-set inserts | 4 | For case assembly |
| 9 | Custom 2-layer PCB | 1 | ≤100×100 mm |

----

## System Layout

**XIAO RP2040 → Components (from KiCad)**

- **SW1 (CP key)** → GPIO26 / A0  
- **SW2 (FC key)** → GPIO27 / A1  
- **SW3 (OT key)** → GPIO28 / A2  
- **SW4 (LFN key)** → GPIO29 / A3  

- **Rotary Encoder**
  - A → GPIO2 / SCK  
  - B → GPIO4 / MISO  
  - C → GND  

- **RGB LEDs (SK6812 MINI)**
  - XIAO GPIO0 / TX → D1 DIN  
  - D1 DOUT → D2 DIN  
  - VDD of D1 & D2 → +5 V (VBUS)  
  - VSS of D1 & D2 → GND  

- **0.91" I²C OLED Header (J1)**
  - Pin 1 → GND  
  - Pin 2 → 3V3  
  - Pin 3 → SCL (GPIO7)  
  - Pin 4 → SDA (GPIO6)

---

## 🗂 Project Structure

zuras-hackpad/
├── CAD/
│   └── ZuraHackPad.step
├── PCB/
│   ├── zuras-hackpad.kicad_pro
│   ├── zuras-hackpad.kicad_sch
│   └── zuras-hackpad.kicad_pcb
├── Firmware/
│   └── main.py
└── README.md

---

## 📸 Required Screenshots (for submission)

## 🖼 Project Images

### 🔹 Top View  
![HackPad Top](Images/Top.png)

### 🔹 Bottom View  
![HackPad Bottom](Images/Bottom.png)

### 🔹 Full 3D Model  
![HackPad Full Model](Images/Full.png)

### 🔹 PCB – Front Side  
![HackPad PCB Front](Images/PDC-Front.png)

### 🔹 PCB – Back Side  
![HackPad PCB Back](Images/PDC-Back.png)

### 🔹 PCB – Final Routing View  
![HackPad PCB Final](Images/PDC-Finish.png)

### 🔹 Schematic  
![HackPad Schematic](Images/Schematic.png)

### 🔹 Debug Screenshot  
![HackPad Debug](Images/Debug.png)

---

## 🔌 Firmware (KMK / CircuitPython)

Firmware responsibilities:

- Scan 4 switches  
- Read rotary encoder A/B/SW  
- Display info on OLED (copy state, system values, warnings)  
- Drive SK6812 LEDs  
- Send OS-level keycodes or macros  
- Implement Fn-lock behavior  
- Open terminal / create folders through macro sequences

Stored in:

Firmware/main.py

- Copy CircuitPython UF2 onto the board
- Drag the `KMK` folder + `boot.py` (from KMK) onto the USB drive
- Copy `main.py` from this folder onto the drive
- Press reset – the macropad should start working

---

## 🏗 Build Steps

### 1. PCB
- Export Gerbers from KiCad  
- Order 2-layer ≤100×100 mm board

### 2. Case
- Export STEP as STL  
- 3D-print top + bottom shells  
- Insert heat-sets  
- Fit OLED + encoder + switches  

### 3. Assembly
- Solder MCU, switches, RGB LEDs, OLED header  
- Screw enclosure together  
- Flash CircuitPython → drag KMK → place main.py  

---

## 🚀 Submission Checklist

- [x] PCB ≤100 mm × 100 mm  
- [x] 2-layer PCB  
- [x] XIAO RP2040 (TH)  
- [x] ≤16 inputs  
- [x] Only approved components  
- [x] 3D printed case  
- [x] Complete STEP model  
- [x] Schematic + PCB + Firmware added  
- [x] README finished  
- [x] Submitted via Hack Club Dashboard  

---

## 🧾 License
MIT recommended.

---

## 🙌 Credits
Made by: Zura (LordZura)  
Powered by: KiCad, Onshape, Seeed XIAO RP2040, KMK, Hack Club Blueprint
