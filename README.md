# QuadMotorHAT

When I was making my WRO robot, I faced problems interfacing multiple motors with easy wiring to my Raspberry Pi, and I wanted to use a single board. While there are many HATs available, I decided to build my own to keep it as simple as possible with effortless control.

## Features

* **4 Motor Control:** Simple control using the included Python library.
* **Screw Terminals:** Reliable screw terminals for secure motor and power connections.
* **Compact Design:** Low profile design that leaves enough clearance to mount a cooling fan on your Pi.

---

## Instructions

### 1. Setup

### Ensure gpiozero is installed:

```bash
pip install gpiozero
```

Place `quadmotorhat.py` inside your project directory alongside your main script:

```text
your_project/
├── quadmotorhat.py
└── main.py
```

```python
from quadmotorhat import M1, M2, M3, M4
```