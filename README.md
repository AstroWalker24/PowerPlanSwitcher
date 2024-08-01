# PowerPlanSwitcher

A Python script that switches between predefined power plans based on the time of day. This script uses the `powercfg` command line tool to change the power plan on Windows.


## Power Plans

- **Balanced**: 8 AM - 6 PM
- **Power Saver**: Midnight - 8 AM
- **High Performance**: 6 PM - Midnight


## Getting Started

### Prerequisites

- Python 3.x
- Windows Operating System

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/PowerPlanSwitcher.git
    cd PowerPlanSwitcher
    ```

2. (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    ```

### Usage

Run the script using Python:

```bash
python switch_power_plan.py



You can customize the power plan GUIDs and time ranges by editing the switch_power_plan.py file.

