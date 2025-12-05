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

---

## 🧬 System Layout

### Pin Usage Summary

**XIAO RP2040 → Components**

- **SDA (GPIO6)** → OLED SDA  
- **SCL (GPIO7)** → OLED SCL  
- **GPIO0** → Encoder A  
- **GPIO1** → Encoder B  
- **GPIO29 (A3)** → Encoder Switch  
- **GPIO2** → SK6812 DIN  
- **GND** → All component grounds  
- **3V3** → OLED & SK6812 VDD

**LEDs:**
- LED1 DIN ← XIAO GPIO2  
- LED1 DOUT → LED2 DIN

**Switches (4× SW_Push):**
- Each switch → 1 GPIO pin (A0, A1, A2, A3 etc.)  
- Other side → GND

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

![HackPad top part](Images/Top.png)
![HackPad bottom part](images/Bottom.png)
![HackPad full model](images/Full.png)
![HackPad PCB](images/PCB.png)
![HackPad schematic](images/SCH.png)

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
