# Design System Strategy: The Clinical Sentinel

## 1. Overview & Creative North Star
This design system moves away from the generic "dashboard" aesthetic to embrace a Creative North Star we call **"The Clinical Sentinel."** 

In the high-stakes environment of email security, "trust" isn't built with heavy borders or aggressive alerts; it is built through precision, breathing room, and editorial authority. We reject the "standard" boxy UI in favor of an **Editorial-Security hybrid**. This approach uses intentional asymmetry, generous whitespace, and a sophisticated layering of surfaces to create an interface that feels less like a utility and more like a high-end diagnostic tool. 

By leveraging deep tonal shifts and massive corner radii, we create a signature visual identity that communicates both technological superiority and human-centric clarity.

---

## 2. Colors & Surface Architecture
The palette is rooted in a spectrum of "High-Trust Blues" and "Security Neutrals." However, the application of these colors must follow a strict architectural hierarchy to avoid a flat, "templated" look.

### The "No-Line" Rule
To achieve a premium editorial feel, **prohibit the use of 1px solid borders for sectioning content.** Standard lines create visual noise. Instead, define boundaries through background color shifts. A `surface-container-low` section sitting against a `background` provides all the definition a user needs without the "grid" fatigue.

### Surface Hierarchy & Nesting
Treat the UI as a physical stack of materials. Use the `surface-container` tiers to create depth:
- **Level 0 (Background):** `#f7f9ff` — The canvas.
- **Level 1 (Sections):** `surface-container-low` (`#f1f3f9`) — Used for large structural blocks.
- **Level 2 (Interactive Elements):** `surface-container-lowest` (`#ffffff`) — Cards containing active data should sit on top of Level 1.
- **Level 3 (High Prominence):** `surface-bright` — Reserved for critical focus areas.

### Signature Textures
While the user requested "no gradients," we will implement **Micro-Tonal Transitions**. For primary actions, use a barely-perceivable transition from `primary` (#003d9b) to `primary_container` (#0052cc). This adds "soul" and a three-dimensional quality to buttons that flat hex codes cannot achieve.

---

## 3. Typography: Editorial Authority
We use **Inter** not as a system font, but as a clinical typeface. The hierarchy is designed to guide the eye through high-contrast scale shifts.

- **The Display Scale:** Use `display-lg` (3.5rem) for high-level security statuses (e.g., "99.9% Secure"). It should feel authoritative and monumental.
- **The Label Scale:** Use `label-sm` (0.6875rem) in all-caps with increased letter spacing (+5%) for metadata and overlines. This creates a "technical" feel that balances the softer, rounded corners of the UI.
- **Body Context:** `body-lg` (1rem) is the workhorse. Ensure a line height of 1.6x to maintain the "Editorial" readability standard.

---

## 4. Elevation & Depth
In this design system, depth is a function of light and color, not heavy shadows.

- **Tonal Layering:** Always prefer stacking a lighter surface on a darker surface over using a shadow. For example, a `#ffffff` card on a `#eceef4` background creates a natural, clean lift.
- **Ambient Shadows:** When an element must "float" (like a dropdown or a critical malware alert), use a shadow with a **24px to 48px blur** and an opacity of **4% to 6%**. The shadow color must be a tinted version of `on_surface` (a deep navy-tinted grey) rather than pure black.
- **The "Ghost Border" Fallback:** If a container requires more definition for accessibility, use the `outline_variant` at **15% opacity**. It should feel like a suggestion of a border, not a hard constraint.
- **Glassmorphism:** For overlays or navigation sidebars, use `surface` colors at 80% opacity with a `20px` backdrop-blur. This allows the scanner's activity (background pulses) to peek through, maintaining a sense of "active monitoring."

---

## 5. Components

### Buttons
- **Shape:** Fixed `40px` (Full Pill) radius.
- **Primary:** `primary` background with `on_primary` text. Use a subtle inner-glow (top-down) for a tactile feel.
- **Secondary:** `surface_container_highest` background. No border.
- **Interaction:** On hover, a button shouldn't just change color; it should "lift" using a subtle `surface_container_lowest` shift.

### The Security Card
- **Shape:** `24px` radius.
- **Structure:** No dividers. Separate the "Sender Info" from the "Malware Payload Data" using a vertical spacing shift of `2rem` (`xl`).
- **Surface:** Use `surface_container_lowest` (#ffffff) to make the card feel like a clean sheet of paper resting on the clinical background.

### Input Fields
- **Styling:** Avoid the "box" look. Use a `surface_container_high` background with a `bottom-only` ghost border.
- **States:** On focus, the border transitions to `primary` with a 2px weight, and the background shifts to `surface_bright`.

### Threat Indicators (Chips)
- **High Risk:** `error_container` background with `on_error_container` text. 
- **Clean:** `success` (as defined in original request) but softened with 10% opacity for the background and 100% opacity for the text.

---

## 6. Do's and Don'ts

### Do:
- **Use Intentional Asymmetry:** Align the main headline to the left but place the "Scan Status" CTA in a floating, offset position to break the "template" feel.
- **Embrace Negative Space:** If a screen feels "empty," leave it. In security, white space equals "calm" and "control."
- **Prioritize Tonal Shifts:** Use the difference between `surface_container_low` and `surface_container_high` to group related email metadata.

### Don't:
- **Don't use 100% Black:** Always use `on_surface` (#181c20) for text to maintain the premium, soft-contrast clinical look.
- **Don't use 1px Dividers:** Never use a horizontal line to separate list items. Use a `1rem` gap and a subtle background hover state.
- **Don't use sharp corners:** Even "small" elements like checkboxes must have at least a `4px` radius to remain consistent with the system's approachable clinical nature.