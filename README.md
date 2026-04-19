# Clinical Sentinel | Email Malware Scanner

Clinical Sentinel is a premium, enterprise-grade frontend application designed for deep email security analysis. It provides an "Editorial-Security" hybrid interface that prioritizes clarity, precision, and authority in detecting malicious email content.

## 🚀 How It Works

The application is built as a highly responsive, standalone frontend that manages its own state and simulations.

### Core Features
- **Heuristic Scanning**: Paste email headers or raw source code into the **Full Scanner** for forensic analysis.
- **File Upload**: Support for `.eml` and `.msg` file analysis.
- **Threat Feed**: A real-time monitoring dashboard for local scanning activity.
- **Security Vault**: A dedicated section for managing quarantined or flagged data.
- **Multi-language Support**: Fully localized in English (EN) and Spanish (ES) using a custom `i18n.js` system.

### Tech Stack
- **Frontend**: Vanilla HTML5, JavaScript (ES6+), and Tailwind CSS.
- **Icons**: Google Material Symbols (Outlined).
- **Persistence**: `localStorage` is used to persist user sessions, scan history, and language preferences.
- **Localization**: A custom `data-i18n` attribute system managed by `i18n.js`.

---

## 🛠 Project Structure

- `dashboard.html`: The main analytical dashboard.
- `functional scanner.html`: The core scanning interface with file upload and direct input.
- `threat feed.html`: Activity monitoring and threat visualization.
- `i18n.js`: Centralized translation dictionary and logic.
- `DESIGN.md`: Comprehensive guide to the clinical design system.
- `*.py`: Developer utility scripts for maintaining icons, translations, and layout consistency.

---

## 🔌 Connecting a Backend

Currently, the scanner uses a **Simulation Engine** (managed in `functional scanner.html`) to demonstrate functionality. To connect a real backend (e.g., Python/FastAPI, Node.js/Express, or PHP), follow these steps:

### 1. Update the Execution Logic
In `functional scanner.html`, locate the `startScanSimulation` function. You need to replace the `setTimeout` block with an asynchronous `fetch` call to your API.

#### Existing Logic (Simulation):
```javascript
function startScanSimulation() {
    // ... animation setup ...
    setTimeout(() => {
        showResults();
    }, 1500);
}
```

#### New Logic (Real Backend):
```javascript
async function startScanSimulation() {
    // ... animation setup ...
    const payload = inputHeaders.value.trim();
    
    try {
        const response = await fetch('https://your-api-endpoint.com/v1/scan', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email_content: payload })
        });
        
        const data = await response.json();
        showResults(data); // Pass backend data to the results display
    } catch (error) {
        console.error("Scan failed:", error);
        // Handle error in UI
    }
}
```

> [!TIP]
> **CORS Configuration**: If your backend is hosted on a different domain or port than your frontend, remember to enable **CORS (Cross-Origin Resource Sharing)** in your backend settings to allow the frontend to communicate with it.

### 2. Suggested Backend Implementation (Example)
If you are using **Python with FastAPI**, your endpoint might look like this:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ScanRequest(BaseModel):
    email_content: str

@app.post("/v1/scan")
async def scan_email(request: ScanRequest):
    # Perform your security checks here (YARA, Regex, SPF/DMARC lookup)
    is_malicious = "malware" in request.email_content.lower()
    
    return {
        "isMalicious": is_malicious,
        "score": 0.95 if is_malicious else 0.01,
        "threats": ["Suspicious Link"] if is_malicious else []
    }
```

### 3. Update result rendering
In `showResults()`, update the UI elements (e.g., `resultStatus.textContent`) using the data returned from your API instead of the `Math.random()` simulation.

---

## 👨‍💻 Developer Notes

### Managing Translations
To add new strings:
1. Add the key and its translations to `i18n.js`.
2. Use `<span data-i18n="your_key">Default Text</span>` in your HTML.
3. If adding many strings, use `apply_total_localization.py` to automate the process.

### Icon Maintenance
The project uses `Material Symbols Outlined`. If icons aren't rendering correctly, run `fix_body_icons.py` to ensure all icons are wrapped in the correct `<span>` tags with the appropriate CSS classes.